custos = [900, 350, 300, 400]
ganhos = [4000, 750, 1200]


def somatorio(lista):
    return sum(lista)

total_custos = somatorio(custos)
total_ganhos = somatorio(ganhos)


diferenca = total_ganhos - total_custos


print(f"Total de custos: R${total_custos}")
print(f"Total de ganhos: R${total_ganhos}")
print(f"Diferença (ganhos - custos): R${diferenca}")

