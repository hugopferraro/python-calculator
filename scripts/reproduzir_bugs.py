"""Reproduz, de forma determinística, os defeitos ainda não corrigidos."""

import importlib
from unittest.mock import patch


def executar(caso, acao):
    """Executa um caso e exibe tanto o retorno normal quanto a exceção."""
    try:
        resultado = acao()
        print(f"{caso}: {resultado!r}")
    except Exception as erro:  # A exceção é justamente a evidência observada.
        print(f"{caso}: {type(erro).__name__}: {erro}")


with patch("builtins.input", return_value="0"):
    calculadora = importlib.import_module("python_calculator.Calculadora")


def executar_menu(entradas):
    with patch("builtins.input", side_effect=entradas):
        return calculadora.calculadora_cientifica()


executar("BUG-002 | fatorial(5)", lambda: calculadora.fatorial(5))
executar("BUG-003 | fatorial(-1)", lambda: calculadora.fatorial(-1))
executar("BUG-004 | logaritmo_natural(1)", lambda: calculadora.logaritmo_natural(1))
executar("BUG-005 | logaritmo_base10(100)", lambda: calculadora.logaritmo_base10(100))
executar("BUG-006 | logaritmo_base10(0)", lambda: calculadora.logaritmo_base10(0))
executar("BUG-011 | divisao(1, 0)", lambda: calculadora.divisao(1, 0))

for numero, entradas in {
    "BUG-007 | opção 10 (seno)": ["10", "n"],
    "BUG-008 | opção 11 (cosseno)": ["11", "60"],
    "BUG-009 | opção 12 (tangente)": ["12", "45"],
    "BUG-012 | entrada não numérica": ["1", "abc"],
}.items():
    executar(numero, lambda entradas=entradas: executar_menu(entradas))
