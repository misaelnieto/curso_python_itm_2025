---
marp: true
title: Entornos virtuales
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Entornos virtuales

### 2005 - Instituto Tecnológico de Mexicali

![bg right](imagenes/virtualenvs.jpg)

---
# PYTHONPATH

- `PYTHONPATH` es una variable de entorno del sistema operativo que le dice al intérprete de Python dónde buscar módulos que se intentan importar con la instrucción `import`.
- Cuando se ejecuta `import mi_modulo`, Python busca `mi_modulo.py` (o un paquete `mi_modulo`) en varias ubicaciones, incluyendo las especificadas en `PYTHONPATH`.


---

# Usos del PYTHONPATH

Principalmente, `PYTHONPATH` se usa para:

*   **Importar módulos no instalados:** Permite importar módulos que no se han instalado con `pip install` y que se encuentran en directorios específicos del usuario o del proyecto. Esto es útil durante el desarrollo.

*   **Añadir rutas personalizadas:** Permite añadir rutas donde se encuentran módulos propios o de terceros que no están en las rutas estándar de Python.


---

## ¿Cómo funciona?

Cuando se ejecuta `import mi_modulo`, Python busca en el siguiente orden:

1.  El directorio actual.
2.  Las rutas especificadas en la variable de entorno `PYTHONPATH`.
3.  Los directorios de las bibliotecas estándar de Python.
4.  Los directorios de los paquetes de terceros instalados.


---


# El entorno de desarrollo de Python

![center height:10em](imagenes/interpretes-1.png)

---

# El entorno de desarrollo de Python

![center height:10em](imagenes/interpretes-2.png)


---

# Siguiente: [Aplicacion web con Flask →](301-Flask.md)