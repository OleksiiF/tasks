#!/usr/bin/env python3
#-*- coding: utf-8 -*-


# Написать функцию, которая принимает 2 числа.
# Функция должна вернуть сумму всех элементов числового ряда между этими двумя числами.
# (если подать 1 и 5 на вход, то результат должен считаться как 1+2+3+4+5 = 15)
def get_sum_between(a, b):
    if a > b:
        a, b = b, a

    return sum(range(a, b + 1))


# Определить количество четных и нечетных чисел в заданном списке.
# Оформить в виде функции, где на вход будет подаваться список с целыми числами.
# Результат функции должен быть 2 числа, кол-во четных и нечетных соответственно.
def count_even_odd(digits):
    even = 0
    odd = 0

    for digit in digits:
        if digit % 2:
            odd += 1
        else:
            even += 1

    return even, odd


# Реализовать алгоритм бинарного поиска на python.
# На вход подается упорядоченный список целых чисел, а так же элемент,
# который необходимо найти и указать его индекс, в противном случае –
# указать что такого элемента нет в заданном списке.
def binary_search(digits, target):
    result = 'Nope'

    if digits:
        work_horse = len(digits) // 2
        start = 0
        end = len(digits) - 1

        while digits[work_horse] != target and start <= end:
            if target > digits[work_horse]:
                start = work_horse + 1

            else:
                end = work_horse - 1

            work_horse = (start + end) // 2

        if digits[work_horse] == target:
            result = work_horse

    return result


if __name__ == '__main__':
    assert get_sum_between(1,5) == 15
    assert get_sum_between(5,7) == 18
    assert get_sum_between(0,-3) == -6
    assert get_sum_between(1, 1) == 1

    assert count_even_odd(list(range(5))) == (3, 2)
    assert count_even_odd(list(range(-3, 4))) == (3, 4)
    assert count_even_odd(list(range(-3, 4))) == (3, 4)

    assert binary_search(list(range(5)), 3) == 3
    assert binary_search(list(range(-5, 5)), 1) == 6
    assert binary_search(list(range(-5, 5)), 6) == 'Nope'
    assert binary_search([0], 1) == 'Nope'
    assert binary_search([], 13) == 'Nope'

    print('Uhuuu!!!')
