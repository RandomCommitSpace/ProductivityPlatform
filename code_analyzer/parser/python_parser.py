import ast
from pathlib import Path

class PythonParser:
    """Parses Python files into ASTs."""

    def parse_file(self, file_path: Path) -> ast.AST:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        return ast.parse(source, filename=str(file_path))

    def parse_directory(self, dir_path: Path):
        """Generator yielding (file_path, AST) for all .py files."""
        for py_file in dir_path.rglob("*.py"):
            yield py_file, self.parse_file(py_file)

