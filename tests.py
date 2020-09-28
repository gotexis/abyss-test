import unittest

from main import count_areas


class TestCases(unittest.TestCase):

    def test_1(self):
        pic = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 20, 0, 0],
            [0, 0, 0, 0, 20, 20, 0],
            [0, 0, 0, 0, 20, 20, 0],
        ]
        result = count_areas(pic)
        self.assertDictEqual(result, {'total_sectors': 4, 'colors': {0: 1, 1: 1, 20: 1}})

    def test_2(self):
        pic = [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 1, 2, 2, 0, 0, 0],
            [0, 0, 2, 2, 20, 0, 0],
            [0, 0, 0, 0, 20, 20, 0],
            [0, 0, 0, 0, 20, 20, 0],
        ]
        result = count_areas(pic)
        self.assertDictEqual(result, {'total_sectors': 6, 'colors': {0: 2, 1: 1, 2: 1, 20: 1}})


if __name__ == '__main__':
    unittest.main()
