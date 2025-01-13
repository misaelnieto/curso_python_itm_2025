---
marp: true
title: Programación orientada a objetos
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Programación orientada a objetos

### 2005 - Instituto Tecnológico de Mexicali

![bg right](imagenes/objetos.jpg)


---
<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->


---

# "Todo es un objeto" en Python

En Python, "todo es un objeto" significa que cualquier entidad manipulada (números, texto, funciones, clases, módulos) es una instancia de una clase. Cada objeto tiene:

*   **Identidad:** un identificador único (`id()`).
*   **Tipo:** la clase a la que pertenece (`type()`).
*   **Valor:** los datos que contiene.

Además, puede tener atributos (variables) y métodos (funciones asociadas). Esta uniformidad simplifica el lenguaje y facilita la programación orientada a objetos, permitiendo tratar datos y código de manera consistente.

---

# Todo es un objeto

<div class="columnas">
<div class="col">

- `object`: Es la clase base de todas las demás clases en Python.
Proporciona el comportamiento básico que comparten todos los objetos, como la gestión de atributos, la representación en cadena (__str__), la comparación (__eq__, __ne__, etc.) y el hashing (__hash__).
En la jerarquía de clases, object está en la cima.    
</div>
<div class="col">

- `type`: Es la clase de las clases. En otras palabras, es la *metaclass*. Cuando creas una clase, en realidad estás creando una instancia de `type`. `type` también es la clase de sí misma. Es un caso especial.
</div>
</div>

---

### El sistema de objetos de Python (un poco más extendido)

El sistema de objetos de Python se fundamenta en el principio de que "todo es un objeto". Esto significa que incluso los tipos de datos básicos (como enteros, cadenas y booleanos), las funciones, las clases y los módulos son tratados como objetos.

Existen dos objetos fundamentales: `object` y `type`. `object` es la clase base de la que heredan todas las demás clases, proporcionando comportamientos comunes. `type`, por su parte, es la metaclass, es decir, la clase que crea las clases. De hecho, `object` es una instancia de `type`, y `type` es una instancia de sí misma.

Cada objeto en Python posee una identidad única (`id()`), un tipo (`type()`) que define su clase y un valor que representa los datos que contiene. Además, los objetos pueden tener atributos (variables asociadas) y métodos (funciones asociadas). Esta estructura unificada simplifica el lenguaje y facilita la programación orientada a objetos.


---

# Introspección en Python 

La introspección permite examinar objetos en tiempo de ejecución. Funciones clave:

*   `type(objeto)`: Devuelve el tipo del objeto.
*   `dir(objeto)`: Lista atributos y métodos del objeto.
*   `id(objeto)`: Devuelve la identidad (dirección en memoria) del objeto.
*   `hasattr(objeto, 'nombre')`: Verifica si el objeto tiene un atributo/método con ese nombre.
*   `callable(objeto)`: Verifica si el objeto es invocable (una función, método, etc.).
*   `inspect` (módulo): proporciona herramientas más avanzadas para examinar módulos, clases, métodos, funciones, trazas de pila, marcos, y objetos de código.

Ejemplo: `dir([1, 2])` muestra los métodos de una lista.