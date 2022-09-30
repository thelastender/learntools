#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font

def process_file(file_name, sheet_name):
    wb1 = load_workbook(file_name)
    ws1 = wb1[sheet_name]
    wb2 = Workbook()
    wb2.remove(wb2.active)
    i = 0
    last_unit = 0
    for row in ws1.iter_rows(min_row=2, min_col=1, max_col=6):
        word = row[0].value
        unit = row[1].value
        defination = row[3].value
        pos = row[4].value
        example = row[5].value
        if unit != last_unit:
            r = ['NO', "WORD", "PoS", "DEFINITION & EXAMPLE", "UNIT"]
            ws2 = wb2.create_sheet("UNIT %s" % unit)
            ws2.append(r)
            # change style
            col = ws2.column_dimensions['D']
            col.alignment = Alignment(vertical="top", wrapText=True)
            col.width = 80
            col = ws2.column_dimensions['B']
            col.alignment = Alignment(horizontal="center", vertical="top", wrapText=True)
            col.width = 20
            col = ws2.column_dimensions['A']
            col.alignment = Alignment(vertical="top", wrapText=True)
            col.width = 5
            col = ws2.column_dimensions['E']
            col.alignment = Alignment(vertical="top", wrapText=True)
            col.width = 5
            col = ws2.column_dimensions['C']
            col.alignment = Alignment(vertical="top", wrapText=True)
            col.width = 10
            last_unit = unit
            i = 1
        r = [i, word, pos, "%s\r%s" % (defination, example), unit]
        ws2.append(r)
        i = i + 1
    wb2.save("think 1.xlsx")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Need file name", file=sys.stderr)
        sys.exit(1)
    sheet_name = 'THINK L1 FRENCH' if len(sys.argv) <= 2 else sys.argv[2]
    process_file(sys.argv[1], sheet_name)
