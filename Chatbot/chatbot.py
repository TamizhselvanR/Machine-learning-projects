from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import os
import pyttsx3
engine = pyttsx3.init()
bot = ChatBot('bot',
              logic_adapters = [
                  {
                      'import_path':'chatterbot.logic.BestMatch',
                      'default_response':'I am sorry..But I Do not understand.',
                      'maximum_similarity_threshold':0.80
                  }
              ]
              )
while True:
    message = input("You:")
    if message.strip() == 'Bye':
        print("Bot:See you later buddy")
    else:
        reply = bot.get_response(message)
        print("Bot:",reply)
        engine.say(reply)
        engine.runAndWait()

