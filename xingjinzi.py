#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, io, sys


def init():
    pass

def process(inputfile):
    d = []
    with io.open(inputfile, 'r', encoding='utf-8') as f:
        l = f.readline().strip()
        while l:
            s = []
            for c in l:
                s.append(c)
            d.append(s)
            l = f.readline().strip()
    return d

def gen(title, d, output):
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
    character_step = font_factor * content_font_size * mm
    pinyin_step = 10 * mm
    word_height = 10 * mm
    line_padding = 5 * mm
    margin_top = 30 * mm
    margin_left = 15 * mm
    padding = 4 * mm
    x = margin_left
    y = margin_top
    line_step = 0 # 上一行高度
    page = 1
    # title
    c.setFontSize(20)
    c.drawString(width / 2 - len(outputname) * character_step / 2, top, '%s' % outputname)
    # content
    i = 0
    c.setFontSize(content_font_size)
    for k in d:
        w = character_step + padding + (5 * character_step) # 一组字词宽度
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
        h = word_height * len(k)
        line_step = max(line_step, h)
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
        for word in k:
            c.drawString(x + character_step + padding, y + j * word_height, word)
            c.drawString(x + character_step + padding + character_step, y + j * word_height, '（')
            c.drawString(x + character_step + padding + character_step + 4 * character_step, y + j * word_height, '）')
            j = j + 1
        x = x + w
        i = i + 1
    # footer
    c.setFontSize(footer_font_size)
    c.drawString(width / 2 - len(str(page)) * character_step / 2, height - top / 2, '%d' % page)
    c.save()

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        inputname = sys.argv[1]
        outputname = sys.argv[2]

        init()
        d = process(inputname)
        gen(outputname, d, outputname)
