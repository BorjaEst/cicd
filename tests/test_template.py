"""Unittest module template."""

import unittest

from cicd import module_template


class Group_001(unittest.TestCase):
    """Tests for application, Group 001"""

    def setUp(self):
        """Set up group fixtures, if any (once per case)."""
        print("Group 001 setUp")

    def tearDown(self):
        """Tear down group fixtures, if any (once per case)."""
        print("Group 001 tearDown")

    def suite_001(self):
        """Returns suite_001 suite"""
        suite = unittest.TestSuite()
        suite.addTest(module_template.Tests('test_001'))
        suite.addTests(self.suite_002())
        return suite

    def suite_002(self):
        """Returns suite_002 suite"""
        suite = unittest.TestSuite()
        suite.addTest(module_template.Tests('test_002', value=1))
        suite.addTest(module_template.Tests('test_002', value=2))
        return suite

    def test_001(self):
        runner = unittest.TextTestRunner()
        result = runner.run(self.suite_001())
        self.assertTrue(result.wasSuccessful())


class Group_002(unittest.TestCase):
    """Tests for application, Group 001"""

    def setUp(self):
        """Set up group fixtures, if any (once per case)."""
        print("Group 002 setUp")

    def tearDown(self):
        """Tear down group fixtures, if any (once per case)."""
        print("Group 002 tearDown")

    def suite_001(self):
        """Returns suite_001 suite"""
        suite = unittest.TestSuite()
        suite.addTest(Group_001('test_001'))
        return suite

    def test_001(self):
        runner = unittest.TextTestRunner()
        result = runner.run(self.suite_001())
        self.assertTrue(result.wasSuccessful())
