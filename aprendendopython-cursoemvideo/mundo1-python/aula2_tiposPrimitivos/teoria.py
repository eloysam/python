"""
---------------------- TEORIA ----------------------------------------------------------------
4 tipos primitivos
- int
- float
- bool
- str
"""
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1 + n2  # o + significa aqui uma concatenação

# Tipos diferentes de PRINT
# print('O resultado é: {}'.format(soma))
print(f'O soma entre {n1} e {n2} é: {soma}')
print('-> A soma entre {} e {} é: {}'.format(n1, n2, soma)) # Deu certo. Jesus é muitoo bom!!
# print('O resultado é: {}'.format(soma))
print(type(soma))
