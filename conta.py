

class Conta:

    #função construtora, o que o objeto tem
    #self é como o this
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto... {}".format(self))
        # '__' quer dizer que atributo é private, vai ficar, exemplo: _Conta__numero
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} reais do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    #metodo privado, só pode ser chamado dentro da classe
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    #ja nao precisa colocar parenteses qdo chamar
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #metodo da classe, não cria um objeto, porque é da classe
    @staticmethod
    def codigo_banco():
        return "001"

    #metodo da classe
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
