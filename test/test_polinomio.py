import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.Polinomio import Polinomio, Monomio

def test1_polinomio():
    polinomio = Polinomio([Monomio(3, 2), Monomio(3, 0), Monomio(3, 3)])
    assert "+ 3x^2 + 3 + 3x^3" == str(polinomio)

def test2_polinomio():
    polinomio = Polinomio([Monomio(3.2, 2), Monomio(3, 0), Monomio(3, 3)])
    assert "+ 3.2x^2 + 3 + 3x^3" == str(polinomio)

def test3_polinomio_simplificacion():
    polinomio = Polinomio([Monomio(3, 2), Monomio(3, 2), Monomio(5, 0), Monomio(-5, 0)])
    assert "+ 6x^2" == str(polinomio)

def test4_polinomio_exponente_0():
    polinomio = Polinomio([Monomio(5, 0), Monomio(3, 0)])
    assert "+ 8" == str(polinomio)

def test5_polinomio_simplificacion_monomios_0():
    polinomio = Polinomio([Monomio(0, 2), Monomio(3, 1), Monomio(0, 0)])
    assert "+ 3x" == str(polinomio)

def test6_polinomio_monomio_con_coef_negativo():
    polinomio = Polinomio([Monomio(-3, 2), Monomio(3, 0), Monomio(2, 1)])
    assert "- 3x^2 + 3 + 2x" == str(polinomio)

def test7_polinomio_suma_monomios():
    polinomio = Polinomio([Monomio(2, 2), Monomio(3, 2), Monomio(-5, 2)])
    assert "0" == str(polinomio)

def test8_polinomio_multiplicacion_monomios():
    monomio_multiplicado = Monomio(2, 2)
    monomio_multiplicado.multiplicacion(Monomio(3, 3))
    assert " + 6x^5" == str(monomio_multiplicado)

def test9_polinomio_con_mon_0():
    polinomio = Polinomio([Monomio(0, 0), Monomio(4, 1)])
    assert "+ 4x" == str(polinomio)

def test10_polinomio_exponente_1():
    polinomio = Polinomio([Monomio(2, 1), Monomio(3, 1)])
    assert "+ 5x" == str(polinomio)

def test1_evalua():
    polinomio = Polinomio([Monomio(3, 2), Monomio(3, 0), Monomio(3, 3)])
    assert 9 == polinomio.evalua(1)

def test2_evalua_x_0():
    polinomio = Polinomio([Monomio(5, 2), Monomio(3, 1), Monomio(2, 0)])
    assert 2 == polinomio.evalua(0)

def test3_evalua_x_negativo():
    polinomio = Polinomio([Monomio(3, 2), Monomio(3, 0), Monomio(2, 1)])
    assert 11 == polinomio.evalua(-2)

def test4_evalua_polynomial_simple():
    polinomio = Polinomio([Monomio(5, 3)])
    assert 5 == polinomio.evalua(1)

def test5_evalua_polynomial_zero_coefficients():
    polinomio = Polinomio([Monomio(0, 3), Monomio(0, 1), Monomio(0, 0)])
    assert 0 == polinomio.evalua(2)

def test6_evalua_x_1_polinomio_con_exponentes_negativos():
    polinomio = Polinomio([Monomio(2, -2), Monomio(1, -1)])
    assert 3 == polinomio.evalua(1)

def test7_evalua_monomio_0_en_polynomial():
    polinomio = Polinomio([Monomio(0, 3), Monomio(1, 2), Monomio(4, 0)])
    assert 8 == polinomio.evalua(2)

def test8_evalua_polynomial_with_large_exponent():
    polinomio = Polinomio([Monomio(1, 100), Monomio(1, 2), Monomio(1, 1)])
    assert 3 == polinomio.evalua(1)

def test9_evalua_polynomial_with_negative_exponent_and_x_negativo():
    polinomio = Polinomio([Monomio(2, -1), Monomio(3, -2)])
    assert 1 == polinomio.evalua(-1)

def test10_evalua_polynomial_with_complex_values():
    polinomio = Polinomio([Monomio(2.5, 2), Monomio(3.1, 1), Monomio(4.5, 0)])
    assert 27.875 == polinomio.evalua(2.5)