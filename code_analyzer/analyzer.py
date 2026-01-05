from pathlib import Path
from code_analyzer.parser.python_parser import PythonParser
from code_analyzer.rules.long_function_rule import LongFunctionRule
from code_analyzer.rules.variable_naming_rule import VariableNamingRule
from code_analyzer.report.reporter import Reporter

class CodeAnalyzer:
    """Runs all rules on a given directory."""

    def __init__(self):
        self.parser = PythonParser()
        self.rules = [LongFunctionRule(), VariableNamingRule()]
        self.reporter = Reporter()

    def analyze_directory(self, dir_path: Path):
        results = {}
        for file_path, tree in self.parser.parse_directory(dir_path):
            issues = []
            for rule in self.rules:
                issues.extend(rule.analyze(tree))
            results[file_path] = issues
        self.reporter.generate(results)
