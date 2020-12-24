# 🌌 Mundo Desconocido

Mundo Desconocido se trata de un blog con temática sobre el **universo y el espacio**, desarrollado con Django y MongoDB para la asignatura de Ingeniería de Software 2.

## Instalación
Para iniciar el programa se puede realizar de dos formas:
1. **Global**: Instalando las dependencias en tu ordenador de manera global. Para ejecutar el servidor se realiza ejecutando el comando `python3 src\manage.py runserver`.
2. **Docker**: Creación de una imagen Docker para ejecutar el servidor. Para crear esta imagen se debe ejecutar los siguientes comandos:
    1. `docker build -t proyectois2 .`
    2. `docker run -p 80:80 proyectois2`