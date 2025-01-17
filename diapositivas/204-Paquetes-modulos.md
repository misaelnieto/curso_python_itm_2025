---
marp: true
title: Módulos y paquetes
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Módulos y paquetes

### 2005 - Instituto Tecnológico de Mexicali

![bg right](imagenes/paquetes-modulos.jpg)


<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

---

### Módulos en Python (más detallado)

Los módulos en Python son archivos con extensión `.py` que contienen definiciones de funciones, clases y variables. Permiten organizar y reutilizar código. Se importan con la palabra clave `import`.

**Ejemplo:**

Supongamos un archivo `mi_modulo.py`:

```python
# mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

PI = 3.14159
```

---

# Actividad

## Configuración de `mi_modulo.py `

- Guardar en `c:\Code\mi_modulo.py`
- Abrir una consola y cambiar el directorio a `c:\Code`.
    ```bash
    cd c:\Code
    ```
- Invocar el intérprete de python
    ```python
    >>>
    ```
---

# 3 maneras de usar el módulo

<div class="columnas">
<div class="col">

- Importando todo el módulo
    ```python
    >>> import mi_modulo
    >>> mi_modulo.saludar("Fulano")
    Hola, Fulano!
    >>> mi_modulo.PI
    3.14159
    ```
- Importando elementos especificos del modulo
    ```python
    >>> from mi_modulo import saludar, PI
    >>> saludar("Pedro")
    Hola, Pedro!
    >>> print(PI)
    3.14159
    ```

</div>
<div class="col">

- Importando con un alias
  ```python
    >>> import mi_modulo as mm
    >>> mm.saludar("Luis")
    Hola, Luis!
    >>> print(mm.PI)
    3.14159
  ```
</div>
</div>

---

# Los módulos tambien son objetos

Se puede usar ´dir(modulo)´ para saber qué cotiene dicho módulo.


```python
>>> import mi_modulo
>>> dir(mi_modulo)
['PI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'saludar']
>>> mi_modulo.PI
3.14159
>>> mi_modulo.saludar
<function saludar at 0x00000224BAADA7A0>


>>> mi_modulo.__file__
'C:\\Code\\mi_modulo.py'

>>> mi_modulo.__name__
'mi_modulo'

```
---

# Paquetes

Los paquetes son directorios que contienen módulos (`.py`) y un archivo `__init__.py`. Sirven para organizar módulos relacionados en una estructura jerárquica, facilitando la gestión de proyectos complejos.

En Python, la **modularidad** se extiende a la organización de módulos en directorios, creando lo que se conoce como *paquetes*. Un paquete es un directorio que contiene:

*   Uno o más archivos `.py` (módulos).
*   Un archivo especial llamado `__init__.py`.

El archivo `__init__.py` puede estar vacío, pero su presencia indica a Python que el directorio debe ser tratado como un paquete.


---

# Ejemplo de estructura de un paquete


<div class="columnas">
<div class="col">

```
mi_paquete/
├── init.py
├── modulo1.py
└── subpaquete/
    ├── init.py
    └── modulo2.py
```

</div>
<div class="col">

- `mi_paquete/`: Es el paquete principal.
- `mi_paquete/__init__.py`: Inicializa el paquete `mi_paquete`.
- `mi_paquete/modulo1.py`: Un módulo dentro del paquete.
- `mi_paquete/subpaquete/`: Un subpaquete dentro de `mi_paquete`.
- `mi_paquete/subpaquete/__init__.py`: Inicializa el subpaquete `subpaquete`.
- `mi_paquete/subpaquete/modulo2.py`: Un módulo dentro del subpaquete.
</div>
</div>

---

# Importación de paquetes

Para importar módulos dentro de un paquete, se usa la notación punto (`.`) para indicar la jerarquía:

<div class="columnas">
<div class="col">

- Importa `mi_paquete.modulo1` directo
    ```python
    import mi_paquete.modulo1
    mi_paquete.modulo1.funcion_modulo1()
    ```
- Importa el `modulo1` desde `mi_paquete`
    ```python
    from mi_paquete import modulo1
    modulo1.funcion_modulo1()
    ```

</div>
<div class="col">

- Importa todo el contenido del paquete, pero solo lo que este definido en el `__init__.py`. 
    ```python
    from mi_paquete import *
    ```
- Para que esto funcione, en el `__init__.py` del paquete deberia estar: `from . import modulo1` o `from .subpaquete import modulo2`

</div>
</div>

---

# Las baterías vienen incluidas

- Python viene con cientos de módulos incluidos
	- https://docs.python.org/3/library/index.html
- Miles de módulos de terceros disponibles desde https://pypi.org/


---


# Siguiente: [Entornos virtuales →](205-Entornos-virtuales.md)