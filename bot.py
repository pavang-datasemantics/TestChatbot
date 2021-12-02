from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot

chatbot = ChatBot('bot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
#           logic_adapters=[
#               'chatterbot.logic.MathematicalEvaluation', #MathematicalEvaluation adapter solves math problems
#               'chatterbot.logic.TimeLogicAdapter',       #TimeLogicAdapter evaluates time based inputs
#               'chatterbot.logic.BestMatch']
            database_uri='sqlite:///dB.sqlite3')

# Training the bot with chatterbot english corpus, uncomment while running the script for first time

# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")

""" Uncomment to use in terminal window

name = input("Enter your name ")
print("welcome to the chatbot testing", name)
while True:
    request = input(name+ ':')
    if request == 'bye' or request == 'BYE' or request == 'Bye':
        print('Bot: Bye!')
        break
    else:
        response=chatbot.get_response(request)
        print('Bot:', response)

"""