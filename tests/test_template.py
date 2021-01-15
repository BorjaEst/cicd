"""Unittest module template."""

import unittest

from cicd import module_template


def suite_001(param):
    """Returns suite_001 suite"""
    suite = unittest.TestSuite()
    suite.addTest(module_template.Tests('test_002', value=param+1))
    suite.addTest(module_template.Tests('test_002', value=param-1))
    return suite


class Group_001(unittest.TestCase):
    """Tests for application, Group 001"""

    def setUp(self):
        """Set up group fixtures, if any (once per case)."""
        print("Group 001 setUp")

    def tearDown(self):
        """Tear down group fixtures, if any (once per case)."""
        print("Group 001 tearDown")

    def test_001(self):
        print("This is test 001")
        runner = unittest.TextTestRunner()
        result = runner.run(suite_001(param=1))
        self.assertTrue(result.wasSuccessful())


class Group_002(unittest.TestCase):
    """Tests for application, Group 001"""

    def setUp(self):
        """Set up group fixtures, if any (once per case)."""
        print("Group 002 setUp")

    def tearDown(self):
        """Tear down group fixtures, if any (once per case)."""
        print("Group 002 tearDown")

    def test_002(self):
        print("This is test 002")
        runner = unittest.TextTestRunner()
        result = runner.run(Group_001("test_001"))
        self.assertTrue(result.wasSuccessful()) 
