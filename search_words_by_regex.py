#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re


if __name__ == '__main__':
    with open('words_alpha.txt') as word_file:
        words = set(word_file.read().split())
    for word in words:
        if re.match(r'^mel\w+c$', word):
            print(word)
