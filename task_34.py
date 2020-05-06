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
# 5. Метод __add__ принимающий второй экземпляр класса Matrix и возвращающий
# сумму матриц, если передалась на вход матрица другого размера - поднимать
# исключение MatrixSizeError (по желанию реализовать так, чтобы текст ошибки
# содержал размерность 1 и 2 матриц - пример:"Matrixes have different sizes -
# Matrix(x1, y1) and Matrix(x2, y2)")
# 6. __mul__ принимающий число типа int или float и
# возвращающий матрицу, умноженную на скаляр.
# 7. __str__ переводящий матрицу в строку. Столбцы разделены между собой
# табуляцией, а строки — переносами строк (символ новой строки). При этом
# после каждой строки не должно быть символа табуляции и в конце не должно
# быть переноса строки
from copy import deepcopy


class Matrix:

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(
            ['\t'.join(
                [str(element) for element in row]
            ) for row in self.matrix]
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise Exception('Give me my int or float, %username%')

        return [
            [element * scalar for element in row]
            for row in self.matrix
        ]

    def __add__(self, second_matrix_obj):
        if not isinstance(second_matrix_obj, Matrix):
            raise Exception('Neo not happy.')

        if self.size != second_matrix_obj.size:
            raise Exception(
                f"Matrices have different sizes - Matrix{self.size} "
                f"and Matrix{second_matrix_obj.size}"
            )

        return [
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.matrix, second_matrix_obj.matrix)
        ]

    @property
    def size(self):
        columns = len(self.matrix)
        rows = len(self.matrix[0])

        return rows, columns

    def get_transpose(self):
        self.matrix = list(map(list, (zip(*self.matrix))))

        return self.matrix

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
    print(f'Size of matrix {matrix_obj.size}')
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

    print('Second part of tasks')
    print(str(matrix_immmut_obj))
    print(matrix_immmut_obj * 2)
    print(matrix_immmut_obj + matrix_immmut_obj)
    matrix_dif_size = Matrix([
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ])

    try:
        matrix_immmut_obj + matrix_dif_size

    except Exception as e:
        print(f"Huston, we have a problem here. I mean {e}")
