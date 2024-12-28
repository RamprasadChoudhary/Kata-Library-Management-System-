# run_tests.py
import pytest
import os

def run_tests():
    """Run the test suite and generate HTML report"""
    # Run pytest with HTML report generation
    pytest.main(["-v", "--html=test_report.html", "--self-contained-html"])
    
    # Print the location of the test report
    print("\nTest report generated: test_report.html")
    
    # Get the absolute path of the report
    report_path = os.path.abspath("test_report.html")
    print(f"Full path: {report_path}")

if __name__ == "__main__":
    run_tests()