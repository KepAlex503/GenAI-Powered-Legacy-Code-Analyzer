import ast
from pathlib import Path
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class MethodInfo:
    name: str
    class_name: Optional[str]
    args: List[str]
    return_type: Optional[str]
    lineno: int
    calls: List[str]
    file: Optional[str] = None

    def full_name(self) -> str:
        return f"{self.class_name}.{self.name}" if self.class_name else self.name

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)  # refactor
        data["full_name"] = self.full_name()
        return data


class MethodExtractor(ast.NodeVisitor):
    def __init__(self):
        self.methods: List[MethodInfo] = []
        self.current_class: Optional[str] = None

    def visit_ClassDef(self, node: ast.ClassDef):
        prev_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = prev_class

    def visit_FunctionDef(self, node: ast.FunctionDef):
        args = [arg.arg for arg in node.args.args if arg.arg != "self"]
        return_type = self._resolve_annotation(node.returns)
        calls = self._find_calls(node)

        method = MethodInfo(
            name=node.name,
            class_name=self.current_class,
            args=args,
            return_type=return_type,
            lineno=node.lineno,
            calls=calls
        )
        self.methods.append(method)
        self.generic_visit(node)

    def _resolve_annotation(self, annotation: Optional[ast.expr]) -> Optional[str]:
        if annotation is None:
            return None
        if isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Subscript):
            return self._get_subscript(annotation)
        return ast.unparse(annotation)

    def _get_subscript(self, node: ast.Subscript) -> str:
        base = getattr(node.value, "id", "")
        sub = self._resolve_annotation(node.slice)
        return f"{base}[{sub}]"

    def _find_calls(self, node: ast.FunctionDef) -> List[str]:
        calls = []

        class CallCollector(ast.NodeVisitor):
            def visit_Call(self, call_node: ast.Call):
                if isinstance(call_node.func, ast.Attribute):
                    calls.append(call_node.func.attr)
                elif isinstance(call_node.func, ast.Name):
                    calls.append(call_node.func.id)

        CallCollector().visit(node)
        return calls


def parse_python_file(path: Path) -> List[MethodInfo]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    extractor = MethodExtractor()
    extractor.visit(tree)

    for method in extractor.methods:
        method.file = str(path)

    return extractor.methods


def analyze_directory(path: Path) -> List[Dict[str, Any]]:
    method_data: List[Dict[str, Any]] = []

    # can be added blacklist of methods\files to analyze (blacklist __init__ methodps for example)
    for file in path.rglob("*.py"):
        methods = parse_python_file(file)
        method_data.extend([m.to_dict() for m in methods])
    return method_data