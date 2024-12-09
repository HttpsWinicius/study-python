#Formatação com %:
#Inteiros:

numero = 1
print('Temos um inteiro transformado em string: %s aqui.' % numero)
#Aqui, %s é um placeholder para uma string. A variável numero é convertida para string e inserida no lugar de %s.

#Pontos Flutuantes:
#%1.0f: Formata o número flutuante sem casas decimais.
#%1.2f: Formata o número flutuante com 2 casas decimais.
#%1.4f: Formata o número flutuante com 4 casas decimais.

print('Printando pontos flutuantes sem casas decimais: %1.0f' % 13.1444)
print('Printando pontos flutuantes com 2 casas decimais: %1.2f' % 13.1444)
print('Printando pontos flutuantes com 4 casas decimais: %1.4f' % 13.1444)

#Formatação com str.format():

usar_format = 'One = {a}, Two = {b}, Three = {c}'.format(a=1, b='String', c=12.3)
print(usar_format)

#Aqui, {a}, {b}, e {c} são placeholders que são substituídos pelos valores fornecidos no método format().
# Isso permite uma formatação mais legível e flexível.


