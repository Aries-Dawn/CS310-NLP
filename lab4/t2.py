import jieba
print('/'.join(jieba.cut('李小福是创新办主任也是云计算方面的专家')))
jieba.add_word('创新办')
jieba.add_word('云计算')
print('/'.join(jieba.cut('李小福是创新办主任也是云计算方面的专家')))
print('/'.join(jieba.cut('如果放到 post 中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True)
print('/'.join(jieba.cut('如果放到 post 中将出错。', HMM=False)))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
jieba.suggest_freq('台中', True)
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))