N = int(input())

for i in range(N): 
    lista =  input().split(' ')
    vetornv = []
    for elemento in range(len(lista)): 
        a = lista[elemento]
        if a != "":
            vetornv.append(a[0])
    print("".join(vetornv))
        