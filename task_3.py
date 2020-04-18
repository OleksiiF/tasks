#!/usr/bin/env python3
#-*- coding: utf-8 -*-


# Реализовать некий класс Matrix, у которого:
# 1. Есть собственный конструктор, который принимает в качестве аргумента -
# список списков, копирует его (то есть при изменении списков,
# значения в экземпляре класса не должны меняться).
# Элементы списков гарантированно числа, и не пустые.
# 2. Метод size без аргументов, который возвращает кортеж вида
# (число строк, число столбцов).
# 3. Метод transpose, транспонирующий матрицу и возвращающую результат
# (данный метод модифицирует экземпляр класса Matrix)
# 4. На основе пункта 3 сделать метод класса create_transposed,
# который будет принимать на вход список списков, как и в пункте 1,
# но при этом создавать сразу транспонированную матрицу.
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def get_size(self):
        columns = len(self.matrix)
        rows = len(self.matrix[0])

        return rows, columns

    def get_transpose(self):
        result = [[] for i in range(len(self.matrix[0]))]

        for index_row, row in enumerate(self.matrix):
            for index_element, element in enumerate(row):
                result[index_element].append(element)

        self.matrix = result

        return result

    @classmethod
    def create_transposed(cls, matrix):
        matrix_obj = cls(matrix)
        matrix_obj.get_transpose()

        return matrix_obj

    @staticmethod
    def matrix_print(data):
        for row in data:
            for element in row:
                print(element, end=' ')
            print()


if __name__ == '__main__':
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_obj = Matrix(data)
    print(f'Size of matrix {matrix_obj.get_size()}')
    print('Initial matrix')
    Matrix.matrix_print(matrix_obj.matrix)
    # Transpose matrix
    print('Transposed matrix')
    Matrix.matrix_print(matrix_obj.get_transpose())
    # Create transpose matrix
    trans_matrix_obj = Matrix.create_transposed(data)
    print('Initial matrix with transpose')
    Matrix.matrix_print(trans_matrix_obj.matrix)
    # Check for matrix_obj immutable
    matrix_immmut_obj = Matrix(data)
    print('You already saw it')
    Matrix.matrix_print(matrix_immmut_obj.matrix)
    print('Mute data source')
    data[1][1] = 'Some new value'
    Matrix.matrix_print(matrix_immmut_obj.matrix)
