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
    def __init__(self, testName, value=None):
        super().__init__(testName)
        self.value = value

    def setUp(self):
        """Set up test fixtures, if any (once per case).
        """
        print("Test setUp")

    def tearDown(self):
        """Tear down test fixtures, if any (once per case).
        """
        print("Test tearDown")

    def test_001(self):
        self.assertTrue(hello_world())
        self.assertFalse(False)

    def test_002(self):
        print("Param value: {}".format(self.value))
        self.assertIsInstance(self.value, int)
