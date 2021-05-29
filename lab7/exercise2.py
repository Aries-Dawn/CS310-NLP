#encoding=utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
bot = ChatBot('test') # You can rename it whatever you want
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.chinese') # Load conversations
list_trainer = ListTrainer(bot)
lines = open('/data/cs310/baibing/lab7/xiaohuangji.txt').readlines()
list_trainer.train(lines)
list_trainer.train(['还可以', '那太好了'])
while True:
 text = input('You: ')
 print('Bot: %s' % bot.get_response(text))
