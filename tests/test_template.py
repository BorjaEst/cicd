"""Unittest module template."""

import unittest

from cicd import module_template


def init(Level):
    print(">>--Init {}".format(Level))


def down(Level):
    print("<<--Down {}".format(Level))


class Tests(unittest.TestCase):
    """Tests for application."""

    def group_001(self):
        """Run tests calling setUp/tearDown from module"""
        init(Level="group_001")
        module_template.Tests('test_001').run()
        module_template.Tests('test_002', value=1).run()
        down(Level="group_001")

    def group_002(self):
        """Run tests omiting setUp/tearDown from module"""
        init(Level="group_002")
        module_template.Tests('test_001').test_001()
        module_template.Tests('test_002', value=2).test_002()
        down(Level="group_002")

    def group_010(self, Level):
        """New group that takes the previous 2"""
        init(Level=Level)
        self.group_001()
        self.group_002()
        down(Level=Level)

    def test_001(self):
        """Test that calls group1 using level 001"""
        self.group_010(Level="Root test_001")

    def test_002(self):
        """Test that calls group1 using level 002"""
        self.group_010(Level="Root test_002")
