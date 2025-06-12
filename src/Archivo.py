import os

class Archivo:
    def __init__(self, nombre_archivo):
        """
        Inicializa un objeto Documento cargando el contenido del archivo dado.

        :param nombre_archivo: Nombre del archivo a cargar.
        """
        self.__nombre = nombre_archivo
        self.__archivo = self.archivoBytes(self.__nombre)

    def get_nombre(self):
        """Devuelve el nombre del archivo."""
        return self.__nombre

    def get_archivo(self):
        """Devuelve el contenido del archivo en bytes."""
        return self.__archivo

    def archivoBytes(self, archivo):
        """
        Verifica y devuelve el contenido de un archivo en bytes.

        :param archivo: Nombre del archivo a verificar y leer.
        :return: Contenido del archivo en bytes.
        :raises FileNotFoundError: Si el archivo no existe.
        :raises IOError: Si ocurre un error al leer el archivo.
        """
        self.verifica_archivo(archivo)
        return self.leer_archivo(archivo)

    def leer_archivo(self, nombre_archivo):
        """
        Lee el contenido de un archivo binario desde el directorio `../docs`.

        :param nombre_archivo: Nombre del archivo a leer.
        :return: Contenido del archivo en bytes.
        :raises FileNotFoundError: Si el archivo no existe.
        :raises IOError: Si ocurre un error al leer el archivo.
        """
        # Construir la ruta del archivo
        ruta = os.path.join(os.path.dirname(__file__), '../docs', nombre_archivo)

        # Verificar si el archivo existe
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"El archivo '{nombre_archivo}' no existe en la ruta: {ruta}")

        # Leer el archivo en modo binario
        try:
            with open(ruta, 'rb') as archivo:
                return archivo.read()
        except IOError as e:
            raise IOError(f"Error al leer el archivo '{nombre_archivo}': {e}")


    def verifica_archivo(self, ruta):
        """
        Verifica si el archivo existe dentro de la carpeta 'docs'.

        Args:
            ruta (str): Nombre del archivo a verificar dentro de la carpeta 'docs'.

        Returns:
            str: Contenido del archivo si este existe y se puede leer.

        Raises:
            TypeError: Si `ruta` no es una cadena válida.
            FileNotFoundError: Si el archivo no existe en la carpeta 'docs'.
            Exception: Si ocurre algún error al intentar leer el archivo.

        Precondición:
            - `ruta` debe ser una cadena que representa el nombre del archivo.

        Postcondición:
            - Si el archivo existe y es legible, se devuelve su contenido.
        """
        if not isinstance(ruta, str):
            raise TypeError("La ruta debe ser una cadena válida.")
        ruta_actual = os.path.dirname(__file__)
        ruta_completa = os.path.join(ruta_actual, '../docs', ruta)
        try:
            with open(ruta_completa, 'r') as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo en la carpeta 'docs': {ruta_completa}")
        except Exception as e:
            raise Exception(f"Ocurrió un error al leer el archivo: {e}")