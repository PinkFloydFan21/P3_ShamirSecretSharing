import hashlib
import os
from .Lagrange import Lagrange
from cryptography.hazmat.primitives import padding as padding_lib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import pickle

class Decodificador:

    def __init__(self):
        pass

    def leer_fragmentos(self, archivo):

        """ 
        Lee los puntos (fragmentos) desde un archivo. 
        Args: 
            archivo (str): Nombre del archivo de fragmentos. 
        Returns: List[Tuple[int, int]]: Lista de puntos (x, y). 
        """
        puntos=[]
        ruta = os.path.join(os.path.dirname(__file__), '../docs', archivo) 

        if not os.path.exists(ruta): raise FileNotFoundError(f"Error: El archivo '{archivo}' no existe.")

        with open(ruta, 'r') as archivo: 
            for linea in archivo: 
                x, y = map(int, linea.strip().strip('()').split(',')) 
                puntos.append((x, y))     
        return puntos
    
    def reconstruir_secreto(self, archivo):

        """
        Reconstruye el secreto a partir de los 
        fragmentos utilizando la interpolación de Lagrange.
        Args:
            archivo: archivo con los puntos (List[Tuple[int, int]]): Lista de puntos (x, y).

        Returns:
            int: El secreto reconstruido.
        """
        puntos = self.leer_fragmentos(archivo)
        lagrange = Lagrange(puntos)
        secreto = lagrange.evalua(0)
        return int(round(secreto))

    def leer_archivo(self, archivo_cifrado):
        """
        Lee el contenido de un archivo cifrado.
        Args:
            archivo_cifrado (str): Nombre del archivo cifrado.
        Returns:
            bytes: Contenido del archivo en bytes.
        """
        ruta = os.path.join(os.path.dirname(__file__), f'../docs/{archivo_cifrado}')
        if os.path.exists(ruta):
            with open(ruta, 'rb') as archivo:
                return archivo.read()
        raise FileNotFoundError(f"El archivo '{archivo_cifrado}' no existe.")
    
    def guardar_archivo(self, nombre_original, data):
        """Guarda datos cifrados en un archivo con extensión `.aes`.

        Crea un directorio `resultados` si no existe y almacena el archivo cifrado.

        :param nombre_original: Nombre del archivo original (str).
        :param data: Datos cifrados a guardar (bytes).
        """
        ruta = os.path.join(os.path.dirname(__file__), '../resultados')
        cifrado = os.path.join(ruta, f"{nombre_original}") 

        if not os.path.exists(ruta):
            os.makedirs(ruta)
    
        with open(cifrado, 'wb') as archivo:
            archivo.write(data)
 
    def descifrar_archivo(self, archivo_cifrado, archivo_frg):
        """
        Descifra un archivo cifrado utilizando AES en modo CBC.

        Args:
            archivo_cifrado (str): Nombre del archivo cifrado.
            password (str): Contraseña utilizada para generar la clave de descifrado.
        Raises:
            Exception: Si el archivo no existe o si hay problemas durante el descifrado.
        """
        secreto = self.reconstruir_secreto(archivo_frg)
        datos_cifrados = self.leer_archivo(archivo_cifrado)
        clave = secreto.to_bytes(32, byteorder='big')

        iv = datos_cifrados[:16]
        datos_cifrados_puros = datos_cifrados[16:]

        descifrar = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
        decryptor = descifrar.decryptor()
        datos_padded = decryptor.update(datos_cifrados_puros) + decryptor.finalize()

        unpadder = padding_lib.PKCS7(algorithms.AES.block_size).unpadder()
        datos_descifrados = unpadder.update(datos_padded) + unpadder.finalize()
        # Deserializar el objeto Archivo
        objeto_archivo = pickle.loads(datos_descifrados)

        # Guardar el archivo original
        self.guardar_archivo(objeto_archivo.get_nombre(), objeto_archivo.get_archivo())

