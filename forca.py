import random 

# Iniciando minhas variáveis  
palavras = []

print("1-comidas")
print("2-ambiente")
print("3-tecnologia")

opcao=int(input("digite o tem desejado:"))
if opcao == 1:
    arquivo = open ("comidas.txt" , "r")
elif opcao == 2:
    arquivo = open ("tema2.txt" , "r")
elif opcao == 3:
    arquivo = open ("tema3.txt" , "r")
else:
    print("opção ines,selecionado opção1")
    arquivo = open ("comidas.txt" , "r")

for linha in arquivo :
    palavras.append(linha.strip())

palavra = random.choice(palavras)
limite_tentativas = len(palavra) + 5
acertou = False
enforcou = False

#cria a palavra sem preencher 
letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")

#cria o laço de repetição que executa o jogo enquanto  o jogador não acertou e nem enforcou 
contador = 1
while(not acertou and not enforcou):
    print(letras_acertadas)
    print("tentativas: ",contador,"/",limite_tentativas)
    chute =  input("digite a palavra: ")
    
    #verifica se o chute é igual a alguma letra da palavra 
    indice = 0
    for letra in palavra :
        if chute == letra:
            letras_acertadas[indice] = chute
        else :
            indice +1

    # se o contador chegar no limite : print vocẽ perdeu 
    if contador == limite_tentativas:
        enforcou = True
        print("você perdeu : ( \nA Palavra era:" , palavra)

    # verifica se (_) não tem mais 
    if letras_acertadas.count("_") == 0:
        acertou = True 
        print("Parabén, você encontrou a palavra secreta!")
        print(letras_acertadas)

    contador = contador + 1
    