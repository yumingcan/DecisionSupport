import random
coin = ['正', '反']
line_list = []
gram_list = []
for i in range(6):
    line = random.choices(coin, k=3)
    test = line.count('反')
    if test == 1:
        line_list.append('少阳')
        gram_list.append('阳')
    if test == 2:
        line_list.append('少阴')
        gram_list.append('阴')
    if test == 3:
        line_list.append('老阳')
        gram_list.append('阳')
    if test == 0:
        line_list.append('老阴')
        gram_list.append('阴')
line = line_list[: : -1]
print(line)
gram = gram_list[: : -1]
# print(gram_result)
trigram = [gram[3:6],  gram[0:3]]
Index = []
for j in range(2):
    gtest = trigram[j]
    if gtest == ['阳', '阳', '阳']:
        gIndex = 1
    if gtest == ['阴', '阳', '阳']:
        gIndex = 2
    if gtest == ['阳', '阴', '阳']:
        gIndex = 3
    if gtest == ['阴', '阴', '阳']:
        gIndex = 4
    if gtest == ['阳', '阳', '阴']:
        gIndex = 5
    if gtest == ['阴', '阳', '阴']:
        gIndex = 6
    if gtest == ['阳', '阴', '阴']:
        gIndex = 7
    if gtest == ['阴', '阴', '阴']:
        gIndex = 8
    Index.append(gIndex)
print(Index)
hexagrams = ['乾','夬','大有','大壮','小畜','需','大畜','泰', '履','兑','睽','归妹','中孚','节','损','临','同人','革','离','丰','家人','既济','贲','明夷','无妄','随','噬嗑','震','益','屯','颐','复',
'姤','大过','鼎','恒','巽','井','蛊','升','讼','困','未济','解','涣','坎','蒙','师','遁','咸','旅','小过','渐','蹇','艮','谦','否','萃','晋','豫','观','比','剥','坤']
# print(hexagrams)
print(hexagrams[(Index[0]-1)*8 + Index[1]-1])