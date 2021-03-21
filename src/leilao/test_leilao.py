from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao

class TestAvaliador(TestCase):

    def setUp(self): #com essa função nao será preciso chamar o metodo em cada metodo test
        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')
        self.lance_do_yuri = Lance(self.yuri, 100)
        self.lance_do_gui = Lance(self.gui,150)
        self.leilao = Leilao('celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150,self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_apenas_3_lances(self):
        vini = Usuario('Vini')

        lance_do_vini = Lance(vini, 200.00)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado,self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,self.leilao.maior_lance)

    # se o leilao nao tiver lances deve permir propor o lance

    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)
        self.assertEqual(1,len(self.leilao.lances))

    def test_deve_permirtir_propor_um_lance_se_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri,200.00)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidades_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2,quantidades_de_lances_recebidos)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui_duzentos = Lance(self.gui,200.00)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_gui_duzentos)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1,quantidade_de_lances_recebidos)
