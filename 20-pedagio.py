import os

os.system("cls")

print("Seja bem vindo ao pedagio! ")

pergunta = input("Você está dirigindo? (sim/não): ") 

print("=" * 25)

if pergunta == "sim":
    print("\nTipos de veículos: \n(1) Carro \n(2) Moto \n(3) Caminhão")
    veiculo = input("Escolha o número do seu veículo: ")

elif(pergunta == "não"):
    print("Pedágio apenas para veículos.")
    print("=" * 25)
    input("Pressione qualquer tecla para sair.")

preco = 0

if(veiculo == "1"): 
    nome_veiculo = "carro"
    preco = 10

elif(veiculo == "2"):
    nome_veiculo = "Moto"
    preco = 5

elif(veiculo == "3"):
    nome_veiculo = "Caminhão"
    preco = 20
else:
    print("Opção invalida.")

print("=" * 25)

if(preco > 0):
    print(f"Você escolheu {nome_veiculo}, o valor a pagar do pedagio é R$ {preco}:")
elif pergunta == "sim":
    print("Não foi possível processar o pagamento.")
else:
    print("Você não pode passar sem veiculo.")


print("=" * 25)

input("pressione qualquer tecla para sair.")
