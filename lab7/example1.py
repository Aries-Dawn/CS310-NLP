#encoding=utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
# bot = ChatBot('test') # You can rename it whatever you want
bot = ChatBot(
    "My ChatterBot",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ]
)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.chinese') # Load conversations
while True:
 text = input('You: ')
 print('Bot: %s' % bot.get_response(text))
