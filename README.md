- EcoTech Solutions - Sistema de Gestión Interna-
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Este repositorio contiene el prototipo y avance estructural del Sistema de Gestión Interna para la empresa **EcoTech Solutions**, desarrollado en el marco de la asignatura *Programación Orientada a Objeto Seguro* (TI3021) en INACAP.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Descripción del Proyecto
El objetivo principal es traducir el modelo UML previamente validado a una solución funcional en **Python**, aplicando principios del paradigma Orientado a Objetos (POO) y asegurando la persistencia de datos mediante la conexión con **Oracle Database**.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Tecnologías y Librerías;
* **Lenguaje:** Python 3.x
* **Base de Datos:** Oracle Database
* **Librería de Conexión:** `oracledb` (Librería oficial de Oracle)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Estructura del Proyecto;
* `clases.py`: Define el modelo de dominio aplicando encapsulamiento, herencia y relaciones (`Persona`, `Empleado`, `Cliente`, `Producto`, `Pedido`).
* `conexion.py`: Configura y prueba la conexión exitosa a la base de datos Oracle mediante `oracledb`.
* `main.py`: Script principal de prueba para validar la creación de objetos, gestión de stock y flujo de pedidos.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Requisitos de Evaluación Cumplidos;
 **Traducción UML a Python:** Definición de clases y relaciones de herencia/asociación.
 **Principios POO:** Uso de encapsulamiento (atributos protegidos/métodos) y reutilización de código (`super()`).
 **Persistencia:** Conexión funcional a Oracle Database con gestión adecuada de excepciones.
