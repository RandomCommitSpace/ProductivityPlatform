class Reporter:
    """Generates a readable report from analysis results."""

    def generate(self, analysis_results: dict):
        for file_path, issues in analysis_results.items():
            print(f"\nFile: {file_path}")
            if not issues:
                print("  No issues found ✅")
            else:
                for issue in issues:
                    print(f"  ⚠️ {issue}")
