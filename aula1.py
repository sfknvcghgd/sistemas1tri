print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
opcao = int(input("Digite a opção desejada:"))
if (opcao == 1):
    print("Você escolheu 1")
    numero_m = 10
    limite_tentativas = 3
elif (opcao == 2):
    numero_m = 20
    limite_tentativas = 5
    print("Você escolheu 2")
elif (opcao == 3):
    numero_m = 50
    limite_tentativas = 10
    print("Você escolheu 3")
else:
    print("Opção inválida")

import random
sorteio = random.randint(1, numero_m)
print("###jogo da adivinhação###")
print("adivinhe o numero de 1 a", numero_m)
tentativa = 1
while (limite_tentativas >= tentativa):
    print("tentativa:", tentativa)
    chute = int(input("digite o seu chute:"))
    if(chute == sorteio):
        print ("Parabéns,você acertou!")
        break
    elif(chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("chute um número maior!")
    tentativa = tentativa + 1  

print("O número sorteado era: ##", sorteio, "##")
print("### FIM DO JOGO ###")

