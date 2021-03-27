#encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=False) # 默认模式
print("Accurate Mode: " + "/ ".join(seg_list))
seg_list = jieba.cut("我来到北京清华大学", cut_all=True) # 全模式
print("Full Mode: " + "/ ".join(seg_list))
seg_list = jieba.cut_for_search("我来到北京清华大学") # 搜索引擎模式
print("Search Engine Mode: " + "/ ".join(seg_list))
seg_list = jieba.cut("他来到了网易杭研大厦")
print("Unknown Words Recognize: " + ", ".join(seg_list))
