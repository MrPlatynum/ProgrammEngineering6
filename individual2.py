#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Введите предложение (без '-'): ")

    sentence = sentence.lstrip()

    first_space_index = sentence.find(' ')
    if first_space_index == -1:
        first_word = sentence
    else:
        first_word = sentence[:first_space_index]
    print(first_word)
    count_o = first_word.lower().count('о')

    print(f"Количество букв 'о' в первом слове: {count_o}")
