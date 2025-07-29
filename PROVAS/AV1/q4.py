T = int(input())

if T <= 100:
    for _ in range(T):
        n = int(input())
        if 1 <= n <= 100:
            instrucoes = []
            vetorNum = []
            for i in range(n):
                instrucoes.append(input())
            for elemento in range(len(instrucoes)): 
                instrucao = instrucoes[elemento]
                if 'L' in instrucao: 
                    vetorNum.append(-1)
                elif 'R' in instrucao: 
                    vetorNum.append(1)
                elif 'SAME AS' in instrucao: 
                    indice = int(instrucao.split()[-1]) - 1
                    vetorNum.append(vetorNum[indice])
            print(sum(vetorNum))