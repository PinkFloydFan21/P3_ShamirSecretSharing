class Monomio:
    """Representa un monomio de variable x.

    Attributes:
        coef (float): El coeficiente del monomio.
        exp (int): El exponente del monomio.
    """

    def __init__(self, coef, exp):
        """Inicializa el objeto Monomio.

        Este constructor establece el coeficiente y el exponente del monomio y verifica
        que ambos valores no sean `None` mediante el metodo `precondicion`.

        Args:
            coef (float): El coeficiente del monomio.
            exp (int): El exponente del monomio.

        Precondición:
            - `coef` y `exp` no pueden ser `None`.

        Postcondición:
            - El objeto `Monomio` es creado con el coeficiente `coef` y el exponente `exp`.
        """
        self.precondicion(coef, exp)
        self.coef = coef
        self.exp = exp

    def suma(self, monomio):
        """Suma dos monomios con la misma base (exponente).

        Si los monomios tienen el mismo exponente, su coeficiente se suma. Si no, no se realiza la suma.

        Args:
            monomio (Monomio): El monomio con el que se desea realizar la suma.

        Precondición:
            - Los monomios deben tener el mismo exponente.

        Postcondición:
            - Si los monomios tienen el mismo exponente, el coeficiente del monomio actual se actualiza
              con la suma de los coeficientes. Si no tienen el mismo exponente, no ocurre ningún cambio.

        Returns:
            bool: `True` si la suma fue realizada, `False` si los monomios no tienen el mismo exponente.
        """
        if self.__eq__(monomio):
            return False
        self.coef = self.coef + monomio.coef
        return True

    def multiplicacion(self, monomio):
        """Multiplica dos monomios.

        La multiplicación de los monomios se realiza multiplicando sus coeficientes y sumando sus exponentes.

        Args:
            monomio (Monomio): El monomio con el que se desea realizar la multiplicación.

        Precondición:
            - Ninguna.

        Postcondición:
            - El coeficiente se multiplica por el coeficiente del otro monomio y el exponente se suma al
              exponente del otro monomio.

        Returns:
            bool: `True` si la multiplicación fue realizada.
        """
        if self.__eq__(monomio):
            return False
        self.coef = self.coef * monomio.coef
        self.exp = self.exp + monomio.exp
        return True

    def precondicion(self, coef, exp):
        """Verifica que el coeficiente y el exponente no sean `None`.

        Si alguno de los parámetros es `None`, lanza una excepción `ValueError`.

        Args:
            coef (float): El coeficiente del monomio.
            exp (int): El exponente del monomio.

        Precondición:
            - Ninguna.

        Postcondición:
            - Si `coef` o `exp` son `None`, se lanza una excepción `ValueError`.

        Raises:
            ValueError: Si coef o exp son `None`.
        """
        if coef is None or exp is None:
            raise ValueError("El coeficiente y el exponente no pueden ser None.")

    def __hash__(self):
        """Devuelve un valor hash para el monomio.

        Se usa el coeficiente y el exponente para generar un hash único del monomio.

        Args:
            Ninguno.

        Precondición:
            - Ninguna.

        Postcondición:
            - Se devuelve un valor hash único generado a partir del coeficiente y el exponente del monomio.

        Returns:
            int: El valor hash del monomio.
        """
        return hash((self.coef, self.exp))

    def __eq__(self, other):
        """Compara si dos monomios son iguales.

        Dos monomios son iguales si tienen el mismo coeficiente y el mismo exponente.

        Args:
            other (Monomio): Otro objeto Monomio a comparar.

        Precondición:
            - Ninguna.

        Postcondición:
            - Devuelve `True` si los monomios son iguales (coeficiente y exponente), de lo contrario `False`.

        Returns:
            bool: `True` si los monomios son iguales, `False` si no lo son.
        """
        return self.coef == other.coef and self.exp == other.exp

    def __str__(self):
        """Devuelve una representación en cadena del monomio.

        La representación en cadena sigue el formato de un monomio matemático con coeficiente y exponente.

        Args:
            Ninguno.

        Precondición:
            - Ninguna.

        Postcondición:
            - Devuelve una cadena representando el monomio en el formato estándar (ej. `2x^2`, `-3x`, `5`).

        Returns:
            str: La representación en cadena del monomio.
        """
        i = self.coef
        if self.coef < 0:
            i = abs(self.coef)
            signo = " - "
        else:
            signo = " + " if self.coef > 0 else ""
        if i == 0:
            return "0"
        elif self.exp == 0:
            return f"{signo}{i}"
        elif self.exp == 1:
            return f"{signo}{i}x"
        else:
            return f"{signo}{i}x^{self.exp}"


class Polinomio:
    """Representa un polinomio como una lista de monomios.

    Attributes:
        list_monomios (List): Lista de monomios que forman el polinomio.
    """

    def __init__(self, list_monomios):
        """Inicializa el objeto Polinomio.

        El constructor recibe una lista de monomios, verifica que todos los elementos sean monomios
        y luego simplifica la lista de monomios (eliminando términos redundantes).

        Args:
            list_monomios (list): Lista de objetos Monomio.

        Precondición:
            - La lista debe contener objetos de tipo `Monomio`.

        Postcondición:
            - El polinomio se crea y la lista de monomios se simplifica.
        """
        self.verifica(list_monomios)
        self.monomios = self.simplificar(list_monomios)

    def simplificar(self, list_monomios):
        """Simplifica una lista de monomios.

        Combina monomios con el mismo exponente, sumando sus coeficientes.

        Args:
            list_monomios (list): Lista de objetos Monomio.

        Precondición:
            - La lista contiene monomios.

        Postcondición:
            - Se retornan los monomios combinados si tienen el mismo exponente, y se eliminan aquellos con coeficiente cero.

        Returns:
            list: Lista de monomios simplificados.
        """
        monomios_dict = {}
        for monomio in list_monomios:
            if monomio.exp in monomios_dict:
                monomios_dict[monomio.exp] += monomio.coef
            else:
                monomios_dict[monomio.exp] = monomio.coef
        simplificados = []
        for exp, coef in monomios_dict.items():
            if coef != 0:
                simplificados.append(Monomio(coef, exp))
        return simplificados

    def evalua(self, x):
        """Evalúa el polinomio en un valor dado de `x`.

        Sustituye `x` en cada monomio del polinomio y devuelve la suma total.

        Args:
            x (float): El valor de `x` para evaluar el polinomio.

        Precondición:
            - `x` debe ser un número real.

        Postcondición:
            - Devuelve el resultado de la evaluación del polinomio en el valor `x`.

        Returns:
            float: El valor numérico del polinomio evaluado en `x`.
        """
        resultado = 0
        for monomio in self.monomios:
            resultado += monomio.coef * (x ** monomio.exp)
        return resultado

    def verifica(self, list_monomios):
        """Verifica que todos los elementos de la lista sean instancias de Monomio.

        Este metodo lanza una excepción `TypeError` si algún elemento en la lista no es un objeto Monomio.

        Args:
            list_monomios (list): Lista de objetos Monomio.

        Precondición:
            - Ninguna.

        Postcondición:
            - Lanza una excepción `TypeError` si algún elemento no es un `Monomio`.

        Raises:
            TypeError: Si algún elemento de la lista no es un objeto `Monomio`.
        """
        temp = Monomio(1, 0)
        for monomio in list_monomios:
            if not isinstance(monomio, Monomio):
                raise TypeError("Solo se aceptan objetos de tipo Monomio en la lista")

    def __str__(self):
        """Devuelve una representación en cadena del polinomio.

        La representación en cadena es la concatenación de los monomios, respetando los signos y los exponente.

        Args:
            Ninguno.

        Precondición:
            - Ninguna.

        Postcondición:
            - Devuelve una cadena representando el polinomio (ej. `2x^3 + 3x^2 + 4`).

        Returns:
            str: La representación en cadena del polinomio.
        """
        monomios_str = []

        for monomio in self.monomios:
            monomio_str = str(monomio)
            if monomio_str != "0":
                monomios_str.append(monomio_str)
        if not monomios_str:
            return "0"
        polinomio_str = "".join(monomios_str).strip()
        return polinomio_str
