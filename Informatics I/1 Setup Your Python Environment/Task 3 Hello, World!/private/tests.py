import sys
from io import StringIO
from unittest import TestCase

# You don't need to worry about this yet.
class PublicTestSuite(TestCase):

    def test_prints_something(self):
        capture = StringIO()
        sys.stdout = capture
        from public import hello
        sys.stdout = sys.__stdout__
        m = "@@The output is not 'Hello, World!'@@"
        self.assertEqual(capture.getvalue(), "Hello, World!\n", m)

