#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    # Преобразование слов в нижний регистр для учёта регистра букв
    word1 = word1.lower()
    word2 = word2.lower()

    # Список для хранения ответов (да/нет)
    results = []

    # Перебор букв первого слова
    for letter in word1:
        if letter in word2:
            results.append("да")
        else:
            results.append("нет")

    print(" ".join(results))
