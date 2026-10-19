# Aula 1

#Intruões da Prática

'''
Escreva um script em Python que cumpra os seguintes requisitos:

Crie variáveis para armazenar o nome de um produto, o preço unitário (com decimais) e a quantidade comprada.

Calcule o valor total gasto na compra.

Imprima uma mensagem na tela utilizando interpolação de strings (f-strings) exibindo o nome do produto e o preço total calculado.
'''

produto_nome = "maçã"
produto_preco = 2.75
quantidade = 5
valor_gasto = produto_preco * quantidade
print(f"A compra do produto {produto_nome} deu o valor total de R$ {valor_gasto:.2f}.")