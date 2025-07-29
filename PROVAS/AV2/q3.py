arquivo = "lesmas.txt"

def quant_linhas(arq):
    with open (arq, "r", encoding = "utf-8") as f:
        total = 0 
        for _ in f:
            total += 1

        return total

with open (arquivo, "r", encoding = "utf-8") as f:
    total_linhas = quant_linhas(arquivo)
    for linha, conteudo in enumerate(f, 1):
        if linha % 2 == 0:
            velocidades = list(map(int, conteudo.split()))
            
            #print(velocidades)
            maior = max(velocidades)

            if maior < 10:
                print("1")
            elif  20 > maior >= 10:
                print("2")
            elif( maior >= 20):
                print("3")


