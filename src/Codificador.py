
import hashlib
import os
import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from .Polinomio import Monomio, Polinomio
from .Archivo import Archivo
import pickle

class Codificador:

    """
    Clase para cifrar y manejar archivos utilizando el algoritmo sha256 y AES en modo CBC.
    Attributes:
        __key (bytes): Clave de cifrado generada a partir de una contraseña.
    """

    def __init__(self):
        self.__key = None
        self.__nombreCifrado = None
        """
        Inicializa el objeto Codificador.
        Establece la clave de cifrado (__key) como `None` por defecto.
        Establece el nombre original del archivo claro (__nombre) como `None` por defecto.
        """

    def generaSha(self, password):
        self.__key = hashlib.sha256(password.encode()).digest()
        """
        Genera la clave de cifrado utilizando SHA-256.

        La clave se genera a partir de la contraseña proporcionada y se almacena
        en el atributo `__key`.

        :param password: La contraseña utilizada para generar la clave (str).
        """

    def convertir_objeto(self, nombre_archivo):
        """Lee el contenido de un archivo.

        Convierte un objeto documento en bytes.

        :param nombre_archivo: Nombre del archivo a leer (str).
        :return: El objeto en bytes, o `None` si el archivo no existe.
        """
        archivo = Archivo(nombre_archivo)
        en_bytes = pickle.dumps(archivo)
        return en_bytes

    
    def guardar_archivo(self, data):
        """Guarda datos cifrados en un archivo con extensión `.aes`.

        Crea un directorio `resultados` si no existe y almacena el archivo cifrado.

        :param nombre_original: Nombre del archivo original (str).
        :param data: Datos cifrados a guardar (bytes).
        """

        ruta = os.path.join(os.path.dirname(__file__), '../resultados')
        cifrado = os.path.join(ruta, f"{self.__nombreCifrado}.aes") 

        if not os.path.exists(ruta):
            os.makedirs(ruta)
    
        with open(cifrado, 'wb') as archivo:
            archivo.write(data)
 

    def cifrar_archivo(self, archivo_claro, nombre, password):
        """Cifra un archivo utilizando AES en modo CBC.

        Lee el archivo especificado, lo cifra utilizando la contraseña proporcionada
        y guarda el archivo cifrado con extensión `.aes`.

        :param archivo_claro: Nombre del archivo a cifrar (str).
        :param password: Contraseña utilizada para generar la clave de cifrado (str).
        :raises Exception: Si el archivo no existe.
        """
        
        self.generaSha(password)
        self.__nombreCifrado = nombre

        datos = self.convertir_objeto(archivo_claro)

        padder = PKCS7(algorithms.AES.block_size).padder()
        datos_padded = padder.update(datos) + padder.finalize()

        iv = os.urandom(16)

        cifrar = Cipher(algorithms.AES(self.__key), modes.CBC(iv), backend=default_backend())
        encryptor = cifrar.encryptor()
        datos_cifrados = encryptor.update(datos_padded) + encryptor.finalize()

        datos_con_iv = iv + datos_cifrados
        self.guardar_archivo(datos_con_iv)


    def shamir_generar_polinomio(self, grado):
        """
        Genera un polinomio para Shamir's Secret Sharing con la contraseña como término independiente.
        
        Args:
            password (str): Contraseña del usuario.
            grado (int): Grado del polinomio, que será `t-1` donde `t` es el umbral.

        Returns:
            Polinomio: Polinomio generado.
        """
        if(grado <= 0 or grado >20):
            raise Exception("El umbral del polinomio es inválido por ser cero, negativo, o muy grande.")
        
        k = int.from_bytes(self.__key, 'big')

        coeficientes = [random.randint(1, 2**256 - 1) for _ in range(1 , grado-1)]
        coeficientes.insert(0, k)  # Insertar K como término independiente

        monomios = [Monomio(coef, exp) for exp, coef in enumerate(coeficientes)]
        return Polinomio(monomios)

    def shamir_generar_puntos(self, polinomio, n):
        """
        Genera `n` puntos evaluando el polinomio en distintos valores de `x`.

        Args:
            polinomio (Polinomio): Polinomio generado.
            n (int): Número de puntos a generar.

        Returns:
            List[Tuple[int, int]]: Lista de puntos `(x, y)`.
        """
        if(n<=0):
            raise Exception("El número de puntos a generar no puede ser negativo o cero.")
        
        puntos = [(x, polinomio.evalua(x)) for x in range(1, n + 1)]
        return puntos

    def guardar_fragmentos(self, puntos):
        """
        Genera un archivo de fragmentos de Shamir con los puntos (xi, P(xi)).

        :param archivo_cifrado: Nombre del archivo cifrado (str).
        :param puntos: Lista de puntos (xi, P(xi)).
        """
        ruta = os.path.join(os.path.dirname(__file__), '../resultados')
        archivo_fragmentos = os.path.join(ruta, f"{self.__nombreCifrado}.frg")
        
        with open(archivo_fragmentos, 'w') as archivo:
            for x, y in puntos:
                archivo.write(f"({x},{y})\n")
