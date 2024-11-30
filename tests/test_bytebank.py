import pytest

from pytest import mark
from codigo.bytebank import Funcionario

"""
Classe responsável por realizar testes unitários para a classe Funcionario do módulo codigo.bytebank. Essa classe
contém vários métodos que testam diferentes cenários e comprotamentos da classe Funcionário.

Usando aqui o padrão de estruturação Given-When-Then que ajuda a tornar os testes mais claros e faceis de entender.
Given = Dado(Contexto)...
When = = Quando(Ação)...
Then = Então(Desfecho ou resultado)
"""


class TestClass:
    # Testa se a idade calculada está correta
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given(contexto)
        entrada = '13/03/2000'
        esperado = 24

        funcionario_teste = Funcionario('Lucas', entrada, 2000)

        # When(ação)
        resultado = funcionario_teste.idade()

        # Then(desfecho)
        assert resultado == esperado

    # Testa se o sobrenome está sendo extraído corretamente
    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        # Given(contexto)
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 2000)

        # When(ação)
        resultado = lucas.sobrenome()

        # Then(desfecho)
        assert resultado == esperado

    # Testa se o decréscimo do salário está sendo aplicado corretamente
    def test_quado_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given(contexto)
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        # When(ação)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        # Then(desfecho)
        assert resultado == esperado

    # Testa se o calculo do bonbus está sendo realizado corretamente
    # Criando a etiqueta @mark.calcular_bonus específica para executar apenas os testes relacionados ao calculo do bonus
    # Para executar, digite o comando pytest -m calcular_bonus
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given(contexo)
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)

        # When(ação)
        resultado = funcionario_teste.calcular_bonus()

        # Then(desfecho)
        assert resultado == esperado

    # Testa se o calculo do bonbus está sendo realizado corretamente
    # Criando a etiqueta @mark.calcular_bonus específica para executar apenas os testes relacionados ao calculo do bonus
    # Para executar, digite o comando pytest -m calcular_bonus
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Given(contexo)
            entrada = 1000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

            # When(acao)
            resultado = funcionario_teste.calcular_bonus()

            # Then(desfecho)
            assert resultado
