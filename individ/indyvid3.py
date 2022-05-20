#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Задание 3. Вариант 3

if __name__ == '__main__':
    predlog = input("Введите предложение: ")

    print("Введите диапазон для удаления: ")
    n1 = int(input())
    n2 = int(input())

    print(str(predlog[:n1]), str(predlog[n2:]))
