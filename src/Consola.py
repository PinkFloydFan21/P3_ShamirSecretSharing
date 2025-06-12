from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from .Gestor import verifica_archivo, validar_tamano, nombreCorrecto, rangoValido, gestiona_C, gestiona_D, verificar_extension_aes, verificar_extension_frg

console = Console()

def mostrar_titulo():
    """
    Muestra el título principal del programa con formato enriquecido usando Rich.
    """
    panel = Panel(
        Text("Bienvenid@", style="bold yellow"),
        title="Shamir Secret Sharing",
        subtitle="Encryption and Decryption",
        border_style="green",
        padding=(1, 2),
        expand=True
    )
    console.print(panel)

def mostrar_menu(titulo, opciones):
    """
    Muestra un menú interactivo en la consola con formato Rich.

    Args:
        titulo (str): El título del menú.
        opciones (list): Lista de opciones del menú.
    """
    menu_text = "\n".join(
        [f"[bold yellow][{i}][/bold yellow] [cyan]- {opcion}[/]" for i, opcion in enumerate(opciones, start=1)]
    )
    menu_text += "\n[bold yellow][0][/bold yellow] [red]- Salir[/]"
    panel = Panel(
        menu_text,
        title=f"[bold white]{titulo}[/]",
        subtitle="[italic yellow]Elige una opción",
        border_style="blue",
        style="bold green",
        expand=True
    )
    console.print(panel)

def ejecutar_opcion(opciones, seleccionado):
    """
    Ejecuta una acción según la opción seleccionada.

    Args:
        opciones (list): Lista de funciones asociadas a las opciones.
        seleccionado (str): Entrada del usuario.

    Returns:
        str: "salir" si el usuario elige salir.
    """
    try:
        selec = int(seleccionado)
        if selec == 0:
            return "salir"
        if 1 <= selec <= len(opciones):
            opciones[selec - 1]()
        else:
            console.print("[bold red]Opción no válida. Intenta nuevamente.[/]")
    except ValueError:
        console.print("[bold red]Entrada inválida. Por favor, ingresa un número.[/]")

def entrada_cifrar():
    """
    Flujo de entrada para cifrar un archivo.
    """
    while True:
        try:
            datos = obtener_datos_cifrado()
            gestiona_C(datos)
        except Exception as e:
            console.print(f"[bold red]Error: {e}\n", style="bold yellow")
            console.print("[bold green]Intente de nuevo.")
        else:
            console.print(
                f"[bold magenta]✔ Archivo cifrado guardado correctamente en:\n"
                f"[bold yellow] - {datos[0]}.aes[/] y [bold yellow]{datos[0]}.frg[/] en la carpeta [bold green]../resultados/[/]",
                style="bold yellow"
            )
            break

def obtener_datos_cifrado():
    """
    Obtiene los datos necesarios para el proceso de cifrado.

    Returns:
        list: Lista con los datos proporcionados por el usuario.
    """
    console.print("[bold green]✔ Ingrese el nombre del archivo a encriptar:[/]")
    documento = Prompt.ask("Debe estar en la carpeta [bold cyan]/docs[/] de este proyecto e incluir la extensión (ej: archivo.txt)")
    verifica_archivo(documento)
    contrasena = getpass("Ingrese la contraseña para cifrar su documento: ")
    validar_tamano(contrasena)
    archivo = Prompt.ask("[bold green]✔ Ingrese el nombre que tendrán el archivo cifrado y el archivo de fragmentos:[/]")
    nombreCorrecto(archivo)
    console.print("[bold green]✔ Para la siguiente sección, recuerda: 2 < t <= n[/]")
    n = Prompt.ask("Ingrese el número de partes en las que dividir la contraseña([bold cyan]n[/]):", default="3")
    t = Prompt.ask("Ingrese el número mínimo de partes necesarias para reconstruir la contraseña ([bold cyan]t[/]):", default="2")
    rangoValido(n, t)
    return [archivo, int(n), int(t), documento, contrasena]

def entrada_descifrar():
    """
    Flujo de entrada para descifrar un archivo.
    """
    while True:
        try:
            datos = obtener_datos_descifrado()
            gestiona_D(datos)
        except Exception as e:
            console.print(f"[bold red]Error: {e}\n", style="bold yellow")
            console.print("[bold green]Intente de nuevo.")
        else:
            console.print(
                "[bold magenta]✔ Archivo descifrado correctamente.\n"
                "[bold green]Guardado en la carpeta: [bold yellow]../resultados[/]",
                style="bold yellow"
            )
            break

def obtener_datos_descifrado():
    """
    Obtiene los datos necesarios para el proceso de descifrado.

    Returns:
        list: Lista con los datos proporcionados por el usuario.
    """
    console.print("[bold green]✔ Ingrese el nombre del archivo a descifrar:[/]")
    descifrar = Prompt.ask("Archivo cifrado (ej: archivo.aes):")
    verificar_extension_aes(descifrar)
    verifica_archivo(descifrar)
    evaluacion = Prompt.ask("Archivo con las partes de la contraseña (ej: archivo.frg):")
    verificar_extension_frg(evaluacion)
    verifica_archivo(evaluacion)
    return [descifrar, evaluacion]

def mostrar_consola():
    """
    Función principal que controla el flujo del menú y la interacción con el usuario.
    """
    mostrar_titulo()
    opciones = ["Cifrar Archivo", "Descifrar Archivo"]
    acciones = [
        lambda: entrada_cifrar(),
        lambda: entrada_descifrar(),
    ]

    while True:
        mostrar_menu("Menú Principal", opciones)
        seleccion = Prompt.ask("[bold cyan]Selecciona una opción")
        if ejecutar_opcion(acciones, seleccion) == "salir":
            console.print("[bold yellow]¡Hasta luego![/]")
            break

