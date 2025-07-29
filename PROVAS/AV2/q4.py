
arquivo = "experiencia.txt"

with open(arquivo, "r", encoding = "utf-8") as f:
    cobaias = 0 #numero de cobaias

    dicionario = {} #dicionario de tipo de cobaia e seu respectivo numero, ex:. coelhos:29
    dicionario["C"] = 0
    dicionario["R"] = 0
    dicionario["S"] = 0

    for linha in f:
        vetor = linha.split()
        #print(vetor)
        if len(vetor) == 2:
            numero_cobaias = int(vetor[0])
            tipo = vetor[1]

            dicionario[tipo] += numero_cobaias #ex:. coelhos:29

            cobaias += numero_cobaias

    print(f"Total:{cobaias} cobaias")

    for chave in dicionario:
        if chave == "C":
            print(f"Total de coelhos:{dicionario[chave]}")

        elif chave == "R":
            print(f"Total de ratos:{dicionario[chave]}")

        elif chave == "S":
            print(f"Total de sapos:{dicionario[chave]}")

    for chave in dicionario:

        if chave == "C":
            perc = (dicionario[chave] / cobaias) * 100
            print(f"Percentual de coelhos:{perc:.2f} %")

        elif chave == "R":
            perc = (dicionario[chave] / cobaias) * 100
            print(f"Percentual de ratos:{perc:.2f} %")

        elif chave == "S":
            perc = (dicionario[chave] / cobaias) * 100
            print(f"Percentual de sapos:{perc:.2f} %")
        
