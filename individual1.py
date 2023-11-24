#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    first_word = input("Enter the first word: ")
    second_word = input("Enter the second word: ")
    replaced_word2 = second_word[:len(second_word)] + first_word[len(second_word):]

    print("Result:", replaced_word2)
