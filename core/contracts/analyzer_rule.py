# Define plug-in rules for static analysis
# Enable rule-based architecture

from abc import ABC, abstractmethod
from typing import List
import ast


class AnalyzerRule(ABC):
    """Base contract for static code analysis rules."""

    @abstractmethod
    def analyze(self, tree: ast.AST) -> List[str]:
        """
        Analyze an AST tree and return a list of issues.
        """
        pass
