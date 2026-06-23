"""Step Schemas — input/output contracts for every capability type.

Each step type defines:
- input_from: which upstream step types to consume
- consumes: which fields to read from upstream artifacts
- output: the structured output schema (field names + types)

This is the key to token-efficient graph execution:
- Steps pass FIELD REFERENCES, not full text
- Upstream extraction only takes what the schema declares
- No LLM guessing about output format
"""
from __future__ import annotations

STEP_SCHEMAS: dict[str, dict] = {
    "research": {
        "output": {
            "findings": ["string"],
            "constraints": ["string"],
            "open_questions": ["string"],
        },
        "prompt_template": "Research: {task}\nOutput JSON with findings, constraints, open_questions.",
    },
    "architecture": {
        "input_from": ["research"],
        "consumes": ["findings", "constraints"],
        "output": {
            "components": [{"name": "", "role": "", "tech": ""}],
            "decisions": [{"choice": "", "reason": ""}],
            "risks": ["string"],
        },
        "prompt_template": "Design architecture for: {task}\nBased on findings: {upstream_findings}\nConstraints: {upstream_constraints}\nOutput JSON with components, decisions, risks.",
    },
    "coding": {
        "input_from": ["architecture"],
        "consumes": ["components", "decisions"],
        "output": {
            "files": [{"path": "", "purpose": ""}],
            "impl_decisions": [{"choice": "", "reason": ""}],
        },
        "prompt_template": "Implement: {task}\nArchitecture: {upstream_components}\nDecisions: {upstream_decisions}\nOutput JSON with files, impl_decisions.",
    },
    "review": {
        "input_from": ["architecture", "coding"],
        "consumes": ["decisions", "components", "files"],
        "output": {
            "verdict": "approve|revise|reject",
            "issues": [{"severity": "", "description": "", "fix": ""}],
            "approved_decisions": ["string"],
        },
        "prompt_template": "Review: {task}\nComponents: {upstream_components}\nDecisions: {upstream_decisions}\nFiles: {upstream_files}\nOutput JSON with verdict, issues, approved_decisions.",
    },
    "writing": {
        "input_from": ["research"],
        "consumes": ["findings", "open_questions"],
        "output": {
            "sections": [{"heading": "", "content": ""}],
            "key_points": ["string"],
        },
        "prompt_template": "Write: {task}\nFindings: {upstream_findings}\nOutput JSON with sections, key_points.",
    },
    "reasoning": {
        "input_from": ["research"],
        "consumes": ["findings", "open_questions"],
        "output": {
            "analysis": ["string"],
            "conclusions": ["string"],
        },
        "prompt_template": "Analyze: {task}\nFindings: {upstream_findings}\nOutput JSON with analysis, conclusions.",
    },
}


def get_schema(step_type: str) -> dict:
    """Get the schema for a step type. Returns empty schema if not defined."""
    return STEP_SCHEMAS.get(step_type, {
        "output": {"result": ["string"]},
        "prompt_template": "{task}",
    })


def get_consumed_fields(step_type: str) -> list[str]:
    """Get the list of field names this step type consumes from upstream."""
    schema = STEP_SCHEMAS.get(step_type, {})
    return schema.get("consumes", [])


def get_input_sources(step_type: str) -> list[str]:
    """Get which upstream step types this step reads from."""
    schema = STEP_SCHEMAS.get(step_type, {})
    return schema.get("input_from", [])
