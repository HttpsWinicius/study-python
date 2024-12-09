# Criar lista
my_list = [1, 2, 3]  # Cria uma lista vazia
print(f'Essa eh minha lista: {my_list} ')

my_list_data = [1,2,3,'String']
print(f'Essa eh minha lista com diferentes tipos de dados {my_list_data}')

# Índice e corte de lista
my_list_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Acessando o primeiro elemento da minha lista:', my_list_index[0])  # Acessa o primeiro elemento (1)
print('Acessando o ultimo elemento da minha lista:', my_list_index[-1])  # Acessa o último elemento (5)
print('Acessando aos elementos 0 ao 3 da minha lista:', my_list_index[0:3])  # Acessa do primeiro ao terceiro elemento ([1, 2, 3])

# Métodos básicos da lista
my_list_method = ['ID','SEXO', 'IDADE']
my_list_method.append('EMAIL')  # Adiciona email ao final da lista
print(f'Adicionando um elemento a mais em linha lista {my_list_method}')

tamanho_lista = len(my_list_method)
print(f'O tamanho da minha lista eh de: {tamanho_lista} elementos.')

extrair_ultimo_elemento = my_list_method.pop()
print(f'Extraindo o ultimo elemento de minha lista: {extrair_ultimo_elemento}')

print(f'Agora minha lista nao possui mais EMAIL: {my_list_method}')

extrair_elemento_com_indice = my_list_method.pop(0)
print(f'Extraindo o id da minha lista: {extrair_elemento_com_indice}')

my_list_method_reverse = ['a', 'b', 'c']
my_list_method_reverse.reverse()
print(f'Agora minha lista está com a ordem reversa: {my_list_method_reverse}')

# Listas aninhadas
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
matrix = [list_1, list_2, list_3]
print('Minha matrix: ', matrix)
print('Acessando a primeira lista da matrix: ', matrix[0])  # Acessa a primeira lista ([1, 2, 3])
print('Acessando o terceiro elemento da segunda lista: ', matrix[1][2])  # Acessa o terceiro elemento da segunda lista (6)

# Introdução ao método de compreensão em lista
first_col_lists = [row[0] for row in matrix]
print(first_col_lists)