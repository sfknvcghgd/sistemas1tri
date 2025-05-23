# from nomeDoArquivo import nomeDaClasse
from conta import Conta

conta1 = Conta (123, "10500-10", "Franciscocisco", 7.0, 1234)
print(conta1.extrato())

#Criar o saque e o deposito na classe

if conta1.sacar(2.0):
    print("saque efetuado com sucesso!")
else:
    print("Saque negado!")

print(conta1.extrato())
