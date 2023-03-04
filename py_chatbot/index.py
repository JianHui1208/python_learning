import os
import os.path
from asyncio.windows_events import NULL
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.trainers import ChatterBotCorpusTrainer

file_exists = os.path.exists('database.sqlite3')
if(file_exists):
    os.remove('database.sqlite3')

bot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    response_selection_method=get_first_response,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'
    ]
)

# talking bot with corpus data
define_languages = input('Chinese = 1, English = 2. Language: ')
trainer = ChatterBotCorpusTrainer(bot)
# fileName = 'history'

if define_languages == '1':
    trainer.train(
        # "chatterbot.corpus.custom." + fileName,
        "chatterbot.corpus.chinese.greetings",
        "chatterbot.corpus.chinese.conversations",
        "chatterbot.corpus.chinese.ai"
    )

else: 
    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
        "chatterbot.corpus.english.ai"
    )

# Training yourself bot
# trainer = ListTrainer(bot)

# trainer.train([
#     "Hi, can I help you",
#     "Who are you?",
#     "I am your virtual assistant. Ask me any questions...",
#     "Where do you operate?",
#     "We operate from Singapore",
#     "What payment methods do you accept?",
#     "We accept debit cards and major credit cards",
#     "I would like to speak to your customer service agent",
#     "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
# ])
# trainer.train([
#     "What payment methods do you offer?",
#     "We accept debit cards and major credit cards",
#     "How to contact customer service agent",
#     "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
# ])

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request == 'Bye' or request == 'bye':
        print('Bot: Bye')
        break
    elif request == NULL or request == '':
        print('Bot: Pls Type Somethings...')
    else:
        response=bot.get_response(request)
        print('Bot:',response)