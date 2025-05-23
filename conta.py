class Conta:
    # método construtivo
    def __init__(self , agencia , numero , titular , saldo , senha , ):
        #criando atributos da classe
        #atributo privado usa 2 underlines "__"
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha
    
    def extrato(self):
        return self.__saldo 

    def sacar(self , valor):
        if self.__saldo >= valor and valor >= 0:
            self.__saldo -= valor 
            return True
        else:
            return False

    def depositar (self,valor):
        if valor >0 :
            self.saldo += valor 
            print(f"déposito de" , valor,  "realizado com sucesso ")
        else:
            print("não é possivel depoitar ")
