import unittest

from logics import *


class Test_2048(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_9(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas),False)

    def test_10(self):
        mas = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 0, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas),True)

    def test_12(self):
        mas = [
            [2, 2, 0, 0],
            [2, 0, 4, 0],
            [4, 0, 4, 0],
            [0, 0, 2, 2]
        ]
        rez =[
        [4, 0, 0, 0],
        [2, 4, 0, 0],
        [8, 0, 0, 0],
        [4, 0, 0, 0]
            ]
        self.assertEqual(move_left(mas),rez)

    def test_13(self):
        mas = [
            [0, 0, 4, 0],
            [0, 2, 0, 0],
            [2, 0, 4, 4],
            [2, 2, 4, 4]
        ]
        rez = [
        [4, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 8, 0, 0],
        [4, 8, 0, 0]
        ]
        self.assertEqual(move_left(mas),rez)

    def test_14(self):
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        rez = [
        [4, 8, 4, 2],
        [8, 0, 0, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas),rez)