from typing import List, Dict
from pathlib import Path


class ReportGenerator:
    def __init__(self, output_path: Path):
        self.output_path = output_path

    def generate_markdown(
        self,
        summaries: List[Dict[str, str]],
        include_title: bool = True,
    ) -> None:
        lines = []

        if include_title:
            lines.append("# 📘 Extracted Business Requirements\n")


        # @todo stupid design, maybe work more one that one
        for item in summaries:
            method = item["method"]
            description = item["description"]
            file = item.get("file", "N/A")
            lineno = item.get("lineno", "N/A")

            lines.append(f"## 🔹 `{method}`")
            lines.append(f"**Location**: `{file}:{lineno}`")  # @todo send link on repo ?
            lines.append("")
            lines.append(f"**Description**:\n{description}")
            lines.append("\n---\n")

        markdown_content = "\n".join(lines)
        self._write_to_file(markdown_content)

    def _write_to_file(self, content: str):
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(content, encoding="utf-8")
