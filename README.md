## 👋 ¡Bienvenidos usuarios a mi proyecto! sistema de prestamos

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un sistema básico de préstamos de libros utilizando Python. El programa permite registrar qué persona solicita un libro y llevar el control de los préstamos activos mediante el uso de diccionarios como estructura principal de almacenamiento.

Cada préstamo se guarda en un diccionario donde la clave representa el nombre de la persona y el valor corresponde al libro que tiene prestado. Esta estructura permite gestionar la información de manera organizada, facilitando la búsqueda, registro y eliminación de préstamos cuando se realiza la devolución.

El sistema funciona mediante un menú interactivo en consola que permite registrar nuevos préstamos, devolver libros y visualizar los préstamos activos en cualquier momento. La interacción continua permite realizar múltiples operaciones sin necesidad de reiniciar el programa.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar información estructurada.
- Aplicar funciones para dividir el programa en bloques organizados.
- Utilizar condicionales para validar préstamos existentes.
- Desarrollar un menú interactivo con bucles.
- Simular el funcionamiento básico de un sistema de biblioteca.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Condicionales (`if`, `else`)
- Bucles `while`
- Bucles `for`
- Eliminación de elementos con `del`
- Validación de claves en diccionarios

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `prestamos` donde:
   - La clave representa el nombre de la persona.
   - El valor representa el libro prestado.

2. El sistema muestra un menú con las siguientes opciones:
   - Registrar préstamo.
   - Devolver libro.
   - Mostrar préstamos activos.
   - Salir.

3. Al registrar un préstamo:
   - Se valida que la persona no tenga ya un libro prestado.
   - Se almacena la información en el diccionario.

4. Al devolver un libro:
   - Se verifica que exista el préstamo.
   - Se elimina el registro del diccionario.

5. El programa se ejecuta continuamente hasta que el usuario seleccione la opción de salir.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```