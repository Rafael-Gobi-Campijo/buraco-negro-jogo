#bibliotecas
import random #biblioteca para gerar um valor aleatório
import time #biblioteca para dar um tempo em algumas partes do código
pontos = 0
#listas
nomes = []
recorde = []

input("Pressione 'ENTER' para inicar o jogo. \n")
decisao = input("Você conhece o jogo? Sim/Não: ").lower()
if decisao != 'sim':
    #regras do jogo
    print("Escolha um lugar pra se esconder (1 a 5)...")
    print("Se o buraco negro aparecer no mesmo lugar, você perde! 🕳️")
    print("Se não, parabéns: você sobreviveu (por enquanto). \n")
#modos de jogo
print("1 - Singleplayer")
print("2 - Multiplayer")
jogar = int(input("Qual modo de jogo você gostaria de jogar?: "))

if jogar == 1: #jogo singleplayer
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
        posicaoAleatoria = random.randint(1,5)#a maquina i´ra escolher um número aleatório
        if posicaoAleatoria != escolha:
            print(f"Você escapou! Parabéns {nome}. 😅")
            pontos += 1
        else:
            print("Você foi sugado pelo buraco negro. 💀")
            break

    print(f"Parabéns, {nome}!! Sua pontuação: {pontos} pontos.")#pontuação

elif jogar == 2:#jogo multiplayer
    n1 = int(input("Quantos jogadores?: "))
    cont = 1
    for c in range(n1):
        nome = input(f"Nome do jogador {cont}: ")
        nomes.append(nome)
        cont += 1
    time.sleep(1)
    cont1 = 0
    while n1 > cont1:
        print(f"Vez do {nomes[cont1]}")
        pontos = 0
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
                print(f"Você escapou! Parabéns {nomes[cont1]}. 😅")
                pontos += 1
            else:
                print("Você sugado pelo buraco negro. 💀")
                recorde.append(pontos)
                break
        cont1 += 1
    melhor = max(recorde) #variavel para pegar a melhor pontuação
    campeao = recorde.index(melhor) #variavel para pegar o nome do vencedor
    print(f"O campeão foi o 🥇 {nomes[campeao]} 🏆 com {melhor} pontos ")#campeão
    ("~~"*10)
    print("\n\n!!!RANKING!!!")
    print("~~"*10)
    for i in range(n1):
        recorde.append(0)
        print(f"{i+1}º - {nomes[campeao]} - {melhor} pontos")
        recorde.remove(melhor)
        nomes.pop(campeao)
        melhor = max(recorde)
        campeao = recorde.index(melhor)
    print("~~"*10)
else:
    print("Número inválido")
