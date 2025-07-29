#Essa linha nos d ́a acesso `a fun ̧c ̃ao choices, que utilizaremos para fazer escolhas aleat ́orias com
#probabilidades prescritas.
from random import choices

#função que devolve dicionario de ocorrẽncias para uma certa frase
def frase_para_ocorrencias(frase):
    dicionario = {} #dicionario de ocorrencias vazio 
    palavras = frase.split() #vetor de palavras da frase
    conjunto = set() #conjunto vazio de palavras
    for palavra in palavras: 
        conjunto.add(palavra) #conjunto de palavras da frase
    
    for palavra in conjunto: 
        contador = {}
        for i in range(len(palavras) - 1):
            if palavras[i] == palavra:
                proxima = palavras[i+1]
                if proxima in contador :
                    contador[proxima] +=1 
                else: 
                    contador[proxima] = 1
        dicionario[palavra] = contador

    return dicionario 

#função que devolve a concatenação de dois dicionarios de ocorrencias 
def concatenar_ocorrencias(ocorrencias1, ocorrencias2):
    resultado = {}

    #faz um conjunto de chaves que aparecem em ocorrencias 1 e 2
    todas_chaves = set(ocorrencias1.keys()) | set(ocorrencias2.keys())

    for chave in todas_chaves:
        d1 = ocorrencias1.get(chave, {}) #dicionario interno ou vazio
        d2 = ocorrencias2.get(chave, {}) #dicionario interno ou vazio

        #pega tds as chaves internas
        todas_subchaves = set(d1.keys()) | set(d2.keys())
        interno = {} #novo dicionario interno 

        for subchave in todas_subchaves:
            v1 = d1.get(subchave, 0) #valor da subchave, se nn tiver é zero
            v2 = d2.get(subchave, 0)
            interno[subchave] = v1 + v2 #dai uma chave com valor é acrescentado nesse novo dicionario interno

        resultado[chave] = interno #e o novo dicionario externo é incrementado

    return resultado

#funcao que ler um arquivo de texto e retorna dicionario de ocorrencias para as palavras desse arquivo
def arquivo_para_ocorrencias(arquivo):
    resultado = {} #dicionario acumulador
    for linha in arquivo:
        ocorencias_linha = frase_para_ocorrencias(linha)
        resultado = concatenar_ocorrencias(resultado, ocorencias_linha)
    return resultado 

#funcao que ler um dicionario de ocorrencias e retorna um diconario de frequencias
def ocorrencias_para_frequencias(ocorrencias):
    for chave in ocorrencias:
        d1 = ocorrencias.get(chave) #tenho aqui o dicionario interno
        soma_valores_subchaves = sum(d1.values()) #somos os valores das subchaves
    
        if soma_valores_subchaves == 0:
            continue #mantém o dicionário interno vazio

        for subchave in d1:
            d1[subchave] = d1[subchave] / soma_valores_subchaves

    return ocorrencias

#funcao que recebe uma palavra_atual e um dicionario de frequencias,
#e retorna uma das possıveis palavras seguintes a palavra_atual sorteada de acordo com as probabilidades
def sortear_proxima_palavra(palavra_atual, frequencias):
    #verificando se a palavra atual está no dicionário externo
    if palavra_atual not in frequencias:
        return ""
    
    #obtém o dicionário interno da palavra atual
    dicionario_seguinte = frequencias[palavra_atual]

    #se não tiver palavras seguintes à palavra atual
    if not dicionario_seguinte:
        return ""

    #obtendo as listas das palavras seguintes à palavra atual e das frequencias
    proximas_palavras_possiveis = list(dicionario_seguinte.keys())
    lista_de_frequencias = list(dicionario_seguinte.values())

    # Sorteia a próxima palavra com base nas frequências
    proxima_palavra = choices(proximas_palavras_possiveis, lista_de_frequencias)[0]

    return proxima_palavra

#recebe um dicionario de ocorrencias e retornar uma string de texto com no maximo
#50 palavras
def gerar_texto(ocorrencias):
    #criando um conjunto de palavras do texto
    conjunto = set(ocorrencias.keys())

    #criando uma lista de palavras
    listaPalavras = list(conjunto)

    #primeira palvra do texto
    primeira_palavra = choices(listaPalavras)[0]

    #texto inicia com a primeira palavra
    texto = [primeira_palavra]
    palavra_atual = primeira_palavra

    #gera até o texto ter 50 palavras (ou até não ter mais palavra seguinte)
    while len(texto) <= 50:
        proximaPalavra = sortear_proxima_palavra(palavra_atual, ocorrencias)

        if proximaPalavra == "":
            break #encerra

        texto.append(proximaPalavra)
        palavra_atual = proximaPalavra

    return ' '.join(texto)


#--------------------------------------------------------------------------------
arquivo = open("g1_rj.txt", "r", encoding = "utf-8")
#concatenação = {'hoje': {'está': 2}, 'está': {'sol': 1, 'nublado': 1}, 'sol': {}, 'nublado': {}}

ocorrencias = arquivo_para_ocorrencias(arquivo)

arquivo.close()

#---------------------------------------------------------------------------------
#print(arquivo_para_ocorrencias("g1_rj.txt"))
#print(arquivo_para_ocorrencias("arquivo.txt") == concatenação) 
#print(ocorrencias_para_frequencias(ocorrencias))

#---------------------------------------------------------------------------------
freuqencias = ocorrencias_para_frequencias(ocorrencias)
#proximaPalavra = sortear_proxima_palavra("está", ocorrencias)
#print(proximaPalavra)

#----------------------------------------------------------------------------------

print("texto: ")
texto = gerar_texto(ocorrencias)
print(texto)
