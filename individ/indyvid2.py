#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Задание 2.Вариаент 3

if __name__ == '__main__':
    predlog = input("Введите предложение: ")
    kol = 0

    for i in range(len(predlog)):
        if predlog[i] == 'и':
            kol = kol + 1
        i = i + 1

    print("Букв 'и' в предложении: ", kol)
