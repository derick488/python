# aqui o sistema pede o nome do usuario
nome = input("digite se nome:")
# aqui o sistema pede a idade do usuario
idade = int(input("qual a sua idade:"))
# aqui mostra o nome e idade do usuario
print(f"bem vindo {nome}, voce tem {idade} anos.") 

# aqui e uma funcao de menu
def menu():
    print("como posso te ajudar hoje?")
    print("1 - bebidas")
    print("2 - salgados")
    print("3 - doces")
    print("4 - sorvetes")

# aqui grava a opcao que o usuario digitou
opc = int(input("digite o numero da opcao desejada:"))
# aqui grava a logica
if opc == 1:
    print("temos coca cola,fanta e guarana")

elif opc == 2:
    print("temos coxinha,risoles e empadao")

elif opc == 3:
    print("temos brigadeiro")

elif opc == 4:
    print("temos napolitano,flocos,morango e chocolate")