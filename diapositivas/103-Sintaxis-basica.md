---
marp: true
title: Sintaxis básica de Python
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Sintaxis básica de Python

### 2005 - Instituto Tecnológico de Mexicali

![bg right](imagenes/ast.jpg)

---
<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Todo es un objeto

- Virtualmente todo es un objeto, con atributos y métodos.
- Los números, el texto, las funciones, los módulos, etc.

---

# Puntos claves de la sintaxis de Python

# Sintaxis

- ***Identación***: Los bloques de código se delimitan con espacios (generalmente 4) o tabuladores.
- Las **sentencias** terminan ***hasta el fin de la línea***. El `;` no es necesario. Las líneas vacías se ignoran.
- **Case-sensitive**: Distingue entre mayúsculas y minúsculas
- Los ***comentarios*** comienzan con el caracter `#` y terminan hasta el fin de la línea. 

---

# Puntos claves de la sintaxis de Python

# Variables

- ***Duck typing***: El intérprete *infiere* el tipo de la variable
- **Las variables** son *nombres* que apuntan a una instancia de un objeto.
- **Reglas**
  - Deben comenzar con una letra o `_`
  - **No pueden** comenzar con números
  - **Deberían** solo contener `A-z`, `0-9` y `_`
  - **No pueden** ser igual a alguna de las palabras reservadas

---
# Palabras reservadas

1. Valores booleanos y nulo: `True`, `False` y `None`.
2. Operadores lógicos: `and`, `or`, `not`
3. Estructuras de control de flujo: `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `match` y `case`.
4. Definición de funciones y clases: `def`, `class`, `return`, `lambda` y `yield`
5. Manejo de excepciones: `try`, `except`, `finally`, `raise` y `assert`
1. Manejo de contexto: `with`
2. Importación de módulos: `import`, `from` y  `as`
4. Variables globales y no locales: `global` y `nonlocal`
4. Otras palabras reservadas: `del` y `pass`
---

# Puntos claves de la sintaxis de Python

## Operadores
- Aritméticos (`+`, `-`, `*`, `/`, `//` (división entera), `%` (módulo), `**` (potencia))
- Asignación: (`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`)
- Comparación (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Lógicos (`and`, `or`, `not`)
- Identidad (`is`, `is not`)
- Pertenencia (*membership*) (`in`, `not in`)
- Nivel de bit (`&`, `|`, `^`, `~`, `<<`, `>>`)
- Control de precedencia `()`

---

# Todo es un objeto

```python
>>> a=1
>>> dir(a)
[... 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate',
'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator',
'real', 'to_bytes']

>>> a=3.1416
>>> dir(a)
[... 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']


>>> a='Hola'
>>> dir(a)
[ ... 'capitalize', 'casefold', 'center', 'count', ...  'zfill']
```

---

# Indentación con espacios

```python
if condicion:
    # Código dentro del bloque if (indentado)
    print("Condición verdadera")
else:
    # Código dentro del bloque else (indentado)
    print("Condición falsa")
```


---

# Indentación con espacios

```python
def suma():
    return 1 + 1

def multiplica(a, b):
    return a * b

```

---

# Indentación con espacios

```python
for i in range(10):
    print(i)


c = 10
while c:
    print(c)
    c -= 1
```

---

# Indentación con espacios

```python
class Animal:
    sonido = "..."
    def habla(self):
        print(self.sonido)

class Pollito(Animal):
    sonido = "Pio"
    def picotea(self):
        pass

class Gato(Animal):
    sonido = "Miau"

    def salta(self):
        pass
```

---

# Las sentencias terminan al final de la línea

Las sentencias generalmente terminan al final de la línea. No se usa punto y coma `;` al final de cada línea, aunque se puede usar para separar múltiples sentencias en una misma línea (no es recomendable).


```python
el_mundo_es_plano = True
dos_mas_dos = 5
print("Hola mundo")
a = 5; b = 10; print(a + b) # Múltiples sentencias en una línea (no recomendable)
```

---

# Distinción entre mayúsculas y minúsculas

Python es sensible a mayúsculas y minúsculas (case-sensitive). `Variable`, `variable` y `VARIABLE` son tres identificadores diferentes.

```python
>>> hola="mundo"
>>> print(Hola)
Traceback (most recent call last):
  File "<python-input-22>", line 1, in <module>
    print(Hola)
          ^^^^
NameError: name 'Hola' is not defined. Did you mean: 'hola'?
```

---

# Comentarios

- **Comentarios de una línea**: se inician con `#`.
- **Comentarios de múltiples líneas** (*docstrings*): se delimitan con tres comillas simples `'''` o dobles `"""`. Se utilizan para documentar **funciones**, **clases** y **módulos**.

```python
# Este es un comentario de una línea
def mi_funcion():
    """
    Este es un docstring.
    Describe el funcionamiento de la función.
    """
    pass

print("Hola mundo")  # Los comentarios terminan hasta el fin de linea

```

---

# Las líneas vacías se ignoran

```python
el_mundo_es_plano = True


dos_mas_dos = 5

print("Hola mundo")
```

---

# Siguiente: [Tipos de datos numéricos →](104-Tipos-de-datos-numericos.md)