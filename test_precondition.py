import HtmlTestRunner
import unittest


class TestPrecondition(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_pr11(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_pr12(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_pr13(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

