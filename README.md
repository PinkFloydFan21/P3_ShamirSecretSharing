# Proyecto 03, Shamir Secret Sharing

Repositorio para el Proyecto 03 de Modelado y Programación.

Prof. José Galaviz Casas.

Este proyecto implementa Shamir Secret Sharing, un método criptográfico que permite dividir un secreto en n partes, de forma que solo se necesiten t de ellas para recuperarlo.

Por ejemplo, puedes fragmentar la contraseña de un cohete nuclear en 5 partes, y requerir al menos 3 para activarlo. Con menos de 3, el secreto sigue siendo imposible de revelar.
Ideal para proteger datos sensibles y distribuir la confianza entre varios miembos.

## Integrantes

+ Oscar Yahir Hernandez Garcia  
+ Said Apis Lorenzana
+ Gerardo Gael Sandoval Sandoval  

## Descripción

Proyecto desarrollado en python que implementa el método de interpolación de Lagrange, cifrado por AES y SHA-256 para la codificación y decodificación de contraseñas, utilizando también el esquema del secreto de shamir para dividir y reconstruir datos de manera segura.

## Instalacion del Proyecto

1. **Clona el repositorio:**

   ```Bash
   git clone https://github.com/PinkFloydFan21/P3_ShamirSecretSharing.git
   cd P3_ShamirSecretSharing/
   ```
   
2. **Instala las dependencias:**
   
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
