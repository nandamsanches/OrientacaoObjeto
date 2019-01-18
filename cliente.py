
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #def get_nome(self):
    #   esse metodo garante que primeira letra seja maiuscula
    #   return self.nome.title()

    #fala que método é uma propriedade, então quando chama o método, não precisa colocar parenteses, mas por baixo dos panos
    #ta chamando esse método
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome