#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, io, sys

fn = os.getcwd() + os.sep + 'duoyinzi.dict'

d = {}

def init():
    with io.open(fn, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        while line:
            s = line.split(':')
            d[s[0]] = dict(zip(s[1].split(' '), s[2].split(' ')))
            line = f.readline().strip()
    # print(len(d))

def process(inputfile):
    s = {}
    with io.open(inputfile, 'r', encoding='utf-8') as f:
        l = f.readline().strip()
        while l:
            s[l] = d.get(l, None)
            l = f.readline().strip()
    return s

def gen(title, s, output, with_result=False):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('song', 'Songti.ttc'))
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    width, height = A4 # A4纸大小
    from reportlab.lib.units import mm
    c = Canvas(output + '.pdf', initialFontName='song', bottomup=0)
    top = 20 * mm # 上边距20mm
    page = 1
    # title
    c.setFontSize(20)
    c.drawString(width / 2 - 15 * mm, top, '%s %d' % (outputname, page))
    # content
    def draw_block():
        pass
    c.setFontSize(14)
    i = 0
    word_step = 15 * mm
    character_step = 15 * mm
    line_step = 25 * mm
    margin_top = 30 * mm
    margin_left = 15 * mm
    padding = 2 * mm
    x = margin_left
    y = margin_top
    while i < len(s):
        if x + len(s[i]) * character_step > width - margin_left:
            y = y + line_step
            x = margin_left
            if y > height - margin_top:
                y = margin_top
                c.showPage()
                page = page + 1
                # title
                c.setFontSize(20)
                c.drawString(width / 2 - 15 * mm, top, '%s %d' % (outputname, page))
                c.setFontSize(14)
        j = 0
        while j < len(s[i]):
            k = s[i][j]
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

    init()
    s = process(inputname)
    print(s)
    gen(outputname, s, outputname)
