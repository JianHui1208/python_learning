#imports
import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
app = Flask(__name__, template_folder='template', static_folder='static')

os.remove("db.sqlite3")

#创建chatbot 叫做catBot
catBot = ChatBot("Camilla", storage_adapter="chatterbot.storage.SQLStorageAdapter")

bots = [catBot]
for c in bots :
    # Chatterbot自带的语言库
    trainer = ChatterBotCorpusTrainer(c)

    # 训练语言库
    trainer.train("chatterbot.corpus.english")

# 使用自己设定的语言库
cat_data = open("training/cat.txt").read().splitlines()
catTrainer = ListTrainer(catBot)
catTrainer.train(cat_data)

# Catbot是训练的聊天机器人
bot_dict = {"cat":catBot}
bot_name = "cat"

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cat")
def cat():
    bot_name = "cat"
    return render_template("bunny.html")

@app.route("/get")

#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    bot = bot_dict.get(bot_name)
    return str(bot.get_response(userText))        

if __name__ == "__main__":
    # app.debug = True
    app.run(port=7000)