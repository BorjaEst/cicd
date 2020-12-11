"""Unittest module template."""

import unittest

from cicd import module_template


def group(*tests):
    suite = unittest.TestSuite()
    for testCase in tests:
        suite.addTest(testCase)
    return suite


def load_tests(loader, tests, pattern):
    group1 = group(
        module_template.Tests('test_001'),
        module_template.Tests('test_002')
    )
    return group1
