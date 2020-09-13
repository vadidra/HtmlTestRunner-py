#https://github.com/oldani/HtmlTestRunner

from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner

import test_precondition
import exampletest1
import exampletest2

tests_precondition = TestLoader().loadTestsFromTestCase(test_precondition.TestPrecondition)
example_tests = TestLoader().loadTestsFromTestCase(exampletest1.ExampleTest1)
example2_tests = TestLoader().loadTestsFromTestCase(exampletest2.ExampleTest2)

suite = TestSuite([
    tests_precondition,
    example_tests, 
    example2_tests
    ])

runner = HTMLTestRunner(
    output=r'C:\test1',
    report_name="Test-Report",
    combine_reports=True
    )

runner.run(suite)
