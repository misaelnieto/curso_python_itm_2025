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

# "Todo es un objeto" en Python

En Python, "todo es un objeto" significa que cualquier entidad manipulada (números, texto, funciones, clases, módulos) es una instancia de alguna clase. Cada objeto tiene:

*   **Identidad:** un identificador único (`id()`).
*   **Tipo:** la clase a la que pertenece (`type()`).
*   **Valor:** los datos que contiene.

Además, puede tener *atributos* (variables) y *métodos* (funciones asociadas). Esta uniformidad simplifica el lenguaje y facilita la programación orientada a objetos, permitiendo tratar datos y código de manera **consistente**.

---

# Objetos fundamentales

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

# Clase

```python
class Fruta:
    def __init__(self, nombre, color, sabor):
        self.nombre = nombre
        self.color = color
        self.sabor = sabor

    def madurar(self):
        print(f"{self.nombre} está madurando y se vuelve más dulce.")

    def mostrar_info(self):
        print(f"Esta fruta es una {self.nombre}, es de color {self.color} y tiene un sabor {self.sabor}.")
```
---

# Objetos: Instancia de una clase

- Nombre de la clase
- `()`
- Parámetros del constructor `__init__()`

```python
manzana_roja = Fruta("Manzana", "Roja", "Dulce")

platano_verde = Fruta("Plátano", "Verde", "Insípido")

naranja_valencia = Fruta("Naranja", "Naranja", "Cítrico")
```

---

# Atributos de una **clase**

Son variables que almacenan datos asociados a **una clase** y es compartida por todas las instancias/objetos de esa clase.

Se accede a ellos usando la notación de punto (`.`) después del **objeto** `objeto.atributo` o de la clase `objeto.atributo`.

---

# Modificando los atributos de una clase

En Python puedes modificar el atributo de una clase o de una instancia de esa clase, pero tienen efectos distintos.

```python
class Automovil:
    llantas = 4

    def __init__(self, marca):
        self.marca = marca

    def info(self):
        print(f"Este {self.marca} tiene {self.llantas} llantas.")
```

Aquí `llantas` es un atributo de clase, mientras que `marca` es un atributo de la instancia de esa clase.

---
# Acceso: atributo de clase vs atributo de instancia

```python
>>> auto1 = Automovil('Ford')
>>> auto2 = Automovil('Nissan')
```

## El atributo de clase es accesible desde la clase y desde la instancia.

```python
>>> Automovil.llantas
4
>>> auto1.llantas
4
>>> auto2.llantas
4
```
</div>
</div>

---

# Pero el atributo de instancia pertenece solamente a esa instancia y no a la clase.

```python
>>> auto1.marca
'Ford'
>>> auto2.marca
'Nissan'
>>> Automovil.marca
Traceback (most recent call last):
File "<pyshell#27>", line 1, in <module>
    Automovil.marca
AttributeError: type object 'Automovil' has no attribute 'marca'
```

---

# Atributos de un objeto

Son variables que almacenan datos asociados a un objeto. Representan las características o propiedades de esa instancia en particular.

Se accede a ellos usando la notación de punto (`.`) después del objeto: `objeto.atributo`. Ejemplo:

<div class="columnas">
<div class="col">

- `.nombre`
- `.color`
- `.sabor`

</div>
<div class="col">

```python
print(manzana_roja.nombre)  # Imprime Manzana
print(platano_verde.color) # Imprime Verde
print(naranja_valencia) # Imprime Cítrico
```

</div>
</div>

---


# Métodos de una instancia

- `madurar()`
- `mostrar_info()`

```python
>>> manzana_roja.madurar()
Manzana está madurando y se vuelve más dulce
>>> naranja_valencia.mostrar_info()
Esta fruta es una Naranja, es de color Naranja y tiene un sabor Cítrico.
```
---

## `self`

> En Python, `self` es una convención utilizada para referirse a la ***instancia* del objeto dentro de una clase**. Aunque puedes usar cualquier otro nombre, `self` es la práctica estándar y altamente recomendada, ya que mejora la legibilidad del código y facilita la comprensión por parte de otros programadores.

### Reglas

- Es el primer argumento en los métodos de instancia
- Usa `self` para tener acceso a los atributos y métodos de la instancia de la clase.

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


---



# Siguiente: [Paquetes y módulos →](204-Paquetes-modulos.md)