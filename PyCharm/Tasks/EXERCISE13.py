#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_items(**kwargs):
    for item, price in kwargs.items():
        print(f"{item}: {price}")


if __name__ == '__main__':
    print_items(apple=2, banana=1, orange=1.5, pear=2.5)