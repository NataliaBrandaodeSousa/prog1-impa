def hanoi(n , A , B , C): 
    if n > 0: 
        x = hanoi(n-1 , A , C , B)
        print("Move disco" , n , "de" , A,  "para" ,  C)
        y = hanoi(n-1 , B , A , C)
        return(x + y + 1) 
    else:
        return (0)

n = int(input("Digite um inteiro n para saber a sequência mínima de movimentos " \
"para ganhar o jogo da Torre de Hanói com n discos e três pinos: " ))

Origem = "A"
Trabalho = "B"
Destino = "C"

movimentos = hanoi(n, Origem , Trabalho , Destino)
print("A quantidade de movimentos dessa sequência é", movimentos)
