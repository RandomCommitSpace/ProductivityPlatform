import ast
import re
from core.contracts.analyzer_rule import AnalyzerRule

class VariableNamingRule(AnalyzerRule):
    """Flags variables that are not snake_case."""

    SNAKE_CASE_REGEX = re.compile(r'^[a-z_][a-z0-9_]*$')

    def analyze(self, tree: ast.AST):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    if not self.SNAKE_CASE_REGEX.match(node.id):
                        issues.append(f"Variable '{node.id}' is not snake_case")
        return issues
