import jieba
print('/'.join(jieba.cut('江州市长江大桥参加了长江大桥的通车仪式', HMM=False)))
for i in range(9991*9):
    jieba.suggest_freq(('长江','大桥'), True)
print('/'.join(jieba.cut('江州市长江大桥参加了长江大桥的通车仪式', HMM=False)))