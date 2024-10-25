'''
String em python para armazenar textos
O python entendera que eh uma string se estiver entre aspas simples ou duplas
'''

# Declarando uma string
print('Declarando string com aspas simples: Isso eh uma string')

print("Declarando string com aspas duplas: Isso tambem eh uma string")

print(type('Tipo string'))

print("String declarando com aspas duplas e utilizando aspas simples: I'm a string")

print('String declarando com aspas simples e utilizando aspas duplas: Isso eh uma "citacao"')

print('String declarando com aspas simples e utilizando aspas simples: Isso eh uma \'citacao\'')

print('Quebra de linha em string: \nQuebra de linha')

print('Espacamento em string: \tTab')

print('Capturando tamando da string: ' + str(len('Meu tamanho eh de 31 caracteres')))


# indexacao de strings

index_string = "Olá, meu nome é Alexa, sou uma IA da Amazon"

print(f'Variavel em maiusculo: {index_string.upper()}')

print(f'Variavel em minusculo: {index_string.lower()}')

# Primeira letra
print(index_string[0])

# Ultima letra
print(index_string[-1])


print(f'Aqui serve para retornar toda a variavel: {index_string[:]}')

print(f'Aqui serve para retornar a variavel a partir do indice 2: {index_string[2:]}')

print(f'Aqui serve para retornar a variavel ate o indice 3: {index_string[:3]}')

print(f'Aqui serve para retornar a variavel a partir do indice 16 ate o indice 21: {index_string[16:21]}')

print(f'Index puxando elemento de 2 em 2: {index_string[::2]}')

print(f'Index puxando elemento de 2 em 2 a partir do indice 2: {index_string[2::2]}')

print(f'Index puxando elemento de 2 em 2 a partir do indice 2 ate o indice 10: {index_string[2:10:2]}')

print(f'Revertendo variavel: {index_string[::-1]}')

#Propriedades de string
'''
String sao imutaveis nao suporta redefinicao igual uma lista ou variavel
'''

print(f'Variavel original: {index_string}')

# index_string[0] = 'A' # Erro 'stg' object does not support item assignment

#index_string[0] = index_string + ' Agora o meu valor original mudou' # Erro 'stg' object does not support item assignment

# Concatenacao de strings

print('Concatenacao de strings: ' + 'String 1' + ' String 2')

print('Multiplicacao de strings: ' + 'String ' * 3)

print(f'Concatenacao de strings com variaveis: {index_string + " Concatenando com outra string"}')

index_string = index_string + ' Agora o meu valor original mudou'

print(f'Alterando a string original: {index_string}')

#Metodos de string

print(f'Contando quantas vezes a palavra Alexa aparece na string: {index_string.count("Alexa")}')

print(f'Encontrando a posicao da palavra Alexa na string: {index_string.find("Alexa")}')

print(f'Encontrando a posicao da palavra Alexa na string: {index_string.find("Alexa", 10)}')

print(f'Para achar o metodo de uma string basta utilizar ponto: index_string.')

print(f'Metodo split divindo pelo espaco: {index_string.split()}')

print(f'Metodo split divindo pela virgula: {index_string.split(",")}')

