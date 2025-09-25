import random
import time

input("Pressione 'ENTER' para inicar o jogo. \n")
decisao = input("Você conhece o jogo? Sim/Não:").lower()
if decisao != 'sim':
    print("Escolha um lugar pra se esconder (1 a 5)...")
    print("Se o buraco negro aparecer no mesmo lugar, você some! 🕳️")
    print("Se não, parabéns: você sobreviveu (por enquanto). \n")
nome = input("Digite seu nome: ")
time.sleep(1)
while True:
    print("Escolha uma posição de 1 a 5")
    escolha = int(input('''[1]
[2]
[3]
[4]
[5]
Escolha: '''))
    time.sleep(1)
    posicaoAleatoria = random.randint(1,5)
    if posicaoAleatoria == escolha:
        print("Você sugado pelo buraco negro. 💀")
    else:
        print(f"Você escapou! Parabéns {nome}. 😅")
    
    continuar = input("Jogar novamente? 👾 Sim/Não:  ")
    if continuar != 'sim':
        break