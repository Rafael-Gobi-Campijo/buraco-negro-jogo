import random
import time
pontos = 0

input("Pressione 'ENTER' para inicar o jogo. \n")
decisao = input("Você conhece o jogo? Sim/Não:").lower()
if decisao != 'sim':
    print("Escolha um lugar pra se esconder (1 a 5)...")
    print("Se o buraco negro aparecer no mesmo lugar, você some! 🕳️")
    print("Se não, parabéns: você sobreviveu (por enquanto). \n")

print("1 - Singleplayer")
print("2 - Multiplayer")
jogar = int(input("Qual modo de jogo você gostaria de jogar?: "))

if jogar == 1:
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
        if posicaoAleatoria != escolha:
            print(f"Você escapou! Parabéns {nome}. 😅")
            pontos += 1
        else:
            print("Você sugado pelo buraco negro. 💀")
            break

    print(f"Parabéns, {nome}!! Sua pontuação: {pontos} pontos.")

elif jogar == 2:
    n1 = int(input("Quantos jogadores?: "))
    cont = 1
    for c in range(n1):
        nome = input(f"Nome do jogador {cont}: ")
        cont += 1
    time.sleep(1)
    cont1 = 0
    while n1 > cont1:
        cont1 += 1
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
            if posicaoAleatoria != escolha:
                print(f"Você escapou! Parabéns {n1}. 😅")
                pontos += 1
            else:
                print("Você sugado pelo buraco negro. 💀")
                break
