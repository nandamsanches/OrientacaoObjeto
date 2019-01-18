

class Programa:
    def __init__(self, nome, ano):
        #se tivesse dois underlines ficaria privada e ai as classes filhas nao podiam usar
        #colocando só um underline fica um jeito protegido (lembra protected do java)
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

    #def imprime(self):
    #    print(f'{self._nome} - {self.ano} - {self._likes} Likes')

#entre parenteses fica a classe mãe
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #recebe o que precisa da classe mae pra criar o objeto, para que não tenha que ficar repetindo
        super().__init__(nome, ano)
        self.duracao = duracao

    #def imprime(self):
    #    print(f'{self._nome} - {self.ano} - {self.duracao} min - {self.likes} Likes')

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

    #def imprime(self):
    #   print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes')

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #metodo que define que alguém é iteravel
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()


#list guarda ordenação
filmes_e_series = [vingadores, atlanta, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

#print(playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana:
    print(programa)

#print(f'Contem ou não contem? {demolidor in playlist_fim_de_semana}')

