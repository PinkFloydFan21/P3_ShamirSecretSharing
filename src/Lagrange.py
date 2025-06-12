from .Polinomio import Monomio, Polinomio


class Lagrange:
    """
    Clase para construir y evaluar el polinomio de Lagrange.

    Atributos:
        pares (list): Lista de pares ordenados (x, y).
    """

    def __init__(self, pares):
        """
        Inicializa el polinomio de Lagrange con una lista de pares ordenados.

        Args:
            pares (list): Lista de pares ordenados (x, y) utilizada para construir el polinomio de Lagrange.

        Precondición:
            - `pares` debe ser una lista de al menos dos pares (x, y).

        Postcondición:
            - El polinomio de Lagrange es inicializado y almacenado en el atributo `pares`.

        Raises:
            ValueError: Si no hay al menos dos puntos en la lista de pares.
        """
        if len(pares) < 2:
            raise ValueError("Se necesitan al menos dos pares ordenados para construir el polinomio de Lagrange.")
        self.pares = pares

    def calcula_Li(self, i, x=None):
        """
        Calcula el polinomio base L_i(x) o su valor evaluado si x se proporciona.

        Args:
            i (int): Índice del punto (x_i, y_i).
            x (float, optional): El valor en el que se evalúa el polinomio. Si es None, retorna L_i como Polinomio.

        Precondición:
            - `i` debe ser un índice válido en la lista de pares.
            - La lista `pares` debe estar inicializada.

        Postcondición:
            - Si `x` es proporcionado, se retorna el valor de L_i(x), de lo contrario, se retorna el polinomio L_i como un objeto `Polinomio`.

        Returns:
            Polinomio o float: El polinomio base L_i o su valor evaluado en `x`.
        """
        xi, _ = self.pares[i]
        numerador = [Monomio(1, 0)]
        denominador = 1

        for j, (xj, _) in enumerate(self.pares):
            if i != j:
                termino = [Monomio(1, 1), Monomio(-xj, 0)]
                numerador = self._multiplica_monomios(numerador, termino)
                denominador *= (xi - xj)

        Li = Polinomio([Monomio(m.coef // denominador, m.exp) for m in numerador])
        return Li.evalua(x) if x is not None else Li

    def evalua(self, x):
        """
        Evalúa el polinomio de Lagrange en un valor dado de x.

        Args:
            x (float): El valor en el que se evalúa el polinomio.

        Precondición:
            - `x` debe ser un valor numérico para evaluar el polinomio.

        Postcondición:
            - El valor del polinomio evaluado en `x` es retornado.

        Returns:
            float: El valor del polinomio evaluado en `x`.
        """
        resultado = 0
        for i, (_, yi) in enumerate(self.pares):
            resultado += yi * self.calcula_Li(i, x)
        return resultado

    def genera_polinomio(self):
        """
        Genera el polinomio completo de Lagrange como objeto Polinomio.

        Precondición:
            - La lista de pares ordenados debe estar inicializada.

        Postcondición:
            - El polinomio completo de Lagrange es generado y retornado como un objeto `Polinomio`.

        Returns:
            Polinomio: El polinomio de Lagrange completo.
        """
        terminos = []
        for i, (_, yi) in enumerate(self.pares):
            Li = self.calcula_Li(i)
            terminos.extend([Monomio(m.coef * yi, m.exp) for m in Li.monomios])

        return Polinomio(terminos)

    def _multiplica_monomios(self, m1, m2):
        """
        Multiplica dos listas de monomios.

        Args:
            m1 (list): Lista de Monomios.
            m2 (list): Lista de Monomios.

        Precondición:
            - `m1` y `m2` deben ser listas de objetos `Monomio`.

        Postcondición:
            - Se retorna una lista de monomios resultantes de la multiplicación de las dos listas.

        Returns:
            Polinomio: El polinomio resultante de la multiplicación de los monomios.
        """
        resultado = []
        for monomio1 in m1:
            for monomio2 in m2:
                nuevo_monomio = Monomio(monomio1.coef * monomio2.coef, monomio1.exp + monomio2.exp)
                resultado.append(nuevo_monomio)

        return Polinomio(resultado).simplificar(resultado)
