import ast
from core.contracts.analyzer_rule import AnalyzerRule

class LongFunctionRule(AnalyzerRule):
    """Flags functions longer than 20 lines."""

    def analyze(self, tree: ast.AST):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start = node.lineno
                end = max(getattr(node, "end_lineno", node.lineno), node.lineno)
                if (end - start + 1) > 20:
                    issues.append(f"Function '{node.name}' is too long ({end-start+1} lines)")
        return issues
