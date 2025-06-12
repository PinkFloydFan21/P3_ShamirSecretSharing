# Proyecto3_ESCS

Repositorio del proyecto 3 de Modelado y Programación

## Integrantes

+ Oscar Yahir Hernandez Garcia // no. de cuenta: 321052847  
+ Said Apis Lorenzana // no. de cuenta: 321080550  
+ Gerardo Gael Sandoval Sandoval  // no. de cuenta: 321073259  

## Descripción

Proyecto desarrollado en python que implementa el método de interpolación de Lagrange, cifrado por AES y SHA-256 para la codificación y decodificación de archivos, utilizando también el esquema del secreto de shamir para dividir y reconstruir datos de manera segura.


## Dependencias y ejecucion del programa

Este proyecto utiliza las siguientes dependencias:

- **cffi==1.17.1**: proporciona herramientas para interactuar con código C desde Python
- **cryptography==41.0.3**: para implementar algoritmos criptográficos, como el cifrado y manejo de claves.
- **iniconfig==2.0.0**: manejo y análisis de archivos de configuración en formato .ini.
- **markdown-it-py==3.0.0**: herramienta para convertir texto en formato Markdown a HTML.
- **mdurl==0.1.2**: biblioteca para analizar y trabajar con URLs.
- **packaging==24.2**: permite analizar y manejar información sobre versiones de paquetes.
- **pluggy==1.5.0**: facilita la creación de sistemas con extensiones o complementos.
- **pycparser==2.22**: genera representaciones de código en C para bibliotecas como cryptography.
- **Pygments==2.18.0**: usado para resaltar sintaxis en fragmentos de código.
- **pytest==8.3.3**: marco de trabajo para ejecutar pruebas unitarias de forma eficiente.
- **rich==13.9.4**: mejora la salida de texto en la terminal con colores, tablas y otros elementos enriquecidos.
- **pip**: gestor de paquetes para instalar las demás dependencias.
- **distutils**: para funciones auxiliares relacionadas con compilación y archivos.

Al correr el siguiente comando, se instalaran las dependencias necesarias y se correrá el programa:

```bash
python3 install.py
```

## Para el correcto uso del programa

Para que el programa trabaje correctamente, los archivos que el usuario desee Cifrar/Descifrar deben de estar situados **exlusivamente** en la carpeta **/docs** de este mismo proyecto. También se debe asegurar correr el comando para install.py, ya que está automatizado para descargar automaticamente las dependencias.
