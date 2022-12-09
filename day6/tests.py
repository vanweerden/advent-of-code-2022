import unittest
from scanner import Scanner
# from main import Day6

class Day6Tests(unittest.TestCase):
    def test_scanner_is_marker__true(self):
        scanner = Scanner("")
        test = scanner.is_marker("abcd")
        self.assertTrue(test)

    def test_scanner_is_marker__false(self):
        scanner = Scanner("")
        test = scanner.is_marker("abca")
        self.assertFalse(test)

    def test_scanner_packet_scan_first(self):
        scanner = Scanner("abcdefgh")
        actual = scanner.start_of_packet()
        expected = 4
        self.assertEqual(actual, expected)   

    def test_scanner_packet_scan_middle(self):
        scanner = Scanner("aaabcdaaa")
        actual = scanner.start_of_packet()
        expected = 6
        self.assertEqual(actual, expected)   

    def test_scanner_packet_scan_end(self):
        scanner = Scanner("aaaabcd")
        actual = scanner.start_of_packet()
        expected = 7
        self.assertEqual(actual, expected)   

    def test_scanner_message_scan(self):
        scanner = Scanner("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
        actual = scanner.start_of_message()
        expected = 19
        self.assertEqual(actual, expected)   

if __name__ == '__main__':
    unittest.main()