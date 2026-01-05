from pathlib import Path
from code_analyzer.analyzer import CodeAnalyzer

analyzer = CodeAnalyzer()
analyzer.analyze_directory(Path("habit_engine"))  # analyze your own modules


# python -m tests.code_analyzer_test
