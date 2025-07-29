#funcao para imprimir os candidatos
def imprimirCandidatos(arquivo): 
    print("Candidatos: ", "\n")
    with open(arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())
    print()  #dá espaco para votos

#funcao para imprimir os votos
def imprimirVotos(arquivo):
    print("Votos: ", "\n")
    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())


#funcao para fazer um dicionario de candidatos com os numeros e seus respectivos candidatos
def lerCandidatos(nome_arquivo): 
    candidatos = {} #dicionario vazio
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo: #abra o arquivo ... para leitura como arquivo
        for linha in arquivo: #para cada linha em arquivo
            if "-" in linha:  #se "-" está na linha
                numero, nome = linha.split("-", 1)  #ex: '77' 'Carlos'
                candidatos[numero] = nome  #ex: {'99': 'João'}
    return candidatos 

#funcao para votos validos 
def votos(arquivo, candidatos):
    dicio_votos = {} #dicionario de votos
    votos_registrados = 0 #votos registrados inicialmente sendo zero

    for numero in candidatos: #para cada candidato
        dicio_votos[numero] = 0 #numero inical de votos é zero
    with open(arquivo, "r") as arquivo: 
        votos_valido = 0
        for linha in arquivo:  #para cada linha em arquivo
            votos_registrados += 1
            voto = linha.strip() # linha[:-1]
            if voto in candidatos:
                dicio_votos[voto] += 1
                votos_valido += 1
    return votos_registrados, votos_valido, dicio_votos

def analisar_resultados(votos_valido, votos_registrados, dicio_votos, candidatos): 
    maior_chave = 0  #numero dos candidatos
    valor_max = 0   #quantidade de votos que cada candidato recebeu

    for chave in dicio_votos: 
        if dicio_votos[chave] > valor_max:
            maior_chave = chave 
            valor_max = dicio_votos[chave]

    print(f"Votos registrados: ", votos_registrados ) #printando votos registrados
    print(f"Votos válidos: ", votos_valido) #printando votos válidos

    dicio_votos.pop(maior_chave)  #removendo o candidato com mais votos

    #repetindo o processo:
    seg_maior_chave = 0  #numero dos candidatos
    seg_valor_max = 0   #quantidade de votos que cada candidato recebeu

    for chave in dicio_votos: 
        if dicio_votos[chave] > seg_valor_max:
            seg_maior_chave = chave 
            seg_valor_max = dicio_votos[chave]

    if valor_max > (votos_valido/2): 
        print("Não haverá segundo turno. Candidato eleito: " f"{candidatos[maior_chave]} ({maior_chave}) ")

    else: 
        print("Haverá segundo turno entre os candidatos " f"{candidatos[maior_chave]} ({maior_chave}) e "
              f"{candidatos[seg_maior_chave]} ({seg_maior_chave}) ")

#Programa principal ---------------------------------------
arquivo1 = input() #arquivo de candidatos
arquivo2 = input() #arquivo de votos

imprimirCandidatos(arquivo1)
imprimirVotos(arquivo2)

candidatos = lerCandidatos(arquivo1)
votos_registrados, votos_valido, dicio_votos = votos(arquivo2, candidatos)
analisar_resultados(votos_valido, votos_registrados, dicio_votos, candidatos)
