from unittest.mock import patch

import numpy as np
import pytest


# O código fornecido inicia o menu durante a importação. A entrada "0" permite
# importar as funções sem bloquear a coleta dos testes. Esse comportamento é
# registrado separadamente como BUG-010.
with patch("builtins.input", return_value="0"):
    from python_calculator.Calculadora import (
        adicao,
        divisao,
        multiplicacao,
        potencia,
        raiz_quadrada,
        subtracao,
    )


@pytest.mark.parametrize(
    ("x", "y", "esperado"),
    [
        (2, 3, 5),
        (-2, 3, 1),
        (1.5, 2.25, 3.75),
    ],
)
def test_adicao_retorna_a_soma_dos_operandos(x, y, esperado):
    """Teste TDD do BUG-001: a adição deve somar cada operando uma vez."""
    assert adicao(x, y) == pytest.approx(esperado)


@pytest.mark.parametrize(
    ("operacao", "argumentos", "esperado"),
    [
        (subtracao, (7, 4), 3),
        (multiplicacao, (3, 4), 12),
        (divisao, (8, 2), 4),
        (potencia, (2, 3), 8),
        (raiz_quadrada, (9,), 3),
    ],
)
def test_operacoes_existentes_continuam_funcionando(operacao, argumentos, esperado):
    """Teste de regressão das operações não alteradas durante a correção."""
    assert operacao(*argumentos) == pytest.approx(esperado)


def test_raiz_quadrada_negativa_mantem_mensagem_de_erro():
    assert raiz_quadrada(-1) == "Erro: Raiz quadrada de número negativo"


def test_multiplicacao_funciona_com_arrays_numpy():
    resultado = multiplicacao(np.array([2, 3]), np.array([4, 5]))
    np.testing.assert_array_equal(resultado, np.array([8, 15]))
