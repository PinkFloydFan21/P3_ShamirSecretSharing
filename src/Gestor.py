from .Polinomio import Polinomio
from .Codificador import Codificador
from .Lagrange import Lagrange
from .Decodificador import Decodificador
import os
import re


import os

def verifica_archivo(ruta):
    """
    Verifica si el archivo existe en la carpeta 'docs' o, si no lo encuentra, en la carpeta 'src/resultados'.

    Args:
        ruta (str): Nombre del archivo a verificar, primero se busca en 'docs' y si no se encuentra en 'src/resultados'.

    Returns:
        bytes: Contenido del archivo si es binario.
        str: Contenido del archivo si es texto.

    Raises:
        TypeError: Si `ruta` no es una cadena válida.
        FileNotFoundError: Si el archivo no existe en ambas rutas especificadas.
        Exception: Si ocurre algún error al intentar leer el archivo.

    Precondición:
        - `ruta` debe ser una cadena que representa el nombre del archivo.

    Postcondición:
        - Si el archivo existe y es legible, se devuelve su contenido.
    """
    if not isinstance(ruta, str):
        raise TypeError("La ruta debe ser una cadena válida.")
    ruta_actual = os.path.dirname(__file__)
    ruta_docs = os.path.join(ruta_actual, '../docs', ruta)

    if not os.path.exists(ruta_docs):
        raise FileNotFoundError(f"El archivo {ruta} no fue encontrado dentro de la ruta: '../docs'.")

def verifiEntrada(entrada):
    """
    Verifica si la entrada dada cumple con la longitud máxima recomendada.

    Args:
        entrada (str): Cadena a verificar.

    Raises:
        ValueError: Si la entrada no cumple con la longitud máxima permitida.

    Precondición:
        - `entrada` debe ser una cadena no vacía.

    Postcondición:
        - No lanza excepciones si la longitud de la entrada es menor o igual a 255 caracteres.
    """
    if not isinstance(entrada, str):
        raise TypeError("La entrada debe ser una cadena.")
    if len(entrada) > 255:
        raise ValueError("La longitud de la entrada excede el límite máximo de 255 caracteres.")


def nombreCorrecto(nombre):
    """
    Verifica si el nombre proporcionado está en un formato correcto para un archivo (sin considerar la extensión).

    Args:
        nombre (str): El nombre del archivo a verificar (sin incluir la extensión).

    Raises:
        ValueError: Si el nombre no cumple con el formato válido.

    Precondición:
        - `nombre` debe ser una cadena no vacía.

    Postcondición:
        - Lanza una excepción si el nombre no cumple con las reglas válidas.
        - Si el nombre es válido, no hace nada.

    Formato válido:
        - Solo puede contener letras, números, guiones bajos (_) y guiones (-).
        - No puede empezar con un guion ni contener espacios.
        - La longitud total del nombre debe ser menor o igual a 255 caracteres.
    """
    if not isinstance(nombre, str) or not nombre:
        raise ValueError("El nombre debe ser una cadena no vacía.")
    patron = r"^[a-zA-Z0-9_-]+$"
    if len(nombre) > 25:
        raise ValueError("El texto ingresado excede el tamaño limite.")

    if not re.match(patron, nombre):
        raise ValueError(
            "El nombre de para archivos encriptados no es válido. Debe contener solo letras, números, guiones bajos (_) y guiones (-), "
            "y no debe empezar con un guion ni contener espacios."
        )


def verificar_extension_aes(nombre_archivo):
    """
    Verifica si la extensión del archivo es '.aes'.

    Args:
        nombre_archivo (str): Nombre del archivo a verificar.

    Raises:
        ValueError: Si el archivo no tiene la extensión '.aes'.

    Precondición:
        - `nombre_archivo` debe ser una cadena no vacía que incluya una extensión.

    Postcondición:
        - Lanza una excepción si la extensión del archivo no es '.aes'.
    """
    if not nombre_archivo.endswith('.aes'):
        raise ValueError(f"El archivo '{nombre_archivo}' no tiene la extensión requerida '.aes' . ")

def verificar_extension_frg(nombre_archivo):
    """
    Verifica si la extensión del archivo es '.frg'.

    Args:
        nombre_archivo (str): Nombre del archivo a verificar.

    Raises:
         ValueError: Si el archivo no tiene la extensión '.frg'.

    Precondición:
        - `nombre_archivo` debe ser una cadena no vacía que incluya una extensión.

    Postcondición:
        - Lanza una excepción si la extensión del archivo no es '.frg'.
    """
    if not nombre_archivo.endswith('.frg'):
        raise ValueError(f"El archivo '{nombre_archivo}' no tiene la extensión requerida '.frg'.")



def rangoValido(n, t):
    """
    Verifica que los números ingresados sean enteros y cumplan con un rango válido.

    Esta función asegura que los valores `n` (número de evaluaciones) y `t` (número mínimo de puntos) sean enteros
    y que cumplan con la condición de rango: `2 < t <= n`.

    Args:
        n (int): Número de evaluaciones.
        t (int): Número mínimo de puntos.

    Raises:
        ValueError: Si `n` o `t` no son números enteros válidos.
        ValueError: Si `t` no cumple la condición `2 < t <= n`.

    Precondición:
        - `n` y `t` deben ser valores convertibles a enteros.
        - Debe cumplirse la condición `2 < t <= n`.

    Postcondición:
        - No lanza excepciones si los valores son válidos.
    """
    try:
        n = int(n)
        t = int(t)
    except ValueError:
        raise ValueError(f"No ingresaste un número entero correcto: n={n}, t={t}")
    if not (2 < t <= n):
        raise ValueError(f"No se cumple que 2 < t <= n para los valores n={n}, t={t}")


def validar_tamano(entrada):
    """
    Verifica que la entrada tenga un tamaño mayor a 5 y menor a 32 caracteres.

    Args:
        entrada (str): La cadena a verificar.

    Raises:
        TypeError: Si la entrada no es una cadena.
        ValueError: Si la longitud de la entrada no cumple con el rango requerido.

    Precondición:
        - `entrada` debe ser una cadena no vacía.

    Postcondición:
        - No lanza excepciones si la longitud de la entrada está en el rango [6, 31].
    """
    if not isinstance(entrada, str):
        raise TypeError("La entrada debe ser una cadena.")

    longitud = len(entrada)
    if not (5 < longitud < 32):
        raise ValueError(f"La longitud de la contraseña debe estar entre 6 y 31 caracteres. Longitud actual: {longitud}")

def gestiona_C(datos):
    """
    Realiza la gestión de codificación utilizando el esquema de Shamir.

    Args:
        datos (list): Lista que contiene:
            - datos[0] (str): Nombre del archivo de salida.
            - datos[1] (int): Número de evaluaciones (n).
            - datos[2] (int): Número mínimo de puntos requeridos (t).
            - datos[3] (str): Nombre del archivo a cifrar.
            - datos[4] (str): Contraseña para cifrar el archivo.
    """
    nombre = datos[0]
    n = int(datos[1])
    t = int(datos[2])
    archivo = datos[3]
    contrasena = datos[4]
    cd = Codificador()
    cd.cifrar_archivo(archivo, nombre, contrasena)
    pol = cd.shamir_generar_polinomio(t)
    puntos = cd.shamir_generar_puntos(pol,n)
    cd.guardar_fragmentos(puntos)

def gestiona_D(datos):
    """
    Realiza la gestión de decodificación de un archivo cifrado.

    Args:
        datos (list): Lista que contiene:
            - datos[0] (str): Nombre del archivo cifrado.
            - datos[1] (list): Lista de puntos de evaluación para descifrar.
    """
    cifrado = datos[0]
    evalua = datos[1]
    dc = Decodificador()
    dc.descifrar_archivo(cifrado, evalua)




