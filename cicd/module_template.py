"""Python module template."""
import unittest


def hello_world(*arg, **kwarg):
    print("Hello World")
    if arg or kwarg:
        print(f"  - Arguments as Inputs: {arg}")
        print(f"  - Arguments as KeyVal: {kwarg}")
    return True


class Tests(unittest.TestCase):
    """Tests for `module_template` package."""
    def __init__(self, testName):
        super().__init__(testName)

    def setUp(self):
        """Set up test fixtures, if any (once per case).
        """
        self.value = 1

    def tearDown(self):
        """Tear down test fixtures, if any (once per case).
        """
        self.value = 0

    def test_001(self):
        self.assertTrue(hello_world())
        self.assertFalse(False)

    def test_002(self):
        self.assertEqual(self.value, 1)
        self.assertIsInstance(self.value, int)
