import random
import os

os.system("cls")

print("Seja bem vindo á batalha de pokemon! ┌∩┐(◣_◢)┌∩┐")
input("\nPressione a tecla enter para continuar.")

print("\nSua vida inicial é 100 Hp  (•_•)")
print("Seu ataque é de -10hp de força ao atacar o inimigo  〴⋋_⋌〵")
print("Sua cura carrega de +5hp  (+_+)")
print("Sua defesa bloqueia 100% do próximo dano! |˚–˚|")

# Definição das variáveis numéricas
vida_inicial = 100
vida_comp = 110
ataque_player = 10
cura_player = 5

input("="* 60)
print("\nA BATALHA VAI COMEÇAR!! ►.◄ ")
input("Você está andando em um bosque longe da vila...")
input("\nE SE DEPARA COM UM FILHOTE DE DRAGÃO!!")
print("informações do monstro: 110 HP | 10 FORÇA.")

while vida_inicial > 0 and vida_comp > 0:
    
    defendendo = False
    
    print(f"\n" + "-"*30)
    print(f"VOCÊ: {vida_inicial} HP | MONSTRO: {vida_comp} HP")
    print("-"*30)

    try:
        opcao = int(input("\nOque fazer?  ATAQUE(1)  CURAR(2) DEFENDER(3) FUGIR(4): "))
    except ValueError:
        print("Digite apenas números de 1 a 4!")
        continue

    if opcao == 1:
        print("\nO seu ataque causou no monstro menos 10 HP de vida! ╚(•⌂•)╝")
        vida_comp -= ataque_player

    elif opcao == 2:
        print("\nVocê recebeu +5 HP recuperando sua vida. (+_+)")
        vida_inicial += cura_player

    elif opcao == 3:
        print("\nVocê levantou o escudo! Defesa ativada! ")
        defendendo = True

    elif opcao == 4:
        print("\nVOCÊ FUGIU! SEU COVARDE HAHAHA! \nGAME OVER (✖﹏✖)")
        break 
    else:
        print("Opção inválida! Perdeu a vez.")

    if vida_comp > 0 and opcao != 4:
        opcao_comp = random.randint(1, 4)
        
        if defendendo:
            print(f"\nO monstro tentou o ataque {opcao_comp}, mas seu ESCUDO bloqueou tudo! |˚–˚|")
        else:
            if opcao_comp == 1:
                print("\nO monstro usou um SUPER ATAQUE balançando a calda! (-15 HP)")
                vida_inicial -= 15
            
            elif opcao_comp == 2:
                print("\nO monstro deu uma mordida em você! (-10 HP)")
                vida_inicial -= 10
                
            elif opcao_comp == 3:
                print("\nO monstro tentou te atacar mas se escondeu com medo!")

            elif opcao_comp == 4:
                print("\nO monstro soltou um rugido curativo e ganhou +5 HP!")
                vida_comp += 5

if vida_inicial <= 0:
    print("\nSua vida chegou a 0...")
    print("Você perdeu a batalha... (✖﹏✖)")

elif vida_comp <= 0:
    print("\nO monstro caiu derrotado!")
    print("VOCÊ DERROTOU O DRAGÃO! ٩(^‿^)۶")

input("\nPressione Enter para encerrar.")