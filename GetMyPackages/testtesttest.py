import unittest
import get_em


class t(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


def main():
    t.test_upper()

main()