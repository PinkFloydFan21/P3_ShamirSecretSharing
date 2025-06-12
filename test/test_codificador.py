
import hashlib
import os
import pytest
from src.Codificador import Codificador
from src.Polinomio import Polinomio

def test_generaSha1():
    codificador = Codificador()
    password = "contraseña"
    codificador.generaSha(password)
    expected_key = hashlib.sha256(password.encode()).digest()
    assert codificador._Codificador__key is not None
    assert isinstance(codificador._Codificador__key, bytes)
    assert codificador._Codificador__key == expected_key

def test_generaSha2():
    codificador = Codificador()
    password = "key"
    codificador.generaSha(password)
    expected_key = hashlib.sha256(password.encode()).digest()
    assert codificador._Codificador__key is not None
    assert isinstance(codificador._Codificador__key, bytes)
    assert codificador._Codificador__key == expected_key

def test_leer_archivo_existente():
    codificador = Codificador()
    archivo_claro = "archivo_existente.txt"
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../docs/{archivo_claro}"))

    with open(ruta, "wb") as archivo:
        archivo.write(b"Este es un archivo de prueba.")

    contenido = codificador.convertir_objeto(ruta)

    assert contenido is not None
    assert isinstance(contenido, bytes)
    assert b"Este es un archivo de prueba." in contenido

    os.remove(ruta)

def test_leer_archivo_no_existente():
    codificador = Codificador()
    with pytest.raises(Exception):
        codificador.convertir_objeto("archivo_no_existente.txt")

def test_cifrarArchivo1():
    codificador = Codificador()
    archivo_claro = "Test1.txt"
    password = "contrasena"

    ruta_archivo_claro = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../docs/{archivo_claro}"))

    with open(ruta_archivo_claro, "wb") as archivo:
        archivo.write(b"El veloz murcielago hindu comia kiwi.")

    codificador.cifrar_archivo(ruta_archivo_claro, "Carrie", password)
    cifrado_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resultados/Carrie.aes"))
    assert os.path.exists(cifrado_file)

    os.remove(ruta_archivo_claro)
    os.remove(cifrado_file)

def test_cifrarArchivo2():
    codificador = Codificador()
    archivo_claro = "Test2.txt"
    password = "contrasena"

    ruta_archivo_claro = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../docs/{archivo_claro}"))

    with open(ruta_archivo_claro, "wb") as archivo:
        archivo.write(b"Sometimes it seems my blood spurts out in gobs")

    codificador.cifrar_archivo(ruta_archivo_claro, "PapuZen", password)
    cifrado_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resultados/PapuZen.aes"))
    assert os.path.exists(cifrado_file)

    os.remove(ruta_archivo_claro)
    os.remove(cifrado_file)

def test_cifrar_archivo_no_existente():
    codificador = Codificador()
    with pytest.raises(Exception):
        codificador.cifrar_archivo("archivo_inexistente.txt", "contrasena")

def test_cifrarArchivo3():
    codificador = Codificador()
    archivo_claro = "Test3.txt"
    password = "contrasena_segura"

    ruta_archivo_claro = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../docs/{archivo_claro}"))

    with open(ruta_archivo_claro, "wb") as archivo:
        archivo.write(b"Contenido de prueba para el archivo claro.")

    codificador.cifrar_archivo(ruta_archivo_claro, "Boris", password)
    cifrado_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resultados/Boris.aes"))
    assert os.path.exists(cifrado_file)

    os.remove(ruta_archivo_claro)
    os.remove(cifrado_file)

def test_shamir_generar_polinomio_valido():
    codificador = Codificador()
    password = "segura123"
    codificador.generaSha(password)

    grado = 3
    polinomio = codificador.shamir_generar_polinomio(grado)
    
    assert isinstance(polinomio, Polinomio)
    assert len(polinomio.monomios) == grado-1
    assert polinomio.monomios[0].coef == int.from_bytes(codificador._Codificador__key, 'big')

def test_shamir_generar_polinomio_grado_invalido():
    codificador = Codificador()
    password = "segura123"
    codificador.generaSha(password)

    with pytest.raises(Exception, match="El umbral del polinomio es inválido por ser cero, negativo, o muy grande."):
        codificador.shamir_generar_polinomio(0)

    with pytest.raises(Exception, match="El umbral del polinomio es inválido por ser cero, negativo, o muy grande."):
        codificador.shamir_generar_polinomio(25)

def test_shamir_generar_puntos():
    codificador = Codificador()
    password = "segura123"
    codificador.generaSha(password)

    grado = 3
    polinomio = codificador.shamir_generar_polinomio(grado)

    n = 5
    puntos = codificador.shamir_generar_puntos(polinomio, n)
    
    assert len(puntos) == n
    for x, y in puntos:
        assert isinstance(x, int)
        assert isinstance(y, int)

def test_shamir_generar_puntos_numero_invalido():
    codificador = Codificador()
    password = "segura123"
    codificador.generaSha(password)

    grado = 3
    polinomio = codificador.shamir_generar_polinomio(grado)

    with pytest.raises(Exception, match="El número de puntos a generar no puede ser negativo o cero."):
        codificador.shamir_generar_puntos(polinomio, 0)

def test_guardar_fragmentos():
    codificador = Codificador()
    puntos = [(1, 12345), (2, 67890), (3, 11121), (4, 54321)]

    nombre_archivo = "TestFragmentos"
    codificador._Codificador__nombreCifrado = nombre_archivo  # Simular cifrado previo

    codificador.guardar_fragmentos(puntos)

    ruta_fragmentos = os.path.join(os.path.dirname(__file__), f"../resultados/{nombre_archivo}.frg")
    assert os.path.exists(ruta_fragmentos)

    with open(ruta_fragmentos, 'r') as archivo:
        lineas = archivo.readlines()
        assert len(lineas) == len(puntos)
        for i, (x, y) in enumerate(puntos):
            assert lineas[i].strip() == f"({x},{y})"

    os.remove(ruta_fragmentos)