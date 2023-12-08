#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, io, sys, random

fn = os.getcwd() + os.sep + 'pinyin.dict'
fn2 = os.getcwd() + os.sep + 'pinyin2.dict'

d = {}

def init():
    with io.open(fn2, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        while line:
            s = line.split('=')
            d[s[0]]=s[1]
            line = f.readline().strip()
    # print(len(d))

def translate():
    dd = {}
    with io.open(fn, 'r', encoding='utf-8') as f:
        line = f.readline()
        s = line.split(',')
        for i in s:
            dd[i[0]]=i[1:]
    with io.open(fn2, 'w', encoding='utf-8') as f:
        for k, v in dd.items():
            f.write(('%s=%s' % (k, v)) + '\n')

def process(inputfile, shuffle = False):
    s = []
    with io.open(inputfile, 'r', encoding='utf-8') as f:
        l = f.readline()
        while l:
            ss = []
            l = l.strip()
            if l in d:
                s.append(d.get(l).split(' '))
            else:
                for ll in l:
                    ss.append(d.get(ll, ll))
                s.append(ss)
            l = f.readline()
    if shuffle:
        random.shuffle(s)
    return s

def gen(title, s, output):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('song', 'ZiTiGuanJiaKaiTi-1.ttf'))
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    width, height = A4
    from reportlab.lib.units import mm
    c = Canvas(output + '.pdf', initialFontName='song', bottomup=0)
    top = 20 * mm
    page = 1
    # title
    c.setFontSize(20)
    c.drawString(width / 2 - 15 * mm, top, '%s %d' % (outputname, page))
    # content
    c.setFontSize(14)
    i = 0
    word_step = 15 * mm
    character_step = 18 * mm
    line_step = 25 * mm
    margin_top = 30 * mm
    margin_left = 15 * mm
    padding = 2 * mm
    x = margin_left
    y = margin_top
    count = 0
    while i < len(s):
        if x + len(s[i]) * character_step > width - margin_left:
            y = y + line_step
            x = margin_left
            if y > height - margin_top or count > 45:
                y = margin_top
                c.showPage()
                page = page + 1
                # title
                c.setFontSize(20)
                c.drawString(width / 2 - 15 * mm, top, '%s %d' % (outputname, page))
                c.setFontSize(14)
                count = 0
        j = 0
        while j < len(s[i]):
            k = s[i][j]
            count = count + 1
            c.drawString(x + padding, y, k)
            c.rect(x, y + padding, character_step, character_step)
            # print(k, x / mm)
            x = x + character_step
            j = j + 1
        if j > 0:
            x = x + character_step
        # x = x + word_step
        i = i + 1
    c.save()

if __name__ == '__main__':
    inputname = sys.argv[1]
    outputname = sys.argv[2]

    # translate()
    init()
    s = process(inputname, False)
    print("There are", len(s), 'words.')
    gen(outputname, s, outputname)

