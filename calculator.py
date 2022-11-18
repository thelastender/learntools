#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime
import sys

def calculate(r, min_num, max_num, op = '+'):
    t1 = 0
    t2 = 0
    if op == '-':
        t1 = random.randint(r + 1, max(max_num, r + 1))
        t2 = t1 - r
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
        t1, t2, _, op = calculate(r, min_num, max_num, op)
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

def divide():
    t1, t2, r, _ = multiple()
    return r, t2, t1, 0

# functions 

def split1():
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
    return s

def compare():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    f2 = random.choice(list(f.keys()))
    x1, y1, _, _ = f1()
    x2, y2, _, _ = f2()

    return ["比大小：" + str(x1) + " " + f[f1] + " " + str(y1) + " [ ] " + str(x2) + " " + f[f2] + " " + str(y2)]

def zeros():
    _, t2, _, tt1 = multiple()
    return [str(tt1 * 10) + " x " + str(t2) + "的积的末尾有(      )个0"]

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
    o = '小' if random.random() < 0.5 else '大'
    s = ["[ ]" + str(tt2) + " x " + str(t2) + "的积是" + str(r) + "，[ ]中填(     )是正确的"]
    s.append("    A. " + str(tt1) + "  B. " + str(tt1 - 1) + "  C. " + str(tt1 + 1))
    return s

def eq1():
    return ["填空：" + equation(11, 999, 3)]

def eq2():
    f = {multiple : 'x', divide: '÷', plus : '+', minus : '-'}
    f1 = random.choice(list(f.keys()))
    t1, t2, r, _ = f1()
    x, y, _, op = calculate(t1, 1, 999, '+' if random.random() < 0.5 else '-')
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
        l += "B. (" + str(x) + " " + op + " " + str(y) + ") " + f[f1] + " " + str(t2) + "    " 
        l += "C. " + str(x) + " " + op + " " + str(y) + " " + opposite[f[f1]] + " " + str(t2)
    s.append(l)
    return s


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
    f = [split1, split2, eq1, eq2, compare, zeros, mdpm, m2, mdpm, eq2] * 2
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
