""" OPERAÇÕES ARITMÉTICAS

+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão
** -> potência
// -> divisão inteira
% -> resto da divisão
"""
"""
    ORDEM DE PRECENDÊNCIA
    
1° - ()
2° - **
3° - *, /, //, %
4° - +, - 
"""
print(f"""
5 + 2 = {5 + 2}
5 - 2 = {5 - 2}
5 x 2 = {5 * 2}
5 % 2 = {5 / 2}
5^2 = {5 ** 2}
5 / 2 *sem resto = {5 // 2}
resto da divisão = {5 % 2}""")

print(pow(3, 2))
print(pow(81, 1/2))
print(round(pow(128, 1/3), 2))
print('=' * 9)
print('*' * 90)

nome = str(input('Qual é o seu nome?'))
print('Prazer em te conhecer,{:=^20}!'.format(nome))

