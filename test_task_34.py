#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import unittest

from task_34 import Matrix


# Используя модуль unittests написать тесты: сложения двух
# матриц, умножения матрицы и метод transpose
class TestMatrixMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        cls.first_matrix = Matrix(data)
        cls.second_matrix = Matrix(data)

    @classmethod
    def tearDownClass(cls):
        del cls.first_matrix, cls.second_matrix  # for example.
        print("That's all folks")

    def test_matrix_sum(self):
        self.assertEqual(
            self.first_matrix + self.second_matrix,
            [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        )

    def test_matrix_mul(self):
        self.assertEqual(
            self.first_matrix * 3,
            [[3, 6, 9], [12, 15, 18], [21, 24, 27]]
        )

    def test_matrix_transpose(self):
        self.assertEqual(
            self.first_matrix.get_transpose(),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        )


if __name__ == '__main__':
    unittest.main()
