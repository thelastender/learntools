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
    font_factor = 0.35146
    title_font_size = 20
    content_font_size = 14
    footer_font_size = 10
    top = 20 * mm # 上边距20mm
    pinyin_step = 10 * mm
    character_step = font_factor * content_font_size * mm
    word_height = 15 * mm
    line_padding = 5 * mm
    margin_top = 30 * mm
    margin_left = 15 * mm
    padding = 4 * mm
    x = margin_left
    y = margin_top
    line_step = 0
    page = 1
    # title
    c.setFontSize(20)
    c.drawString(width / 2 - len(outputname) * character_step / 2, top, '%s' % outputname)
    # content
    i = 0
    c.setFontSize(content_font_size)
    for k, v in s.items():
        w = character_step + padding + pinyin_step + (5 * character_step if not with_result else max(list(map(lambda x: len(x), v.values()))) * character_step + 3 * character_step)
        # 判断是否需要换行
        if x + w > width - margin_left and x > margin_left:
            x = margin_left
            y = y + line_step + line_padding
            line_step = 0
            # 判断是否超过一页
            if y > height - margin_top:
                y = margin_top
                # footer
                c.setFontSize(footer_font_size)
                c.drawString(width / 2 - len(str(page)) * character_step / 2, height - top / 2, '%d' % page)
                c.showPage()
                page = page + 1
                # title
                c.setFontSize(title_font_size)
                c.drawString(width / 2 - len(outputname) * character_step / 2, top, '%s' % outputname)
                c.setFontSize(content_font_size)
        h = word_height * len(v)
        line_step = max(line_step, h)
        c.drawString(x, y + (h - word_height) / 2 , k)
        # c.rect(x, y, w, h)
        # 大括号
        c.line(x + character_step + padding / 4, y + (h - word_height - character_step * 2/3) / 2, 
                    x + character_step + padding * 2 / 4, y + (h - word_height - character_step * 2/3) / 2)
        c.line(x + character_step + padding * 2 / 4, y + (- character_step * 2/3) / 2, 
                    x + character_step + padding * 3 / 4, y + (- character_step * 2/3) / 2)
        c.line(x + character_step + padding * 2 / 4, y + h - word_height - (character_step * 2/3) / 2, 
                    x + character_step + padding * 3 / 4, y + h - word_height - (character_step * 2/3) / 2)
        c.line(x + character_step + padding * 2 / 4, y - (character_step * 2/3) / 2, 
                    x + character_step + padding * 2 / 4, y + h - word_height - (character_step * 2/3) / 2)
        j = 0
        for p, word in v.items():
            c.drawString(x + character_step + padding, y + j * word_height, p)
            if with_result:
                c.drawString(x + character_step + padding + pinyin_step, y + j * word_height, '（%s）' % word)
            else:
                c.drawString(x + character_step + padding + pinyin_step, y + j * word_height, '（')
                c.drawString(x + character_step + padding + pinyin_step + 4 * character_step, y + j * word_height, '）')
            j = j + 1
        x = x + w
        i = i + 1
    # footer
    c.setFontSize(footer_font_size)
    c.drawString(width / 2 - len(str(page)) * character_step / 2, height - top / 2, '%d' % page)
    c.save()

if __name__ == '__main__':
    inputname = sys.argv[1]
    outputname = sys.argv[2]
    with_result = False
    if len(sys.argv) > 3:
        with_result = bool(int(sys.argv[3]))

    init()
    s = process(inputname)
    gen(outputname, s, outputname, with_result)
