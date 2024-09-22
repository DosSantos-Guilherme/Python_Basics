'''
autor: Guilherme Rodrigues dos Santos
data de criação: 22/09/2024
descrição: atividade aberta 2 para a disciplina ELT 572
Para executar passe como argumento o numero da questão
exemplo:
para rodar a questão 1 execute:
python3 atividade_aberta_2.py 1
'''

#Questão 1
#Recebe a entrada de 5 nota, faz a media e retorna se o aluno foi aprovado ou reprovado
from sys import argv
if int(argv[1]) == 1:
    nota_usuario = []
    media_nota_usuario = 0.0
    numero_de_notas = 5
    media_aprovacao = 60.0
    for i in range(numero_de_notas):
        nota_usuario.append(float(input(f"insira a nota {i+1}: ")))
        media_nota_usuario+=nota_usuario[i]

    if (media_nota_usuario/numero_de_notas >= media_aprovacao):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado")

#Questão 2
#Imprime a soma de cada linha de uma matriz 5x5
elif int(argv[1]) == 2:
    #arbitrando o valor da matriz
    matriz = [[5,5,5,5,5],[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4]]
    quantidadeLinhas = 5
    quantidadeColunas = 5
    string_resposta = ""
    for i in range(quantidadeLinhas):
        soma_linha_matriz = 0
        for j in range(quantidadeColunas):
            soma_linha_matriz += matriz[i][j]
        string_resposta += f"Soma da linha {i+1}= " + str(soma_linha_matriz) + "\n" 

    print(string_resposta)

#Questão 3

elif int(argv[1]) == 3:
    def condicaoVerdadeira(ent1,ent2):
        if (ent1 - ent2) < 0:
            print("\033[1m condição:\033[0m caso ent1 menos ent2 seja menor que zero")
        if (ent1 * ent2) < 0:
            print("\033[1m condição:\033[0m caso ent1 multiplicando ent2 seja menor que zero")
        if (ent1 + ent2) < 0:
            print("\033[1m condição:\033[0m caso ent1 somando ent2 seja menor que zero")


    condicaoVerdadeira(-4,3)

elif int(argv[1]) == 4:
    def criptografa_mensagem(caractere,string_entrada,tamanho_da_string):
        string_saida = ""
        for i in range(tamanho_da_string):
            char = string_entrada[i]
            if i%2 == 0:
                char = caractere
            string_saida+=char
        return string_saida
    string1 = "a vida é bela demais"
    print(string1)
    print(criptografa_mensagem("k",string1,len(string1)))