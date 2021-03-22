from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if self._valor_e_valido(valor):
            raise LanceInvalido('Saldo Insuficiente')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -=valor

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome

    def _valor_e_valido(self, valor):
        return valor>self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, descricao):
        self.maior_lance = 0.0
        self.menor_lance = 0.0
        self.descricao = descricao
        self.__lances = []

    def propoe(self, lance: Lance):
        if self.lance_e_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)


    @property
    def lances(self):
        return self.__lances[:] #devolve uma copia raza da da lista

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuario não pode dar dois lances seguidos')

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do Lance deve ser maior que o lance anterior')

    def lance_e_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))



