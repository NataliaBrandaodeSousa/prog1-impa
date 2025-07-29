import heapq

N, M = map(int, input().split())

# N - o numero de funcionarios 
# M - o numero de clientes 

#tempo pra cada funcionario processar um item
tempo = list(map(int, input().split()))

#numero de itens de cada cliente
itens = list(map(int, input().split())) 

#contador de tempo 
contador = [0] * (N + 1) #a posicao zero é ignorada

lista = [] #futura listinha de heap

for i in range(1, N + 1):
    lista.append((0, i))

heapq.heapify(lista) #transformando em heap

for item in itens: 
    temp_disp, funcionario = lista[0] #topo 
    contador[funcionario] += (tempo[funcionario - 1] * item) #tempo gasto
    heapq.heapreplace(lista, (temp_disp + (tempo[funcionario - 1] * item), funcionario))

max = 0 
for i in range(1, len(contador)):
    if contador[max] < contador[i]:
        max = i 

print(contador[max])
