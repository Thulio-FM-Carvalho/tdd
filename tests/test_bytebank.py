import pytest

from pytest import mark
from codigo.bytebank import Funcionario


#importante criar uma classe pra cada trecho de codigo que quer testar

#Given-When_Then
#Given = Dado(Contexto)...
#When = = Quando(Ação)...
#Then = Então(Desfecho)


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #Given-Contexto
        entrada = '13/03/2000'
        esperado = 24

        funcionario_teste = Funcionario('Lucas', entrada, 2000)

        #When-Ação
        resultado = funcionario_teste.idade()

        #Then-Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        #Given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 2000)

        #When
        resultado = lucas.sobrenome()

        assert resultado == esperado

    def test_quado_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #Given
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        #When
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)

        # When
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            #Given
            entrada = 1000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

            #When
            resultado = funcionario_teste.calcular_bonus()

            #Then
            assert resultado
