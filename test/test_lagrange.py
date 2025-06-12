import pytest
from src.Lagrange import Lagrange
from src.Polinomio import Polinomio, Monomio

def test_lagrange_minimo_dos_puntos():
    with pytest.raises(ValueError):
        Lagrange([(1, 2)])

def test_lagrange_pol_igual_y():
    pares = [(1, 5), (2, 5), (3, 5)]
    lagrange = Lagrange(pares)
    polinomio = lagrange.genera_polinomio()
    for x in [1, 2, 3, 4, 5]:
        assert pytest.approx(polinomio.evalua(x), rel=1e-6) == 5

def test_lagrange_polinomio_lineal():
    pares = [(1, 2), (3, 4)]
    lagrange = Lagrange(pares)
    polinomio = lagrange.genera_polinomio()
    assert pytest.approx(polinomio.evalua(1), rel=1e-6) == 2
    assert pytest.approx(polinomio.evalua(3), rel=1e-6) == 4
    assert len(polinomio.monomios) == 2
    assert any(monomio.coef > 0 and monomio.exp == 1 for monomio in polinomio.monomios)

def test_lagrange_polinomio_cuadratico():
    pares = [(1, 1), (2, 4), (3, 9)]
    lagrange = Lagrange(pares)
    polinomio = lagrange.genera_polinomio()
    for x, y in pares:
        assert pytest.approx(polinomio.evalua(x), rel=1e-6) == y

def test_lagrange_polinomio_cubico():
    pares = [(1, 1), (2, 8), (3, 27), (4, 64)]
    lagrange = Lagrange(pares)
    polinomio = lagrange.genera_polinomio()
    for x, y in pares:
        assert pytest.approx(polinomio.evalua(x), rel=1e-6) == y

def test_lagrange_no_punto_dado():
    pares = [(1, 2), (2, 3), (3, 5)]
    lagrange = Lagrange(pares)
    resultado = lagrange.evalua(4)
    assert resultado not in [2.0, 3.0, 5.0, 6.0]

def test_polinomioCorrecto():
    pares = [(1, 2), (2, 3), (3, 5)]
    lagrange = Lagrange(pares)
    resultado = lagrange.evalua(4)
    assert resultado == 8.0

def test_polinomioCorrecto2():
    pares = [(0, 3), (1, 3), (2, 5), (3, 15), (4, 39)]
    lagrange = Lagrange(pares)
    resultado = lagrange.genera_polinomio()
    assert resultado.__str__() == "+ 1.0x^3 - 2.0x^2 + 1.0x + 3.0"