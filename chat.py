from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
# Initialize chatbot
chatbot = ChatBot("AI Assistant")
trainer = ChatterBotCorpusTrainer(chatbot)
 
# Train chatbot with English dataset
trainer.train("chatterbot.corpus.english")
 
# Chat loop
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("AI Assistant:", response)