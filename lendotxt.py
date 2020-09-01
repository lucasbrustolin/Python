""" 
# -------------------------------------------------------------------------------------
#                                       EXEMPLO 1
#
# Description: Testando os metodos read(), readline() e readlines()
# -------------------------------------------------------------------------------------

manipulador = open('arquivo.txt','r')

print("\nMétodo read():\n")
print(manipulador.read())

manipulador.seek(0) # volta para inicio do arquivo

print("\nMétodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0) 

print("\nMétodo readlines():\n")
print(manipulador.readlines())

manipulador.close()

# -------------------------------------------------------------------------------------
#                                       EXEMPLO 2
#
# Description: Testando com estrutura de repeticao + metodo rstrip
# -------------------------------------------------------------------------------------
print('Teste de abertura de arquivo em Python')
print('Tentando abrir um arquivo de texto armazenado no PC')

manipulador = open('resource/arquivo.txt','r')
for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close()

# -------------------------------------------------------------------------------------
#                                       EXEMPLO 3
#
# Description: Testando com estrutura de repeticao + contador de linhas 
# -------------------------------------------------------------------------------------

print("\nContando as linhas do arquivo texto")
contador = 0
arquivo = open ('resource/arquivo.txt','r')
for linha in arquivo:
    contador = contador + 1
print('Número de linhas no arquivo: ', contador )
# print('Número de linhas no arquivo: ' + str(contador) )
arquivo.close()
"""
# -------------------------------------------------------------------------------------
#                                       EXEMPLO 4
#
# Description: Busca palavra chave dentro no arquivo texto (Case Sensitive)
# -------------------------------------------------------------------------------------
print("\nRetornado somente as linhas que possuem a palavra Python")
arquivo = open ('resource/arquivo.txt','r')
contador = 0
for linha in arquivo:
    linha = linha.rstrip()
    if 'Python' in linha:
        contador = contador + 1
        print(linha)
print('\nNumero de linhas que possuem a palavra Python:', contador )
arquivo.close()