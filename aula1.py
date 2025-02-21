import random

sorteio = random.randint(1, 10)
print("###jogo da adivinhação###")
print("adivinhe o numero de 1 a 10")
limite_tentativas = 3
tentativa = 1
while (limite_tentativas >= tentativa):
    print("tentativa:", tentativa)
    chute = int(input("digite o seu chute:"))
    if(chute == sorteio):
        print ("Parabéns,você acertou!")
        break
    elif(chute > sorteio):
        print("Chute um número maior!")
    elif (chute < sorteio):
        print("chute um número maior!")
    tentativa = tentativa + 1  



