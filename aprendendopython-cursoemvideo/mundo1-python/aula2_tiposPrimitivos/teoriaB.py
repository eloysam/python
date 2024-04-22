""" FUNÇÕES QUE SERAM ÚTEIS, EM NOME DE JESUS

Métodos de teste de tipo -> IS """

# ISNUMERIC -> Irá verificar se é possível converter o que foi digitado em um número tipo INT
n = input('Digite algo:')
print(f'ISNUMERIC - {n.isnumeric()}')

# ISALPHA -> verifica se algo está no alfabeto - UNICAMENTE
print(f'ISALPHA - {n.isalpha()}')

# ISALNUM -> Verifica se há número e letra juntas
print(f'ISALNUM -{n.isalnum()}')

# ISUPPER -> Verifica se todas as letras estão em letras maíusculas
print(f'ISUPPER - {n.isupper()}')

# ISTITLE -> Verifica se está capitalizada (Ex: Bíblia)
print(f'ISTITLE - {n.istitle()}')
# ISSPACE -> Verifica se SÓ tem espaços
print(f'ISSPACE - {n.isspace()}')