#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime
import sys
from functools import reduce

def operator_priority(op1, op2):
    if op1 in ('+', '-'):
        if op2 in ('+', '-'):
            return 0
        else:
            return -1
    else:
        if op2 in ('+', '-'):
            return 1
        else:
            return 0

def is_prime(n):
    """ 判断是否是素数
    """
    if n == 1:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def resolve(x):
    """ 质因式分解
    """
    if x <= 1:
        return [1]
    result = []
    while x > 1:
        if is_prime(x):
            result.append(x)
            if len(result) == 1:
                result.append(1)
            break
        i = 2
        while i * i <= x:
            if x % i == 0 and is_prime(i):
                result.append(int(i))
                x = int(x / i)
                break
            i = i + 1
    return result

def resolve_two(r, min_num, max_num, op = '+'):
    t1 = 0
    t2 = 0
    if op == '-':
        t1 = random.randint(r + 1, max(max_num, r + 1))
        t2 = t1 - r
    elif op == 'x':
        ps = resolve(r)
        ps1 = ps[0:int(len(ps) / 2)]
        ps2 = ps[int(len(ps) / 2):]
        if len(ps) > 2:
            t1 = reduce(lambda x, y: x * y, ps1)
            t2 = reduce(lambda x, y: x * y, ps2)
        else:
            t1 = ps[0]
            t2 = ps[1]
    elif op == '÷':
        t2 = random.randint(max(1, min_num), min(9, max_num))
        t1 = t2 * r
    else:
        t1 = random.randint(1, min(r - 1, max_num))
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
        t1, t2, _, op = resolve_two(r, min_num, max_num, op)
        # print(t1, op, t2, r)
        i = i - 1
        if len(s) > pos:
            del s[pos]
        s.insert(pos, op)
        s.insert(pos, t2)
        s.insert(pos, t1)
        if i >= 2:
            if random.random() < 0.5:
                pos = pos
                r = t1
            else:
                pos = pos + 1
                r = t2
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
    return l + " = " + str(rr)

def plus():
    t1, t2, r, _ = resolve_two(random.randint(11, 999), 11, 999, '+')
    return t1, t2, r, 0

def minus():
    t1, t2, r, _ = resolve_two(random.randint(11, 999), 11, 999, '-')
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

def divide():
    t1, t2, r, _ = multiple()
    return r, t2, t1, 0

# functions 

def split1():
    # 2022年11月20日不需要
    t1, t2, r, tt1 = multiple()
    s = ["写出下面计算方法的乘法算式：(              )"]
    l = "    " + str(tt1 * 10) + " x " + str(t2) + " = " + str(tt1 * 10 * t2) + ""
    l += "    " + str(t1 - tt1 * 10) + " x " + str(t2) + " = " + str((t1 - tt1 * 10) * t2) + ""
    l += "    " + str(tt1 * 10 * t2) + " + " + str((t1 - tt1 * 10) * t2) + " = " + str(r)
    s.append(l)
    return s

def split2():
    t1, t2, r, tt1 = multiple()
    tt2 = t1 - tt1 * 10
    if random.random() < 0.5:
        s = ["计算" + str(t1) + " x " + str(t2) + "时，下面算法正确的是（       ）。"]
        p = []
        p.append(str(tt1) + " x " + str(t2) + " + " + str(tt2) + " x " + str(t2))
        p.append(str(tt1 * 10) + " x " + str(t2) + " + " + str(tt2) + " x " + str(t2))
        p.append(str(tt1 * 10) + " + " + str(tt2) + " x " + str(t2))
        random.shuffle(p)
        prefix = ['A', 'B', 'C']
        l = ""
        for i in range(len(p)):
            l += "    " + prefix[i] + ". " + p[i] + ""
        s.append(l)
    else:
        s = ["计算" + str(t1) + " x " + str(t2) + "时，下面算法错误的是（       ）。"]
        p = []
        p.append(str(tt1) + " x " + str(t2) + " + " + str(tt2) + " x " + str(t2))
        p.append(str(tt1 * 10) + " x " + str(t2) + " + " + str(tt2) + " x " + str(t2))
        p.append(str(t1) + " x " + str(t2))
        random.shuffle(p)
        prefix = ['A', 'B', 'C']
        l = ""
        for i in range(len(p)):
            l += "    " + prefix[i] + ". " + p[i] + ""
        s.append(l)
    return s

def compare():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    x1, y1, _, _ = f1()
    if f[f1] == 'x':
        x2 = x1 - 1
        y2 = y1 + 1
        f2 = multiple
    elif f[f1] == '÷':
        x2 = x1 + y1
        y2 = y1 + 1
        f2 = divide
    elif f[f1] == '+':
        x2, y2, _, _ = resolve_two(x1 + y1, 1, 999)
        x2 = max(1, x2 + random.randint(-5, 5))
        y2 = max(1, y2 + random.randint(-5, 5))
        f2 = plus
    else:
        x2, y2, _, _ = resolve_two(x1 - y1, 1, 999, '-')
        x2 = max(x2 + random.randint(-5, 5), 1)
        y2 = max(y2 + random.randint(-5, 5), 1)
        f2 = minus
    return ["比大小：" + str(x1) + " " + f[f1] + " " + str(y1) + " [ ] " + str(x2) + " " + f[f2] + " " + str(y2)]

def zeros():
    _, t2, _, tt1 = multiple()
    t2 = random.choice([2, 4, 6, 8])
    tt1 = random.randint(1, 9)
    return [str(tt1 * 100 + 5 * 10) + " x " + str(t2) + "的积的末尾有(      )个0"]

def mdpm():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    t1, t2, r, _ = f1()
    if random.random() < 0.5:
        t1 = "(     )"
    else:
        t2 = "(     )"
    return ["填空：" + str(t1) + " " + f[f1] + " " + str(t2) + " = " + str(r)]

def m2():
    t1, t2, r, tt1 = multiple()
    tt2 = t1 - tt1 * 10
    p = []
    if random.random() < 0.5:
        s = ["[ ]" + str(tt2) + " x " + str(t2) + "的积是" + str(r) + "，[ ]中填(     )是正确的"]
        p.append(str(tt1))
        p.append(str(tt1 - 1 if tt1 - 1 >= 0 else tt1 + 2))
        p.append(str(tt1 + 1))
    else:
        rrr = int(r / 10)
        if rrr > 0:
            s = ["" + str(int(r / 10)) + "[ ] ÷ " + str(t2) + "的商是" + str(t1) + "，[ ]中填的(      )是正确的"]
        else:
            s = ["" + "[ ] ÷ " + str(t2) + "的商是" + str(t1) + "，[ ]中填的(      )是正确的"]
        rr = r - rrr * 10
        p.append(str(rr))
        p.append(str(rr - 1 if rr - 1 >= 0 else rr + 2))
        p.append(str(rr + 1))
    prefix = ['A', 'B', 'C']
    random.shuffle(p)
    ss = ""
    for i in range(len(prefix)):
        ss += "    " + prefix[i] + ". " + p[i]
    s.append(ss)
    return s

def eq1():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    t1, t2, r, _ = f1()

    k = random.randint(1, 3)
    s = ""
    if random.random() < 0.5:
        #print("t1", t1, t2, r)
        x, y, _, op = resolve_two(t1, 1, 999, random.choice(('+', '-', 'x', '÷')))
        l = [x, y, t2]
        o = [" " + op + " ", " " + f[f1] + " ", " = " + str(r)]
        for i in range(len(l)):
            if i == 0 and operator_priority(op, f[f1]) < 0:
                s += "("
            if i + 1 == k:
                s += "(      )"
            else:
                s += str(l[i])
            if i == 1 and operator_priority(op, f[f1]) < 0:
                s += ")"
            s += o[i]
    else:
        #print("t2", t1, t2, r)
        x, y, _, op = resolve_two(t2, 1, 999, random.choice(('+', '-', 'x', '÷')))
        l = [t1, x, y]
        o = [" " + f[f1] + " ", " " + op + " ", " = " + str(r)]
        for i in range(len(l)):
            if i == 1 and operator_priority(f[f1], op) > 0:
                s += "("
            if i + 1 == k:
                s += "(      )"
            else:
                s += str(l[i])
            if i == 2 and operator_priority(f[f1], op) > 0:
                s += ")"
            s += o[i]
    return ["填空：" + s]

def eq2():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    t1, t2, r, _ = f1()
    x, y, _, op = resolve_two(t1, 1, 999, random.choice(('+', '-', 'x', '÷')))
    s = ["下面哪个算式的得数是" + str(r) + "，请选择(      )"]
    l = "    A. " + str(x) + " " + op + " " + str(y) + " " + f[f1] + " " + str(t2) + "    " 
    opposite = {'+': '-', '-': '+', 'x': '+', '÷': '-'}
    if f[f1] == '+' or f[f1] == '-':
        if op == '-':
            l += "B. " + str(x) + " " + op + " (" + str(y) + " " + f[f1] + " " + str(t2) + ")" + "    " 
        else:
            l += "B. " + str(x) + " " + opposite[op] + " (" + str(y) + " " + f[f1] + " " + str(t2) + ")" + "    " 
        l += "C. " + str(x) + " " + op + " " + str(y) + " " + opposite[f[f1]] + " " + str(t2)
    else:
        if op == 'x' or op == '÷':
            l += "B. " + str(x) + " " + opposite[op] + " " + str(y) + " " + f[f1] + " " + str(t2) + "" + "    " 
        else: 
            l += "B. (" + str(x) + " " + op + " " + str(y) + ") " + f[f1] + " " + str(t2) + "    " 
        l += "C. " + str(x) + " " + op + " " + str(y) + " " + opposite[f[f1]] + " " + str(t2)
    s.append(l)
    return s

def times():
    pass

def export(fname, t = None):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('song', 'WenQuanDengKuanWeiMiHei.ttf'))
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    width, height = A4 # A4纸大小
    from reportlab.lib.units import mm
    c = Canvas(fname + '.pdf', initialFontName='song', bottomup=0)
    font_factor = 0.35146
    title_font_size = 20
    content_font_size = 12
    footer_font_size = 10
    top = 15 * mm # 上边距20mm
    character_step = font_factor * content_font_size * mm
    margin_top = 25 * mm
    margin_left = 15 * mm
    padding = 1 * mm
    line_padding = 3 * mm
    # title
    c.setFontSize(20)
    title = "Calculate " + '%s' % (datetime.datetime.now().strftime('%Y-%m-%d') if not t else t)
    c.drawString(width / 2 - len(title) * character_step / 2, top, title)
    # content
    c.setFontSize(content_font_size)
    f = [eq1, eq1, eq1, eq1, eq1, eq1, mdpm, eq1, mdpm, eq1] * 2
    random.shuffle(f)
    i = 1
    j = 1
    y = margin_top
    for f1 in f:
        s = f1()
        s[0] = str(i) + ". " + s[0]
        for ss in s:
            c.drawString(margin_left, y, '%s' % ss)
            y = y + (character_step + padding)
            j = j + 1
        # c.showPage()
        i = i + 1
        y = y + line_padding
    c.save()

if __name__ == "__main__":
    t = None
    if len(sys.argv) > 1:
        t = sys.argv[1]
    fname = 'calculate-' + (datetime.datetime.now().strftime('%Y-%m-%d') if not t else t)
    export(fname, t)
    