# -------------------------------------------------------------------------------------
#                                       EXEMPLO 1
#
# Description: Criando e escrevendo arquivo texto no modo 'W'
# -------------------------------------------------------------------------------------
arquivo = open('resource/arquivocriado.txt','w')
arquivo.write('Este arquivo texto foi gerado via Python - metodo Open() = modo (w)\n')
arquivo.write('Arquivo texto ..................\n')
arquivo.write('Arquivo texto ..................\n')
arquivo.close()

#Lendo arquivo criado
print("\nLendo arquivo criado via Python\n")
arquivo = open('resource/arquivocriado.txt')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

