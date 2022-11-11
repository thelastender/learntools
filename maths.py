#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def list_equation1(count):
    for i in range(count):
        n1 = 90
        n2 = 110
        n = random.randint(0, 2) * 100
        n1 += n
        n2 += n
        t1 = random.randint(n1, n2)
        b = random.random() < 0.5
        if b:
            t2 = random.randint(n1, n2)
            t3 = random.randint(n1, n2)
            d = [' + ', ' - ']
        else:
            t2 = random.randint(n1, t1)
            t3 = random.randint(n1, n2)
            d = [' - ', ' + ']
        s = "" + str(t1) + d[0] + str(t2) + d[1] + str(t3) + ""
        print(s)


def list_equation2(count):
    c = {
        "书": ["本", "童话书", "历史书", "小说"],
        "笔": ["支", "铅笔", "钢笔", "毛笔"],
        "动物": ["只", "猫", "狗", "猪"],
        "玩具": ["个", "小棒", "皮球", "珠子"],
    }
    n1 = 10
    n2 = 499
    for i in range(count):
        key = random.choice(list(c.keys()))
        value = c[key]
        t1 = random.randint(n1, n2)
        b = random.random() < 0.5
        s = "" + str(i + 1) + ". 小明有很多" + value[0] + key + "，"
        s += "" + value[1] + "有" + str(t1) + value[0] + "，"
        if b:
            t2 = random.randint(n1, n2)
            t3 = random.randint(n1, t2)
            d = ["多", "少"]
        else:
            t2 = random.randint(n1, t1)
            t3 = random.randint(n1, n2)
            d = ["少", "多"]
        s += "" + value[2] + "比" + value[1] + d[0] + str(t2) + value[0] + "，"
        s += "" + value[3] + "比" + value[2] + d[1] + str(t3) + value[0] + "，"
        s += "" + value[3] + "有多少" + value[0] + "？请列算式（                       ）"

        print(s)


def list_equation3(count):
     n1 = 10
     n2 = 600
     for i in range(count):
        t1 = random.randint(n1, n2)
        if random.random() < 0.5:
            b2 = ''
            b4 = ''
            p = False
        else:
            b2 = '('
            b4 = ')'
            p = True
        if random.random() < 0.5:
            b1 = ' + '
            t2 = random.randint(n1, n2)
            if random.random() < 0.5:
                b3 = ' + '
                t3 = random.randint(n1, n2)
            else:
                b3 = ' - '
                if p:
                    t3 = random.randint(n1, t2 - 1)
                else:
                    t3 = random.randint(n1, n2)
        else:
            b1 = ' - '
            if random.random() < 0.5:
                b3 = ' + '
                if p:
                    t2 = random.randint(n1, n2)
                    t3 = random.randint(n1, n2)
                    t1 = random.randint(max(t2 + t3, n1), max(t2 + t3 + random.randint(0, n1), n2))
                else:
                    t2 = random.randint(n1, t1) 
                    t3 = random.randint(n1, n2)
            else:
                b3 = ' - '
                if p:
                    t2 = random.randint(n1, n2)
                    t3 = random.randint(max(t2 - t1, n1), t2)
                else:
                    t2 = random.randint(n1, n2)
                    t3 = random.randint(n1, n2)
                    t1 = random.randint(max(t2 + t3, n1), max(t2 + t3 + random.randint(0, n1), n2))
        s = "" + str(i + 1) + ". 计算 " + str(t1) + b1 + b2 + str(t2) + b3 + str(t3) + b4 + " 时，"
        s += "第一步计算的结果是（      ），最后的结果是（      ）"
        print(s)


def list_equation4(count):
    n1 = 10
    n2 = 600
    for i in range(count):
        t1 = random.randint(n1, n2)
        if random.random() < 0.5:
            b1 = "妈妈又给了他"
            t2 = random.randint(n1, n2)
            if random.random() < 0.5:
                b2 = "妈妈又给了他"
                t3 = random.randint(n1, n2)
            else:
                b2 = "花了"
                t3 = random.randint(n1, t1 + t2)
        else:
            b1 = "花了"
            t2 = random.randint(n1, t1)
            if random.random() < 0.5:
                b2 = "妈妈又给了他"
                t3 = random.randint(n1, n2)
            else:
                b2 = "花了"
                t3 = random.randint(min(t1 - t2, n1), t1 - t2)
        b3 = random.choice(("小明还剩的钱是", "小明花了的钱数是", "小明比一开始少的钱数是", "妈妈一共给了小明的钱是"))

        s = "" + str(i + 1) + ". 小明拿" + str(t1) + "元去买水果，"
        s += "第一次" + b1 + str(t2) + "元，" + "第二次" + b2 + str(t3) + "元，"
        s += b3 + " （        ）"
        print(s)

def list_equation5(count):
    n1 = 10
    n2 = 999
    for i in range(count):
        t1 = random.randint(n1, n2)
        if random.random() < 0.5:
            b1 = "和"
            t2 = random.randint(n1, n2)
            if random.random() < 0.5:
                b2 = "多"
                t3 = random.randint(n1, t1 + t2)
            else:
                b2 = "少"
                t3 = random.randint(t1 + t2, t1 + t2 + n2)
        else:
            b1 = "差"
            if random.random() < 0.5:
                b2 = "多"
                t2 = random.randint(n1, n2)
                t3 = random.randint(n1, n2)
                t1 = random.randint(t2 + t3, t2 + t3 + n2)
            else:
                b2 = "少"
                t2 = random.randint(n1, t1)
                t3 = random.randint(t1 - t2, t1 - t2 + n2)
        s = "" + str(i + 1) + ". 有两个数" + str(t1) + "和" + str(t2) + "，"
        s += "它们的" + b1 + "比" + str(t3) + b2 + "（         ）"
        print(s)

def list_equation6(count):
    n1 = 10
    n2 = 999
    n3 = 100
    for i in range(count):
        t1 = random.randint(n1, n2)
        t2 = random.randint(n1, t1)
        if random.random() < 0.5:
            t3 = random.randint(n1, t2 - 1)
            t4 = t2 - t3
        else:
            t3 = int(t2 / n3) * n3 + n3
            t4 = t3 - t2
        if random.random() < 0.5:
            b = ' + '
        else:
            b = ' - '
        if random.random() < 0.5:
            b1 = '('
            b2 = ')'
        else:
            b1 = ''
            b2 = ''
        s = "" + str(i + 1) + ". 算式" + str(t1) + ' - ' + str(t2) + "可以写成"
        s += "" + str(t1) + ' - ' + b1 + str(t3) + b + str(t4) + b2
        s += "吗？（能，不能），如果不能，那么正确的写法是？\r\n"
        print(s)

def list_equation7(count):
    c = {
        "学校组织同学们坐车去春游": ["上去", "人", "车上一共可以容纳", "同学们能坐下吗"],
        "小明往书包里面装书": ["装了", "本", "书包一共可以容纳", "小明能装下吗"],
        "妈妈去买菜": ["买了", "元", "妈妈一共有", "妈妈的钱够吗"],
        "小红切绳子": ["切了", "米", "绳子一共长", "绳子够切吗"]
    }
    n1 = 10
    n2 = 999
    for i in range(count):
        t1 = random.randint(n1, n2)
        t2 = random.randint(n1, n2)
        t3 = random.randint(n1, n2)
        t4 = random.randint(t1, t1 + t2 + t3 + t1)
        key = random.choice(list(c.keys()))
        value = c[key]
        s = "" + str(i + 1) + ". " + key + "，"
        s += "第一次" + value[0] + str(t1) + value[1] + "，"
        s += "第二次" + value[0] + str(t2) + value[1] + "，"
        s += "第三次" + value[0] + str(t3) + value[1] + "，"
        s += "" + value[2] + str(t4) + value[1] + "，"
        s += "" + value[3] + "？"
        print(s)


if __name__ == "__main__":
    print("第三单元练习")
    print("一、用凑整百的方法计算")
    list_equation1(15)
    print("二、列算式")
    list_equation2(10)
    print("三、填空")
    list_equation3(10)
    print("四、填空")
    list_equation4(10)
    print("五、填空")
    list_equation5(10)
    print("六、填空")
    list_equation6(10)
    print("七、应用题")
    list_equation7(10)
    