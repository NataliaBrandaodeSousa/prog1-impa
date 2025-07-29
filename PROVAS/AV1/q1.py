vetor = list(map(int, input().split()))

vitorias = list(map(int, input().split()))

jogadores = vetor[0]
rodadas = vetor[1]

pontuação = [0]*(jogadores)

for i in range(jogadores): 
    pontuação[i] = sum(vitorias[i:: jogadores])

maior = 0 
for i in range(1, len(pontuação)): 
    if pontuação[maior] <= pontuação[i]:
        maior = i

print(maior + 1)

