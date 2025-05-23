nome = Lucas 
numero_chamada = 10

print("Olá! Seja bem-vindo ao sistema. Este código foi desenvolvido por ",nome ", número da chamada "numero_chamada".")

altura = 1.73
musicaFavorita = do ya like
filmeFavorito =  Interestelar

nota_musicaFavorita = 8.8
nota_filmeFavorito = 9.3

minha_altura = 1.75

altura_usuario = float(input("Digite sua altura em metros (ex: 1.70): "))

if altura_usuario > minha_altura:
    print("Você é mais alto(a) do que eu!")
elif altura_usuario < minha_altura:
    print("Você é mais baixo(a) do que eu!")
else:
    print("Temos a mesma altura!")