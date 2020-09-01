# -------------------------------------------------------------------------------------
#                                       EXEMPLO 1
#
# Description: Criando e escrevendo arquivo texto no modo 'W'
# -------------------------------------------------------------------------------------
"""
arquivo = open('resource/arquivocriado.txt','w')
arquivo.write('Este arquivo texto foi gerado via Python - metodo Open() = modo (w)\n')
arquivo.write('Arquivo texto ..................\n')
arquivo.write('Arquivo texto ..................\n')
arquivo.close()

#Lendo arquivo criado
print("\nLendo arquivo criado via Python\n")
arquivo = open('resource/arquivocriado.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()
"""
# -------------------------------------------------------------------------------------
#                                       EXEMPLO 2
#
# Description: Escrevendo em um arquivo ja criado - modo 'a'
# -------------------------------------------------------------------------------------
print("\n")
texto = input("Digite um texto para ser acrescentado ao arquivo criado\n")
arquivo = open('resource/arquivocriado.txt','a')
arquivo.write( texto + '\n')
print('Operacao de adicao de texto efetuada com sucesso no arquivo:' + arquivo.name + '\n'   )
arquivo.close()

#Lendo arquivo criado
print("\nLendo o texto adiconado ao arquivo!\n")
arquivo = open('resource/arquivocriado.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

