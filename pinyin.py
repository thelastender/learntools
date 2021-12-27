#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, io, sys

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

def process(inputfile):
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
    return s

def gen(title, s, output):
    from reportlab.platypus import SimpleDocTemplate, Table
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('song', 'Songti.ttc'))
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

    # 调用模板，创建指定名称的PDF文档
    # doc = SimpleDocTemplate(output + '.pdf')
    # 获得模板表格
    # styles = getSampleStyleSheet()
    # 指定模板
    # style = styles['Normal']
    # style.fontName = 'Hei'
    # 初始化内容
    # story =[]

    # 初始化表格内容
    # data= s

    # 根据内容创建表格
    # t = Table(data)
    # 将表格添加到内容中
    # story.append(t)
    # 将内容输出到PDF中
    # doc.build(story)

if __name__ == '__main__':
    inputname = sys.argv[1]
    outputname = sys.argv[2]

    # translate()
    init()
    s = process(inputname)
    print("There are", len(s), 'words.')
    gen(outputname, s, outputname)

    

    