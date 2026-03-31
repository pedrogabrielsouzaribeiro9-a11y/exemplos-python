import os
import random
os.system("cls")

print("Seja bem vindo ao jogo de adivinhação!")

numero_secreto = random.randint(1,10)
palpite = int(input("Digite um numero: "))

if(palpite == numero_secreto):
    print("Você acertou! ")
elif(palpite > numero_secreto):
    print("O seu palpite é o maior que o número secreto! ")
elif(palpite < numero_secreto):
    print("O seu palpite é menor que o número secreto")

print(f"O numero secreto foi: {numero_secreto}")

