python cut.py $1 2> err.log
ngram-count -text cuted.txt -order 2 -write train2gram.count 2> err2.log
ngram-count -read train2gram.count -order 2 -lm bigram.lm 2> err3.log
python greedy.py