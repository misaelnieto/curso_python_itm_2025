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
*   **Estado:** contiene otros objetos cuyo valor puede ser único a la instancia. Se accede a ellos mediante  ***atributos***
*   **Comportamiento**: Funciones asociadas que definen su comportamiento.

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
# Herencia en Python

La herencia permite que una clase (subclase o hija) herede atributos y métodos de otra clase (superclase o padre). Esto promueve la reutilización de código y la organización jerárquica.



<div class="columnas">
<div class="col">

- Ejemplo
    ```python
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre
        def hablar(self):
            print("Sonido genérico de animal")

    class Perro(Animal):
        def hablar(self):
            print("Guau!")
    ```
</div>
<div class="col">

- Salida
    ```python
    mi_perro = Perro("Chocorol")
    # Imprime: Guau!
    mi_perro.hablar()
    #Imprime: Chocorol. Accede a un atributo de la clase padre
    print(mi_perro.nombre)
    animal_generico = Animal("Polito")
    #Imprime: Sonido genérico de animal
    animal_generico.hablar()
    ```
</div>
</div>


---

### Abstracción

<!--
**La abstracción**: ocultar la complejidad de la implementación interna de un objeto y exponer solo una interfaz simplificada para interactuar con él. Se logra principalmente mediante clases y métodos.
-->

<div class="columnas">
<div class="col">

```python
class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._motor = Motor()

    def arrancar(self):
        self._motor.encender()
        print("El coche ha arrancado.")

    def conducir(self):
        print("Conduciendo el coche.")
```

</div>
<div class="col">

- `self._motor` - Atributo interno, detalle de implementacion
- El usuario de la clase `Coche()` no necesita saber cómo funciona internamente el motor.
    ```python
    mi_coche = Coche("Toyota", "Corolla")
    mi_coche.arrancar()
    mi_coche.conducir()
    ```
</div>
</div>

---

# Encapsulamiento

- El encapsulamiento en Python se implementa principalmente por convención (usando un guión bajo `_`), y en menor medida con "name mangling" (`__`). El objetivo es mejorar la organización del código, prevenir errores y facilitar el mantenimiento.
- En la práctica, no hay atributos ni métodos privados
- Pero si puede haber atributos de solo lectura

---

# Ejemplo de encapsulamiento

<div class="columnas">
<div class="col">

- Clase con tres tipos de atributo

```python
class MiClase:
    def __init__(self):
        self.publico = 3.1416
        self._semi_privado = 1234
        self.__muy_privado = "313373"
    
    def imprime(self):
        print(
            self.publico,
            self._semi_privado,
            self.__muy_privado
        )

objeto = MiClase()
```

</div>
<div class="col">

- Desde dentro de la clase el acceso a los tres atributos es normal.
```python
>>> objeto.imprime()
3.1416 1234 313373
```
- Desde fuera de la clase, solo dos son accesibles con el mismo nombre
```python
>>> objeto.publico
3.1416
>>> objeto._semi_privado
1234
>>> objeto.__muy_privado
Traceback ...
```
</div>
</div>

---

# Ejemplo de encapsulamiento

<div class="columnas">
<div class="col">

- Clase con tres tipos de atributo

```python
class MiClase:
    def __init__(self):
        self.publico = 3.1416
        self._semi_privado = 1234
        self.__muy_privado = "313373"
    
    def imprime(self):
        print(
            self.publico,
            self._semi_privado,
            self.__muy_privado
        )

objeto = MiClase()
```

</div>
<div class="col">

- Pero a `.__muy_privado`, se le cambió el nombre (*name mangling*)
    ```python
    >>> objeto._MiClase__muy_privado
    '313373'
    ```


</div>
</div>

---

# Polimorfismo

<div class="columnas">
<div class="col">

- Una clase base con dos subclases
    ```python
    class Gato:
        def hacer_sonido(self):
            print("Prrrrrr")

    class Luna(Gato):
        def hacer_sonido(self):
            print("Miauuu")

    class Cucho(Gato):
        def hacer_sonido(self):
            print("Mrma mra mra mauuu")
    ```
</div>
<div class="col">

- Ejemplo de uso
```python
>>> gato1 = Gato()
>>> gato1.hacer_sonido()
Prrrrrr

>>> gato2 = Luna()
>>> gato2.hacer_sonido()
Miauuu

>>> gato3 = Cucho()
>>> gato3.hacer_sonido()
Mrma mra mra mauuu
```
</div>
</div>

---

# Recolección de basura

La recolección de basura en Python es un proceso automático que libera la memoria que ya no está en uso por el programa. Python utiliza principalmente dos técnicas:

1.  **Conteo de referencias:** Cada objeto tiene un contador que rastrea cuántas referencias apuntan a él. Cuando este contador llega a cero, el objeto se libera inmediatamente.

2.  **Recolector cíclico:** El conteo de referencias no maneja correctamente las referencias circulares (cuando dos o más objetos se referencian entre sí, impidiendo que su contador llegue a cero). El recolector cíclico detecta y libera estos ciclos.

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