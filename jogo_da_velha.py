#Criando o tabuleiro:
tabuleiro = [["-" for _ in range(3)] for _ in range(3)]
#print(tabuleiro)
#for elemento in tabuleiro:
#print(elemento)

#Começa com o jogador X
jogador_atual = "X"
ganhou = False

while True:
    #Mostrar o tabuleiro
    for elemento in tabuleiro:
        print(elemento)

    #Falar quem vai jogar
    print(f"Vez do jogador {jogador_atual}")
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))

    #Verificar a posição escolhida
    if tabuleiro[linha][coluna] == "-":
        tabuleiro[linha][coluna] = jogador_atual
    else:
        print("Posição ocupada! Tente de novo.")
     
        if jogador_atual == "O": 
            jogador_atual = "X"
        else: 
            jogador_atual = "O"

    # Combinações de Linhas
    linhas = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)], 
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for linha in linhas:
        (l1, c1), (l2, c2), (l3, c3) = linha
        #print(l1, c1, l2, c2, l3, c3)
        if tabuleiro[l1][c1] == tabuleiro[l2][c2] == tabuleiro[l3][c3] and tabuleiro[l1][c1] != "-":
            for elemento in tabuleiro:
                print(elemento)
            ganhou = True
            print(f"Jogador {jogador_atual} venceu! ")
    
    if ganhou:
        break

    #Se no fim da rodada, não teve vencedor, partiremos pra próxima rodada
    if jogador_atual == "O": 
            jogador_atual = "X"
    else: 
        jogador_atual = "O"

    if (
    tabuleiro[0][0] != "-" and tabuleiro[0][1] != "-" and tabuleiro[0][2] != "-" 
    and tabuleiro[1][0] != "-" and tabuleiro[1][1] != "-" and tabuleiro[1][2] != "-"
    and tabuleiro[2][0] != "-" and tabuleiro[2][1] != "-" and tabuleiro[2][2] != "-" 
    ): 
        break

#Caso não ocorra vencedor e todas as casas já foram preenchidas, deu empate, e portanto
#Mostra o tabuleiro e avisa que deu empate
if ganhou == False: 
    for elemento in tabuleiro:
        print(elemento)
    print("Empate!")



        
    
   

        