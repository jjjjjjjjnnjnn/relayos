"""Context Compression — reduce token usage between workflow steps.

Strategies:
1. summary: LLM-based summarization to target length
2. extract: Extract key facts/decisions only
3. truncate: Simple character/token truncation
4. structured: Convert to structured format (JSON/ YAML)
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class CompressedContext:
    content: str
    original_chars: int
    compressed_chars: int
    ratio: float
    strategy: str


class ContextCompressor:
    """Compresses agent output between workflow steps."""

    STRATEGIES = ("summary", "extract", "truncate", "structured")

    def __init__(self, strategy: str = "summary", max_tokens: int = 500):
        if strategy not in self.STRATEGIES:
            strategy = "summary"
        self.strategy = strategy
        self.max_chars = max_tokens * 4  # ~4 chars per token

    def compress(self, content: str, strategy: Optional[str] = None) -> CompressedContext:
        """Compress content using the specified strategy."""
        strategy = strategy or self.strategy
        original_chars = len(content)

        if strategy == "truncate":
            compressed = self._truncate(content)
        elif strategy == "extract":
            compressed = self._extract(content)
        elif strategy == "structured":
            compressed = self._structured(content)
        else:  # summary
            compressed = self._summary(content)

        compressed_chars = len(compressed)
        ratio = compressed_chars / max(original_chars, 1)

        return CompressedContext(
            content=compressed,
            original_chars=original_chars,
            compressed_chars=compressed_chars,
            ratio=round(ratio, 3),
            strategy=strategy,
        )

    def _truncate(self, content: str) -> str:
        """Simple truncation with intelligent cutoff."""
        if len(content) <= self.max_chars:
            return content
        # Try to cut at a sentence boundary
        cut = content[:self.max_chars]
        last_period = cut.rfind(".")
        if last_period > self.max_chars * 0.7:
            return content[:last_period + 1] + "\n... [truncated]"
        return cut + "\n... [truncated]"

    def _extract(self, content: str) -> str:
        """Extract key information: decisions, numbers, conclusions."""
        lines = content.split("\n")
        important = []

        # Patterns that indicate important content
        key_patterns = [
            r"(?i)(conclusion|summary|result|finding|decision|recommend)",
            r"(?i)(therefore|thus|hence|consequently|finally)",
            r"(?i)(\d+[%]|increase|decrease|reduce|improve)",
            r"(?i)(key|important|crucial|critical|significant)",
            r"^#{1,3}\s",  # headings
            r"^\d+\.\s",  # numbered lists
            r"^-\s",      # bullet points
        ]

        for line in lines:
            line_stripped = line.strip()
            if not line_stripped:
                continue
            for pattern in key_patterns:
                if re.search(pattern, line_stripped):
                    important.append(line_stripped)
                    break

        result = "\n".join(important) if important else content[:self.max_chars]
        if len(result) > self.max_chars:
            result = result[:self.max_chars] + "\n... [extracted]"
        return result

    def _summary(self, content: str) -> str:
        """Structural summary — takes first/last sections and key points."""
        if len(content) <= self.max_chars:
            return content

        lines = content.split("\n")
        # Take first 20% (introduction) and last 20% (conclusion)
        split_point = len(lines) // 5
        intro = "\n".join(lines[:split_point])
        conclusion = "\n".join(lines[-split_point:])

        # Try to extract any bullet points or numbered lists
        key_points = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("- ") or stripped.startswith("* ") or re.match(r"^\d+\.", stripped):
                key_points.append(stripped)

        parts = []
        if intro.strip():
            parts.append(intro.strip())
        if key_points:
            points_str = "\n".join(key_points[:10])
            if len(points_str) < self.max_chars * 0.5:
                parts.append(points_str)
        if conclusion.strip() and conclusion.strip() != intro.strip():
            parts.append(conclusion.strip())

        result = "\n\n".join(parts)
        if len(result) > self.max_chars:
            result = result[:self.max_chars] + "\n... [summarized]"
        return result

    def _structured(self, content: str) -> str:
        """Convert to structured JSON-like format."""
        lines = content.split("\n")
        key_values = []

        for line in lines[:50]:  # Only scan first 50 lines
            stripped = line.strip()
            if ":" in stripped and len(stripped) < 200:
                key, _, val = stripped.partition(":")
                key = key.strip().strip("*#").strip()
                val = val.strip()
                if key and val and len(key) < 50:
                    key_values.append((key, val))

        if key_values:
            result = json.dumps(dict(key_values), ensure_ascii=False, indent=2)
            if len(result) > self.max_chars:
                result = result[:self.max_chars] + "\n... [structured]"
            return result

        return self._truncate(content)
