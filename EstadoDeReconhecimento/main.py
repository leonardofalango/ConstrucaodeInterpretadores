#Leonardo Falango
#   Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
# linguagem Python, C, ou C++. Este programa, quando executado, irá determinar se uma string de
# entrada faz parte da linguagem 𝐿 definida por 𝐿 = {𝑥 | 𝑥 ∈ {𝑎, 𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏}
# segundo o alfabeto Σ = {𝑎, 𝑏, 𝑐}.
#     O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
# contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
# entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que
# podem existir em um arquivo de testes para o programa que você irá desenvolver:
  
#     3
#     abbaba
#     abababb
#     bbabbaaab
#     Neste exemplo temos 3 strings de entrada. O número de strings em cada arquivo será
# representado por um número inteiro positivo. A resposta do seu programa deverá conter uma, e
# somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
# da validação conforme o formato indicado a seguir:
    
#     abbaba: não pertence.
#     A saída poderá ser enviada para um arquivo de textos, ou para o terminal padrão e será
# composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
# Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
# contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes
# devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor
# irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de
# testes criado pelo próprio professor.


# Primeiro começaremos lendo os arquivos de texto de entrada
from numpy import rec
from sklearn.model_selection import learning_curve


arq = open("entrada.txt", "r").readlines()
arq1 = open("entrada2.txt", "r").readlines()
arq2 = open("entrada3.txt", "r").readlines()


# Criaremos a função que interpreta
def reconheceString(arquivo):
    arquivo.pop(0) # Para retirar a primeira linha dos arquivos
    arquivo = arquivo[:len(arquivo) - 1] # Para retirar o \n

    reconhecimento = False # Iniciando a variável de reconhecimento
    
    # Fazendo o loop para percorrer as linhas dos arquivo
    for i in range(len(arquivo)):
        linha = arquivo[i]

        # Fazendo o loop para percorrer cada letra da linha
        for j in range(len(linha)):
            letra = linha[j]
            
            # Fazendo a comparação das letras para o reconhecimento
            if letra == "a" or letra == "b":
                if letra == "a":
                    if j == len(linha):
                        reconhecimento = False
                        break
                    
                    if linha[j+1] == "b" and linha[j+2] == "b":
                        reconhecimento = True
                    
                    else:
                        reconhecimento = False
                        break

                else:
                    reconhecimento = False
            
        if reconhecimento == True:
            print(f"Linha {i}: {linha}. Resultado: Reconhecido")
        else:
            print(f"Linha {i}: {linha}. Resultado: Não reconhecido")

arquivos = [arq, arq1, arq2] # Chamando a função para reconhecer
for arquivo in arquivos:
    reconhece = reconheceString(arquivo)
    print("___________________")
