import random
import time
#lista
respostas=[ "É certo", 
           "É claramente verdade", 
           "Sem dúvida",
             "Definitivamente sim", 
             "Pode contar com isso", 
             "Na minha opinião, sim", 
             "Provavelmente", 
             "Perspectiva boa", 
             "Sim", 
             "Os sinais apontam que sim",
            "Resposta confusa, tente novamente",
                 
            "Pergunte novamente mais tarde",
              "Melhor não te contar agora", 
              "Não é possível prever agora", 
              "Concentre-se e pergunte novamente",
                "Não conte com isso", 
                "Minha resposta é não", 
                "Minhas fontes dizem que não",
                  "Perspectiva não muito boa", 
                  "Duvido muito" ]
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