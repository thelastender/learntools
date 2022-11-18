#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def calculate(r, min_num, max_num, op = '+'):
    t1 = 0
    t2 = 0
    if op == '-':
        t1 = random.randint(min(r - 1, max_num), max_num)
        t2 = t1 - r
    else:
        t1 = random.randint(min_num, max(r - 1, min_num))
        t2 = r - t1
    return t1, t2, r, op

def equation(min_num, max_num, parameter_count):
    rr = random.randint(min_num, max_num)
    i = parameter_count
    r = rr
    s = [] #stack
    pos = 0
    replaced = False
    while i >= 2:
        op = '+' if random.random() < 0.5 else '-'
        t1, t2, _, op = calculate(r, min_num, max_num, op)
        i = i - 1
        if len(s) > pos:
            del s[pos]
        s.insert(pos, op)
        s.insert(pos, t2)
        s.insert(pos, t1)
        if i >= 2:
            if t1 > t2:
                pos = pos
            else:
                pos = pos + 1
    stack = []
    k = random.randint(1, parameter_count)
    j = 1
    for x in s:
        #print(x, stack)
        if x == '+' or x == '-':
            x2 = stack.pop()
            x1 = stack.pop()
            if len(stack) > 0:
                stack.append("(" + str(x1) + " " + x + " " + str(x2) + ")")
            else:
                stack.append(str(x1) + " " + x + " " + str(x2))
        else:
            if k == j:
                stack.append("(     )")
            else:
                stack.append(x)
            j = j + 1
    l = stack.pop()
    return l + " = " + str(r)

def plus():
    t1, t2, r, _ = calculate(random.randint(11, 999), 11, 999, '+')
    return t1, t2, r, 0

def minus():
    t1, t2, r, _ = calculate(random.randint(11, 999), 11, 999, '-')
    return t1, t2, r, 0

def multiple():
    max_num = 99
    t1 = random.randint(11, max_num)
    while t1 % 10 == 0:
        t1 = random.randint(1, max_num)
    t2 = random.randint(2, 9)
    tt1 = int(t1 / 10)
    # tt2 = t1 - tt1 * 10
    return t1, t2, int(t1 * t2), tt1

def split1():
    t1, t2, r, tt1 = multiple()
    s = "写出下面计算方法的乘法算式：(              )" + "\r\n"
    s += "    " + str(tt1 * 10) + " x " + str(t2) + " = " + str(tt1 * 10 * t2) + ""
    s += "    " + str(t1 - tt1 * 10) + " x " + str(t2) + " = " + str((t1 - tt1 * 10) * t2) + ""
    s += "    " + str(tt1 * 10 * t2) + " + " + str((t1 - tt1 * 10) * t2) + " = " + str(r)
    return s

def split2():
    t1, t2, r, tt1 = multiple()
    tt2 = t1 - tt1 * 10
    s = "计算" + str(t1) + " x " + str(t2) + "时，下面算法正确的是（       ）。" + "\r\n"
    p = []
    p.append(str(tt1) + " x " + str(t2) + " + " + str(tt2) + " x " + str(t2))
    p.append(str(tt1 * 10) + " x " + str(t2) + " + " + str(tt2) + " x " + str(t2))
    p.append(str(tt1 * 10) + " + " + str(tt2) + " x " + str(t2))
    random.shuffle(p)
    prefix = ['A', 'B', 'C']
    for i in range(len(p)):
        s += "    " + prefix[i] + ". " + p[i] + ""
    return s

def divide():
    t1, t2, r, _ = multiple()
    return r, t2, t1, 0

def compare():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    f2 = random.choice(list(f.keys()))
    x1, y1, _, _ = f1()
    x2, y2, _, _ = f2()

    return "比大小：" + str(x1) + " " + f[f1] + " " + str(y1) + " [ ] " + str(x2) + " " + f[f2] + " " + str(y2)

def zeros():
    _, t2, _, tt1 = multiple()
    return str(tt1 * 10) + " x " + str(t2) + "的积的末尾有(      )个0"

def mdpm():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    t1, t2, r, _ = f1()
    if random.random() < 0.5:
        t1 = "(     )"
    else:
        t2 = "(     )"
    return "填空：" + str(t1) + " " + f[f1] + " " + str(t2) + " = " + str(r)

def m2():
    t1, t2, r, tt1 = multiple()
    tt2 = t1 - tt1 * 10
    o = '小' if random.random() < 0.5 else '大'
    s = "[ ]" + str(tt2) + " x " + str(t2) + "的积是" + str(r) + "，[ ]中填(     )是正确的" + "\r\n"
    s += "    A. " + str(tt1) + "  B. " + str(tt1 - 1) + "  C. " + str(tt1 + 1)
    return s

def eq1():
    return "填空：" + equation(11, 999, 3)

def eq2():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    t1, t2, r, _ = f1()
    x, y, _, op = calculate(t1, 1, 999, '+' if random.random() < 0.5 else '-')
    s = "下面哪个算式的得数是" + str(r) + "，请选择(      )" + "\r\n"
    s += "    A. " + str(x) + " " + op + " " + str(y) + " " + f[f1] + " " + str(t2) + "    " 
    opposite = {'+': '-', '-': '+', 'x': '+', '÷': '-'}
    if f[f1] == '+' or f[f1] == '-':
        s += "B. " + str(x) + " " + op + " (" + str(y) + " " + f[f1] + " " + str(t2) + ")" + "    " 
        s += "C. " + str(x) + " " + op + " " + str(y) + " " + opposite[f[f1]] + " " + str(t2)
    else:
        s += "B. (" + str(x) + " " + op + " " + str(y) + ") " + f[f1] + " " + str(t2) + "    " 
        s += "C. " + str(x) + " " + op + " " + str(y) + " " + opposite[f[f1]] + " " + str(t2)
    return s


if __name__ == "__main__":
    f = [split1, split2, eq1, eq2, compare, zeros, mdpm, m2, mdpm, eq2] * 2
    random.shuffle(f)
    i = 1
    for f1 in f:
        print(str(i) + ". " + f1())
        i = i + 1
        print()
