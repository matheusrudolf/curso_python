nome = 'Matheus Rondon Rudolf'
altura = 1.78
peso = 105
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Matheus Rondon Rudolf tem 1.78 de altura,
# pesa 105 quilos e seu IMC é
# 33.13975508142911