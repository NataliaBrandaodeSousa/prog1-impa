def sorted(lista):
    if len(lista) <= 1: 
        return lista 
    
    menores = []
    maiores = []

    pivo = lista[0]
    for x in lista[1:]: 
        if x <= pivo: 
            menores.append(x)
        else: 
            maiores.append(x)
            
    return sorted(menores) + [pivo] + sorted(maiores)


N = int(input())
vetor = []

for _ in range(N): 
    vetor.append(int(input()))

vetorPar = []
vetorImpar = []
vetorImpar2 = []

for elemento in vetor: 
    if elemento % 2 == 0: 
        vetorPar.append(elemento)
    else: 
        vetorImpar.append(elemento)

vetorPar = sorted(vetorPar)
vetorImpar = sorted(vetorImpar)

for i in range(len(vetorImpar)-1, -1, -1):
    vetorImpar2.append(vetorImpar[i])

for elemento in vetorPar: 
    print(elemento)

for elemento in vetorImpar2: 
    print(elemento)