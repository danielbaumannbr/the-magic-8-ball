import random
import time
#lista
respostas=[
    "É certo",
    "É claramente verdade",
    "Na minha opinião, sim",
    "Provavelmente",
    "Resposta confusa, tente novamente",
    "Pergunte novamente mais tarde",
    "Não conte com isso",
    "Minha resposta é não"
]
print("🎱 The magic 8 ball 🎱")
print("Faça uma pergunta de sim ou não")
print("Digite 'Sair' para encerrar o jogo")
while True:
    pergunta=input("Faça a sua pergunta: ").strip()
    if(pergunta.lower()=='sair'):
        print("Até breve.")
        break
    if(pergunta==""):
        print("Faça uma pergunta.")
        continue
    print("Adivinhando...",end=" ")
    for _ in range(3):
        print("🎱",end=" ")
        time.sleep(0.5)
    resposta = random.choice(respostas)
    print("\nResposta: ",resposta)