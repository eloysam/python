a = 'casaco'

# Funções do python
maiuscula = a.upper()
minuscula = a.lower()
capital = a.capitalize()

# podemos escolhelher qual parte da palavra queremos
metadePalavra = a[3:6]


print(a,'\n', maiuscula,'\n', minuscula,'\n', capital, '\n', metadePalavra)

a = 'casaco'

# Funções do python
maiuscula = a.upper()
minuscula = a.lower()
capital = a.capitalize()

# podemos escolhelher qual parte da palavra queremos
metadePalavra = a[5:6] # você escolhe as partes da palavra que você deseja
ultimasLetras = a[3:] # Pega as últimas letras na frase a partir da posição que você inserir

print(a,'\n', maiuscula,'\n', minuscula,'\n', capital, '\n', metadePalavra, '\n', ultimasLetras)

b = a.replace('aco', 'inha') # Aqui você substitui algum valor que você quer
c = a.replace('o', 'a')
print(a)
print(b)

c.find('s') # com a função FIND você encontra em que posição está a letra 's'

print(c)