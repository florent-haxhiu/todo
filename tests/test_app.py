import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("First test")
        self.assertEqual(True, True)  # add assertion here
