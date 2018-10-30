from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Chate Bot Do Ademar')

conversa = [
    'Oi', 'Olá', 'Tudo bem ?', 'Tudo certo :)',
    'Você é um programador ?', 'Sim, eu programo em Python ;)'
    'VOcê é a Skynet ?', 'Sim... Ops, na verdade não :)'
    ]

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Bot:', resposta)
    else:
        print('Bot: Ainda não sei te responder isso :(')
