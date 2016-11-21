import unittest
import get_em as g


class T(unittest.TestCase):
    testfile1 = "/home/s/dotfiles/GetMyPackages/test_installed.txt"
    testfile2 = "/home/s/dotfiles/GetMyPackages/test_installed_via_wget.txt"
    test_packages = ['add-apt-key', 'weizenbier']
    to_fail = ['weizenbier']
    to_fail_wget = ['dies/ist/keine/url']

    def test_get_content(self):
        c = g.get_content(self.testfile1)
        self.assertEqual(c, self.test_packages)

    def test_install_all(self):
        mal = g.install_all(g.get_content(self.testfile1), True)
        self.assertEqual(mal, self.to_fail)

    def test_install_via_wget(self):
        mal_d, mal_z = g.install_via_wget(g.get_content(self.testfile2))
        self.assertEqual(mal_d, self.to_fail_wget)
