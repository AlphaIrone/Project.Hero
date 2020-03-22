print("欢迎使用摩尔勇士经验计算器")
a = input("如需计算人物经验请输入0，如需计算宠物经验请输入1")
a = int(a)
HighLevelList = ['1080367','1088762','1097386','1106240','1115329','1124654','1134220','1144028','1154083','1164386',
                 '1174942','1185752','1196821','1208150','1219744','1231604','1243735','1256138','1268818','1281776',
                 '1295017','1308542','1322356','1336460','1350859','1365554','1380550','1395848','1411453','1427366',
                 '1443592','1460132','1476991','1494170','1511674']
Section = ['17850625','21420750','25704900','30845879','37015057','44418067','53301681','63962019','76754417','92105299'
           ,'110526369']
if a == 0:
    mode = input("请选择计算类型：0.面板经验值；1.累计经验值")
    mode = int(mode)
    if mode == 0:
        level = input('请输入需要计算的等级')
        level = int(level)
        if level <= 64:
            exp = (level+1) ** 4 - level ** 4
            print("当前等级面板经验值为",exp)
        else:
            exp = HighLevelList[level-65]
            print("当前等级面板经验值为", exp)
    if mode == 1:
        low = input("请输入等级下限")
        high = input("请输入等级上限")
        low = int(low)
        high = int(high)
        lowlock = low
        highlock = high
        exphigh = 0
        explow = 0
        if low >= high:
            print('等级下限不能超过等级上限！')
        else:
            if (low < 65) and (high < 65):
                exp = high ** 4 - low ** 4
                print("从", low, "级升至", high, "级需要", exp, "点经验值")
            elif (low < 65) and (high > 64):
                explow = low ** 4
                while high-65:
                    exphigh += int(HighLevelList[high - 66])
                    high -= 1
                exp = exphigh - explow + 17850625
                print("从",lowlock,"级升至",highlock,"级需要",exp,"点经验值")
            else:
                while high - 65:
                    exphigh += int(HighLevelList[high - 66])
                    high -= 1
                while low - 65:
                    explow += int(HighLevelList[low - 66])
                    low -= 1
                exp = exphigh - explow
                print("从", lowlock, "级升至", highlock, "级需要", exp, "点经验值")
else:
    mode = input("请选择计算类型：0.面板经验值；1.累计经验值")
    tr = input("请输入转生次数")
    tr = int(tr)
    mode = int(mode)
    if mode == 0:
        level = input('请输入需要计算的等级')
        level = int(level)
        if level <= 64:
            exp = (level + 1) ** 4 - level ** 4
            exp = exp * (1.2 ** tr)
            print("当前等级面板经验值为", exp)
        else:
            exp = int(HighLevelList[level - 65])
            exp = int(exp * (1.2 ** tr)+0.5)
            print("当前等级面板经验值为", exp)
    if mode == 1:
        low = input("请输入等级下限")
        high = input("请输入等级上限")
        low = int(low)
        high = int(high)
        lowlock = low
        highlock = high
        exphigh = 0
        explow = 0
        if low >= high:
            print('等级下限不能超过等级上限！')
        else:
            if (low < 65) and (high < 65):
                explow = int(low ** 4 * (1.2 ** tr)+0.5)
                exphigh = int(high ** 4 * (1.2 ** tr)+0.5)
                exp = exphigh - explow
                print("从", low, "级升至", high, "级需要", exp, "点经验值")
            elif (low < 65) and (high > 64):
                explow = int(low ** 4 * (1.2 ** tr) + 0.5)
                while high - 65:
                    exphigh += int(int(HighLevelList[high - 66]) * (1.2 ** tr)+0.5)
                    high -= 1
                exp = exphigh - explow + int(Section[tr])
                print("从", lowlock, "级升至", highlock, "级需要", exp, "点经验值")
            else:
                while high - 65:
                    exphigh += int(int(HighLevelList[high - 66]) * (1.2 ** tr)+0.5)
                    high -= 1
                while low - 65:
                    explow += int(int(HighLevelList[low - 66]) * (1.2 ** tr)+0.5)
                    low -= 1
                exp = exphigh - explow
                print("从", lowlock, "级升至", highlock, "级需要", exp, "点经验值")