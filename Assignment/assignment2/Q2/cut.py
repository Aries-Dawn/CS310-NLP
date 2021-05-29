import jieba
import sys

f = open(sys.argv[1])
fw = open('cuted.txt', 'w')
lines = f.readlines()
for line in lines:
    adds = ' '.join(jieba.cut(line, HMM=False))
    fw.write(adds)
fw.close()
f.close()