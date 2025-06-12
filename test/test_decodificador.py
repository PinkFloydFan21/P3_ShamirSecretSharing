import os
import hashlib
import pytest
from unittest.mock import patch, mock_open
from src.Decodificador import Decodificador
from src.Codificador import Codificador

def test_leer_fragmentos_existente():
    decodificador = Decodificador()
    archivo = "fragmentos.txt"
    contenido = "(1,2)\n(3,4)\n(5,6)"
    
    ruta = os.path.join(os.path.dirname(__file__), f"../docs/{archivo}")
    with open(ruta, "w") as f:
        f.write(contenido)

    puntos = decodificador.leer_fragmentos(archivo)

    assert puntos == [(1, 2), (3, 4), (5, 6)]
    os.remove(ruta)

def test_leer_fragmentos_no_existente():
    decodificador = Decodificador()
    archivo = "no_existe.txt"
    
    with pytest.raises(FileNotFoundError):
        decodificador.leer_fragmentos(archivo)

def test_reconstruir_secreto_valido():
    decodificador = Decodificador()
    archivo = "fragmentos_secreto.frg"
    contenido = "(1,5)\n(2,15)\n(3,35)"
    ruta = os.path.join(os.path.dirname(__file__), f"../docs/{archivo}")

    with open(ruta, "w") as f:
        f.write(contenido)

    secreto = decodificador.reconstruir_secreto(archivo)
    assert secreto == 5, f"Se esperaba el secreto 5, pero se obtuvo {secreto}"

def test_reconstruir_secreto_con_ceros():
    decodificador = Decodificador()
    archivo = "fragmentos_ceros.frg"
    contenido = "(0,0)\n(1,0)\n(2,0)"
    ruta = os.path.join(os.path.dirname(__file__), f"../docs/{archivo}")

    with open(ruta, "w") as f:
        f.write(contenido)

    secreto = decodificador.reconstruir_secreto(archivo)
    assert secreto == 0, f"Se esperaba el secreto 0, pero se obtuvo {secreto}"

def test_reconstruir_secreto_caso_3():

    decodificador = Decodificador()
    archivo = "fragmentos_caso3.frg"
    contenido = "(1,5)\n(2,15)\n(3,43)"
    ruta = os.path.join(os.path.dirname(__file__), f"../docs/{archivo}")

    with open(ruta, "w") as f:
        f.write(contenido)

    secreto = decodificador.reconstruir_secreto(archivo)
    assert secreto == 13, f"Se esperaba el secreto 13, pero se obtuvo {secreto}"


def test_leer_archivo_existente():
    decodificador = Decodificador()
    archivo = "archivo_cifrado.aes"
    contenido = b"Datos cifrados"

    ruta = os.path.join(os.path.dirname(__file__), f"../docs/{archivo}")
    with open(ruta, "wb") as f:
        f.write(contenido)

    resultado = decodificador.leer_archivo(archivo)

    assert resultado == contenido
    os.remove(ruta)

def test_leer_archivo_no_existente():
    decodificador = Decodificador()
    archivo = "archivo_inexistente.aes"

    with pytest.raises(FileNotFoundError):
        decodificador.leer_archivo(archivo)

def test_guardar_archivo():
    decodificador = Decodificador()
    archivo = "test_output.aes"
    data = b"Contenido del archivo"

    decodificador.guardar_archivo(archivo, data)
    
    ruta = os.path.join(os.path.dirname(__file__), f"../resultados/{archivo}")
    assert os.path.exists(ruta)

    with open(ruta, "rb") as f:
        contenido_leido = f.read()
    assert contenido_leido == data

    os.remove(ruta)
