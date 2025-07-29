

N = int(input()) #numero de testes

for _ in range(N):

    M = int(input()) #quantidade de produtos disponiveis na feira

    feira = {} #dicionario de produtos da feira, ex:. mamao: 2.19

    for _ in range(M):
        fruta, preco = input().split() #ex:. mamao 2.19
        preco = float(preco)
        feira[fruta] = preco

    P = int(input()) #qunatidade de produtos diferentes que Dona quer comprar 

    listinha = {} #listinha de compras da dona, ex:. mamao 2

    for _ in range(P):
        fruta, quant = input().split() #ex:. mamao 2.19
        quant = int(quant)
        listinha[fruta] = quant 

    total = 0
    for fruta in listinha:
        total += listinha[fruta] * feira[fruta]

    print(f"R$ {total:.2f}")
