import os
import json
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__, template_folder='template', static_folder='static')

class ChatbotConfig:
    NAME = "Camilla"
    STORAGE_ADAPTER = "chatterbot.storage.SQLStorageAdapter"
    DATABASE_URI = "sqlite:///my_database.db"  # SQLite database URI
    LOGIC_ADAPTERS = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]

def create_chatbot(config):
    chatbot = ChatBot(
        config.NAME,
        storage_adapter=config.STORAGE_ADAPTER,
        database_uri=config.DATABASE_URI,  # Set the database URI
        logic_adapter=config.LOGIC_ADAPTERS
    )
    return chatbot

def train_chatbot(chatbot, training_data):
    trainer = ListTrainer(chatbot)
    trainer.train(training_data)

# Load configuration
chatbot_config = ChatbotConfig()

# Create and train the chatbot
chatbot = create_chatbot(chatbot_config)
training_data = open("training/cat.txt").read().splitlines()
train_chatbot(chatbot, training_data)

# Create and train the chatbot
chatbot = create_chatbot(chatbot_config)
training_data = open("training/cat.txt").read().splitlines()
train_chatbot(chatbot, training_data)

# Define app routes
@app.route("/")
def index():
    return render_template("bunny.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText == "byebye":
        shutdown_server()
        return str("byebye")
    else:
        return process_user_input(userText)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def process_user_input(userText):
    bot_response = chatbot.get_response(userText)
    
    response_data = {
        "text": bot_response.text,
        "confidence": bot_response.confidence,
        "in_response_to": [str(s) for s in bot_response.in_response_to]
    }
    
    result = {"status_code": 990, "message": "Processed successfully", "data": response_data}
    
    return_as_json = True
    if return_as_json:
        return json.dumps(result)
    else:
        return result

if __name__ == "__main__":
    app.run(port=7000)