print('--------------- TABUADA -----------------')
num = int(input('Digite um número de 0 a 9:'))

for i in range(0, 11):
    print(f'{num} x {i} = {num * i}')

numero = int(input('Digite um número de 11 a 20:'))

for i in range(11, 21):
    print(f'{numero} x {i} = {numero * i}')