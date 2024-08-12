### Gestión de Trabajadores

Este proyecto fue desarrollado como actividad final del curso de Programación desde Cero, dictado por Codo a Codo, la división encargada de la capacitación tecnológica dentro de la Agencia de Aprendizaje a lo largo de la vida, iniciativa del gobierno de Buenos Aires para capacitar a la población gratuitamente. 

Se trata de una aplicación en Python para gestionar información de trabajadores. La aplicación permite realizar diversas operaciones sobre los datos de los trabajadores, incluyendo su ingreso, modificación, eliminación y generación de reportes.


# Descripción
La aplicación está compuesta por dos archivos principales:

## menu_principal.py:
Es el punto de entrada de la aplicación. Presenta un menú interactivo para que el usuario seleccione una opción para gestionar trabajadores o generar reportes. Dependiendo de la opción elegida, el usuario puede acceder a diferentes funcionalidades proporcionadas por el módulo trabajadores.py.

## trabajadores.py: 
Contiene la lógica de gestión de trabajadores, incluyendo funciones para ingresar, modificar, eliminar trabajadores y generar reportes sobre su estado y características.


# Funcionalidades:

## menu_principal.py:

Gestionar Trabajadores: Permite ingresar nuevos trabajadores, modificar información de trabajadores existentes y eliminar trabajadores.

Generar Reportes: Ofrece reportes sobre trabajadores activos, desocupados, desocupados en un rango de edad y trabajadores según la profesión.

Cambiar Estado de un Trabajador: Permite cambiar el estado de un trabajador (activo/desocupado).

## trabajadores.py:

Ingresar Trabajador: Permite agregar un nuevo trabajador con su DNI, nombre, edad, profesión y estado.

Modificar Trabajador: Permite actualizar información de un trabajador existente, incluyendo DNI, nombre, edad y profesión.

Eliminar Trabajador: Permite eliminar un trabajador del sistema utilizando su DNI.

Generar Reportes: Incluye funciones para:
Mostrar trabajadores activos.
Mostrar trabajadores desocupados.
Mostrar trabajadores desocupados en un rango de edad.
Mostrar trabajadores según su profesión.

Cambiar Estado: Permite cambiar el estado (activo/desocupado) de un trabajador.

# Requisitos
Python 3.x

# Instalación
Clona el repositorio:
git clone https://github.com/germancaradec/Codo-a-Codo-Desde-cero-Python.git

cd Codo-a-Codo-Desde-cero-Python

# Ejecute la aplicación:
python menu_principal.py

# Conceptos Aplicados:

## Estructuras de Datos: 
Uso de diccionarios para almacenar y gestionar la información de los trabajadores.

## Interacción con el Usuario: 
Menú interactivo que permite al usuario elegir opciones y proporcionar datos.

## Manejo de Excepciones: 
Uso de bloques try-except para manejar entradas incorrectas y evitar que el programa se detenga por errores inesperados.