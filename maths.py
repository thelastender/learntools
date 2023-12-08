#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# axa + 2b = ?
def calc(a, b):
    return a * a + 2 * b

if __name__ == '__main__':
    import sys
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print("Result is:", calc(a, b))
