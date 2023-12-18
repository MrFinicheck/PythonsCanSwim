#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_after_last_zero(*args):
    last_zero_index = -1
    for i in range(len(args) - 1, -1, -1):
        if args[i] == 0:
            last_zero_index = i
            break

    # Если нулей нет.
    if last_zero_index == -1:
        return None

    return sum(args[last_zero_index + 1:])


if __name__ == '__main__':
    arguments = list(map(int, input("Введите аргументы: ").split()))
    result = sum_after_last_zero(*arguments)

    print(f"Сумму аргументов, расположенных после последнего аргумента, "
          f"равного нулю"
          f"{result}")

