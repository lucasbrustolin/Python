""" 
# ----------------------
#      EXEMPLO 1
# ----------------------
# Testando os metodos read(), readline() e readlines()

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
"""

# ----------------------
#      EXEMPLO 2
# ----------------------
# Testando com estrutura de repeticao + metodo rstrip
print('Teste de abertura de arquivo em Python')
print('Tentando abrir um arquivo de texto armazenado no PC')

manipulador = open('resource/arquivo.txt','r')
for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close()

