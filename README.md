# 🌌 Mundo Desconocido

Mundo Desconocido se trata de un blog con temática sobre el **universo y el espacio**, desarrollado con Django y MongoDB para la asignatura de Ingeniería de Software 2.

Puedes visitar nuestra página web en [mundo-desconocido.herokuapp.com](mundo-desconocido.herokuapp.com).

## Partes del proyecto 📑
- Inicio de Sesión
- Base de Datos
- Alojar el Servidor
- Control de versiones (Git)

## Framework 👁️👁️
Usaremos [Django](https://www.djangoproject.com/ "Django") dado que la programación es simple y nos da bastantes facilidades para diseñar el blog a nuestra manera de una forma sencilla y rápida. Además usaremos [Slack](https://app.slack.com/client/T01F9S4N479/C01FQJRJ518 "Slack") para la planificación del proyecto y la discusión y reparto de las tareas. Tuvimos la idea de usar Trello, pero dado que el propio **Github** tiene un apartado para el manejo de proyectos nos decantamos por esa opción.

## Lenguaje 💬
Usaremos [Python](https://es.python.org/ "Python") para el login y la conexión a la base de datos, ya que es el lenguaje que soporta el Framework elegido.

## Instalación
Para iniciar el programa se puede realizar de dos formas:
1. **Global**: Instalando las dependencias en tu ordenador de manera global. Para ejecutar el servidor se realiza ejecutando el comando `python3 src\manage.py runserver`.
2. **Docker**: Creación de una imagen Docker para ejecutar el servidor. Para crear esta imagen se debe ejecutar los siguientes comandos:
    1. `docker build -t proyectois2 .`
    2. `docker run -p 80:80 proyectois2`