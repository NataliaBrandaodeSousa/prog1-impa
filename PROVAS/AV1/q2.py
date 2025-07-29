Teste = 1

while True: 

    N = int(input()) #participantes 
    if N == 0: 
        break

    numeros = list(map(int, input().split()))
     
    for i in range(N):
        if numeros[i] == i + 1: 
            ganhador = numeros[i]
            break 

    print(f"Teste {Teste}")
    print(ganhador)
    print()


    Teste = Teste + 1

