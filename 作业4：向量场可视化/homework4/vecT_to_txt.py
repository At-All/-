# 1.读入向量场（jet.vecT）。计算该向量场的模，存到文本文件(jetMag.txt)。
import math

f = open('jet.vecT')
fw = open('jetMag.txt', 'w')
a = f.readline().replace('\n', '').split(' ')
h = int(a[0])   #行数
w = int(a[1])   #列数
print(h,w)

for line in f:
    n = line.replace('\n', '').split(' ')
    for i in range(w):
        x = float(n[i*2])
        y = float(n[i*2+1])
        fw.write(str(math.sqrt(x*x+y*y))+' ')
    fw.write('\n')
