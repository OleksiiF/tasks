#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Написать декоратор log, который будет выводить на экран все аргументы,
# которые передаются вызываемой функции.
def print_received_argument(func):
    def wrapper(*args, **kwargs):
        if args:
            print(*args)

        if kwargs:
            print(**kwargs)

        return func(*args, **kwargs)

    return wrapper


# Написать функцию, которая будет принимать на вход
# натуральное число n, # и возращать сумму его цифр.
# Реализовать используя рекурсию (без циклов, без строк,
# без контейнерных типов данных).
@print_received_argument
def get_natural_sum(number):
    result = 0
    if isinstance(number, int) and number > 0:
        result = (
            number % 10 + get_natural_sum(number // 10) if number > 10 else number
        )
    else:
        print('Give me natural number')

    return result


if __name__ == '__main__':
    assert get_natural_sum(123) == 6
    assert get_natural_sum(123456789) == 45
    assert get_natural_sum(-5) == 0
    assert get_natural_sum('sdf') == 0
    assert get_natural_sum(123.4) == 0
    assert get_natural_sum([1, 2, 3, 4, 5]) == 0
