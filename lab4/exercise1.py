import jieba

print('/'.join(jieba.cut('江州市长江大桥参加了长江大桥的通车仪式', HMM=False)))
jieba.add_word('江大桥',20000)
print('/'.join(jieba.cut('江州市长江大桥参加了长江大桥的通车仪式', HMM=False)))

print()

print('/'.join(jieba.cut('我們在野生動物園玩', HMM=False)))
jieba.add_word('我們')
jieba.add_word('野生動物園')
print('/'.join(jieba.cut('我們在野生動物園玩', HMM=False)))


print('/'.join(jieba.cut('ETF 新兵登场元大宝来推 ETF 伞型证券投资信托基金', HMM=False)))
jieba.add_word('元大宝来')
print('/'.join(jieba.cut('ETF 新兵登场元大宝来推 ETF 伞型证券投资信托基金', HMM=False)))