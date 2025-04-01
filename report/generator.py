from typing import List, Dict, Optional
from pathlib import Path


class ReportGenerator:
    def __init__(self, output_path: Path):
        self.output_path = output_path


        # obviously should not be hardcoded, just for test
        self.repo_base_url = "https://github.com/jagjot2008/EeazyCRM/tree/master"

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
            # link = self._build_git_link(file, lineno)


            lines.append(f"## 🔹 `{method}`")
            lines.append(f"**Location**: `{file}:{lineno}`")  # todo Link could added
            lines.append("")
            lines.append(f"**Description**:\n{description}")
            lines.append("\n---\n")

        markdown_content = "\n".join(lines)
        self._write_to_file(markdown_content)

    def _write_to_file(self, content: str):
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(content, encoding="utf-8")
