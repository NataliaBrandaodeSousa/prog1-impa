
#funcao para retornar a matriz
def imprimir_matriz(nomeArquivo):
    matriz = [] #criando uma matriz vazia

    dados = open(nomeArquivo, "r")  #arquivo ja pode ser lido 
    linha = dados.readline() #lê primeira linha 

    print("A matriz de entrada é: \n")
    #imprimir a matriz 
    while linha != "": #enquanto não é o fim do arquivo 
        numeros = list(map(int, linha.split())) #transforma a linha em vetor
        matriz.append(numeros) #acrescenta o vetor a matriz

        print(linha, end = "")  #oq é colocado no fim da linha impresso
        linha = dados.readline()
    print()
    dados.close() #fecha o arquivo
    return matriz

#funcao para saber se é quadrada 
def quadrada(matriz):
    quadrada = True
    tamanhoLinha = len(matriz[0])
    if tamanhoLinha != len(matriz): 
        quadrada = False
    return quadrada

#funcao para saber se é simetrica
def simetrica( matriz, quadrada):
    numeroLinhas = len(matriz) #tamanho da matriz
    simetrica = True 
    if quadrada: 
        for i in range(numeroLinhas - 1):
            for j in range(i+1, numeroLinhas): 
                if matriz[i][j] != matriz[j][i]: 
                    simetrica = False
    else: 
        simetrica = False
    if quadrada: 
        if simetrica: 
            print("A matriz é quadrada e simétrica")
        else: 
            print("A matriz é quadrada e não é simétrica")
    else: 
        print("A matriz não é quadrada")

#funcao para encontrar moda:
def moda(matriz):
    vetor = [] #criando um vetor de numeros da matriz
    for linha in matriz: 
        for num in linha: 
            vetor.append(num)

    #frequencia de cada numero
    frequencia = {}

    # Conta quantas vezes cada valor aparece
    valores_unicos = list(set(vetor))
    for num in valores_unicos: 
        frequencia[num] = 0 

    for elemento in vetor: 
        frequencia[elemento] += 1

    #achando o maximo em frquencia
    maior_valor = 0
    chave_maior_valor = 0

    for chave in frequencia:
        valor = frequencia[chave]
        if valor > maior_valor:
            maior_valor = valor
            chave_maior_valor = chave

    print("A moda da matriz é ", chave_maior_valor)

#Programa Principal ---------------------------------------------------

nomeArquivo = input()
matriz = imprimir_matriz(nomeArquivo)
quadrada = quadrada(matriz)
simetrica(matriz, quadrada)
moda(matriz)



