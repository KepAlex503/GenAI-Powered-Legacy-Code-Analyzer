import ast
from pathlib import Path
from typing import List, Dict, Optional, Any
import matplotlib.pyplot as plt

# @todo too many methods overrided


class MethodInfo:
    def __init__(
        self,
        name: str,
        class_name: Optional[str],
        args: List[str],
        return_type: Optional[str],
        lineno: int,
        calls: List[str]
    ):
        self.name = name
        self.class_name = class_name
        self.args = args
        self.return_type = return_type
        self.lineno = lineno
        self.calls = calls

    def full_name(self) -> str:
        return f"{self.class_name}.{self.name}" if self.class_name else self.name

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "class_name": self.class_name,
            "args": self.args,
            "return_type": self.return_type,
            "lineno": self.lineno,
            "calls": self.calls,
        }


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self, filename: Path):
        self.filename = filename
        self.methods: List[MethodInfo] = []
        self.current_class: Optional[str] = None

    def visit_ClassDef(self, node: ast.ClassDef):
        previous_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = previous_class

    def visit_FunctionDef(self, node: ast.FunctionDef):
        args = [arg.arg for arg in node.args.args if arg.arg != 'self']
        return_type = self._get_annotation(node.returns)
        calls = self._extract_calls(node)

        method_info = MethodInfo(
            name=node.name,
            class_name=self.current_class,
            args=args,
            return_type=return_type,
            lineno=node.lineno,
            calls=calls
        )
        self.methods.append(method_info)
        self.generic_visit(node)

    def _get_annotation(self, annotation: Optional[ast.expr]) -> Optional[str]:
        if annotation is None:
            return None
        if isinstance(annotation, ast.Name):
            return annotation.id
        if isinstance(annotation, ast.Subscript):
            return self._get_subscript(annotation)
        return ast.dump(annotation)

    def _get_subscript(self, node: ast.Subscript) -> str:
        value = getattr(node.value, 'id', '')
        slice_repr = self._get_annotation(node.slice)
        return f"{value}[{slice_repr}]"

    def _extract_calls(self, node: ast.FunctionDef) -> List[str]:
        calls = []

        class CallVisitor(ast.NodeVisitor):
            def visit_Call(self, call_node: ast.Call):
                if isinstance(call_node.func, ast.Attribute):
                    calls.append(call_node.func.attr)
                elif isinstance(call_node.func, ast.Name):
                    calls.append(call_node.func.id)

        CallVisitor().visit(node)
        return calls

    def parse(self) -> List[MethodInfo]:
        with self.filename.open("r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename=str(self.filename))
            self.visit(tree)
        return self.methods


# @todo maybe add ignore names so save money on some tests analyzing for example
def analyze_directory(path: Path) -> List[Dict[str, Any]]:
    python_files = list(path.rglob("*.py"))
    all_methods = []

    for file in python_files:
        analyzer = CodeAnalyzer(file)
        methods = analyzer.parse()
        for method in methods:
            data = method.to_dict()
            data["file"] = str(file)
            all_methods.append(data)

    return all_methods
