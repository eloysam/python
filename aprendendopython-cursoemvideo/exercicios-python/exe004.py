var = input('Digite algo:')

print(f"""
Tipo primitivo: {type(var)}
É um número: {var.isnumeric()}
Só tem espaços? {var.isspace()}
É uma string: {var.isalpha()}
É uma mistura entre número e string: {var.isalnum()}
Está em maíscula? {var.isupper()}
Está minúscula? {var.islower()}
Está capitalizada? {var.istitle()}""")