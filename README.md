# Proyecto 03, Shamir Secret Sharing

Repositorio para el Proyecto 03 de Modelado y Programación.

Prof. José Galaviz Casas.

Este proyecto consiste en la implementación del Shamir Secret Sharing, quehace posible que un sólo dato pueda ser ocultado de manera que, a partir de él, se generan n diferentes datos y que con
al menos t ≤ n cualesquiera de ellos sea posible recuperar el dato original.

## Integrantes

+ Oscar Yahir Hernandez Garcia  
+ Said Apis Lorenzana
+ Gerardo Gael Sandoval Sandoval  

## Descripción

Proyecto desarrollado en python que implementa el método de interpolación de Lagrange, cifrado por AES y SHA-256 para la codificación y decodificación de archivos, utilizando también el esquema del secreto de shamir para dividir y reconstruir datos de manera segura.


## Dependencias y ejecucion del programa

Este proyecto utiliza las siguientes dependencias:

- **cffi==1.17.1**
- **cryptography==41.0.3**
- **iniconfig==2.0.0**
- **markdown-it-py==3.0.0**
- **mdurl==0.1.2**
- **packaging==24.2**
- **pluggy==1.5.0**
- **pycparser==2.22**
- **Pygments==2.18.0**
- **pytest==8.3.3**
- **rich==13.9.4**
- **pip**
- **distutils**

Al correr el siguiente comando, se instalaran las dependencias necesarias y se correrá el programa:

```bash
python3 install.py
```

## Para el correcto uso del programa

Para que el programa trabaje correctamente, los archivos que el usuario desee Cifrar/Descifrar deben de estar situados **exlusivamente** en la carpeta **/docs** de este mismo proyecto. También se debe asegurar correr el comando para install.py, ya que está automatizado para descargar automaticamente las dependencias.
