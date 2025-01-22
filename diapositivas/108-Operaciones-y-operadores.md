---
marp: true
title: Operaciones y operadores
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Operaciones y operadores

### 2005 - Instituto Tecnológico de Mexicali

#### https://tinyurl.com/pyitm2025

![bg right](imagenes/operadores.jpg)


---
<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Operaciones

> Una operación en Python es una acción que se realiza sobre uno o más objetos (operandos). 

# Operadores

> Las operaciones están soportadas a través de operadores (ej., `+`, `-`, `in`) o métodos (ej., `.append()`, `.upper()`), cuyo comportamiento será específico según el tipo de objeto.


---
# Operaciones: El cero

- Ausencia de valor: `None`
- Números: `0`, `0.0`, `0L`, `0x00`, `0b00`, `0o00`
- Secuencias vacías: `()`, `''`, `[]`, `{}`


> Cualquier valor **“cero”** equivale a **False**
> Cualquier valor diferente a **“cero”** equivale a **True**

![bg right](imagenes/cero.jpg)

---


# Operadores booleanos

No solo devuelven un valor booleano (`True` o `False`), sino que ***también pueden devolver uno de sus operandos***.


| Operador | Resultado                                                                    |
|----------|------------------------------------------------------------------------------|
| `x or y`   | Si `x` evalúa a `False`, entonces el resultado equivale a `y`. De lo contrario es `x`.     |
| `x and y`  | Si `x` evalúa a `False`, entonces el resultado equivale a `x`. De lo contrario es `y`.     |
| `not x`    | Si `x` evalúa a `False`, entonces el resultado equivale a `x`. De lo contrario es `False`. |

---

# Ejemplo de `or`

<div class="columnas">
<div class="col">

```python
>>> a = 0
>>> b = 7
>>> a or b
7
```

- `a = 0`: a se considera "falso" porque es `0`.
- `a or b`: Como a es "falso", `or` evalúa el segundo operando, `b`, que es `7`.
</div>
<div class="col">

```python
>>> a = 1
>>> b = 7
>>> a or b
1
```

- `a or b`: Como a es "verdadero", `or` devuelve inmediatamente el primer operando, `a`, que es `1`. No se evalúa el segundo operando (`b`). Por lo tanto, el resultado es `1`.

</div>
</div>


---

# Ejemplo de `and`

<div class="columnas">
<div class="col">

```python
>>> a = 0
>>> b = 7
>>> a and b
0
```

- `a = 0`: a se considera "falso" porque es `0`.
- `a and b`: Como a es "falso", `and`  inmediatamente devuelve el primer operando, `a`, que es `0`.
</div>
<div class="col">

```python
>>> a = 1
>>> b = 7
>>> a and b
7
```

- `a and b`: Como `a` es "verdadero", `and` inmediatamente devuelve el segundo operando `b`, que es `7`.

</div>
</div>

---

# Ejemplo de `not`

```python
>>> a = 0
>>> not a
True
>>> b = []
>>> not b
True
>>> b.append(5)
>>> not b
False
```

---

# Son más útiles juntos

```python
>>> canasta = []
>>> not canasta and 'La canasta esta vacia' or 'La canasta tiene algo'
'La canasta esta vacia'
>>> canasta.append('manzana')
>>> not canasta and 'La canasta esta vacia' or 'La canasta tiene algo'
'La canasta tiene algo'
```

---

<div class="columnas">
<div class="col">

## Operadores de comparación

* Mayor que ... `>`
* Menor que ... `<`
* Mayor o igual ... `>=`
* Menor o igual ... `<=`
* Igual ... `==`
* No igual ... `!=`

</div>
<div class="col">

## Operadores de identidad

Los operadores `is` e `is not` en Python se utilizan para comparar la identidad de los objetos, no su valor.

```python
a = [1, 2, 3]
b = a         # b se refiere al mismo objeto que a
c = [1, 2, 3] # c es un nuevo objeto con el mismo valor que a

print(a == b)   # True (mismo valor)
print(a is b)   # True (misma identidad)

print(a == c)   # True (mismo valor)
print(a is c)   # False (diferente identidad, aunque mismo valor)
```

</div>
</div>

---
# Operaciones: comparación


```python
>>> 2 > 1
True
>>> 1.1 > 2
False
>>> 1 +2j >= 1
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    1 +2j >= 1
TypeError: '>=' not supported between instances of 'complex' and 'int'
```

---
# Operaciones básicas

* Suma ... `+`
* Resta ... `-`
* Multiplicación ... `*`
* División ... `/`
* División entera ... `//`
* Remanente ... `%`
* Potenciación ... `**`

---
# Reglas de división en Python 3

<div class="columnas">
<div class="col">

*   `/` (**División estándar**): Siempre devuelve un `float`.

    ```python
    5 / 2  # Resultado: 2.5
    ```

*   `//` (**División entera**): Devuelve el cociente entero (redondea hacia abajo).

    ```python
    5.0 // 2  # Resultado: 2.0
    -5 // 2 # Resultado: -3
    ```

</div>
<div class="col">

*   `%` (**Módulo **): Devuelve el resto de la división. El signo del resultado es el del divisor.

    ```python
    5 % 2   # Resultado: 1
    -7 % 3 # Resultado: 2
    7 % -3 # Resultado: -2
    ```
* División entera y módulo en una sola función:
    ```python
    >>> divmod(10,3)
    (3,1)
    >>> (10//3, 10%3)
    (3,1)
    ```
</div>
</div>

---

# Operaciones booleanas a nivel de bit.

```python
>>> #or
>>> hex(0x0f | 0xf0)
'0xff'
>>> #and
>>> hex(0x0f & 0xf0)
'0x0'
>>> #xor
>>> hex(0x0f ^ 0xf0)
'0xff'
>>> #Corrimiento
>>> hex(0x01 << 4), hex(0xF0 >> 4)
('0x10', '0xf')
>>> #inversion de bits
>>> hex(~0xF)
'­0x10'
```
---
# Otras operaciones matematicas

* Valor absoluto ... `abs()`
```python
>>> abs(-10)
10
```

---

# Conversión a entero ... `int()`

```python
>>> int(3.14)
3
>>> int('123')
123
>>> int('0x313373', 16)
3224435
>>> int('1010', 2)
10
```

---

# Conversión a float en Python

Se usa la función `float()` para convertir valores a números de coma flotante.

<div class="columnas">
<div class="col">

*   **De entero a float:**

    ```python
    entero = 5
    flotante = float(entero)  # Resultado: 5.0
    print(type(flotante)) #Output: <class 'float'>
    ```

*   **De cadena a float:**

    ```python
    cadena = "3.14159"
    flotante = float(cadena)  # Resultado: 3.14159
    print(type(flotante)) #Output: <class 'float'>
    ```

</div>
<div class="col">

*   **De booleano a float:**

    ```python
    booleano_verdadero = True
    flotante_verdadero = float(booleano_verdadero)  # Resultado: 1.0

    booleano_falso = False
    flotante_falso = float(booleano_falso)  # Resultado: 0.0
    print(type(flotante_verdadero)) #Output: <class 'float'>
    print(type(flotante_falso)) #Output: <class 'float'>
    ```

*   **Combinando con otras funciones:**

    ```python
    cadena_con_espacios = "   42   "
    flotante = float(cadena_con_espacios.strip())
    print(type(flotante)) #Output: <class 'float'>
    ```
</div>
</div>


---


**Puntos importantes:**

*   Si intentas convertir una cadena que no representa un número válido (ej., "abc"), se producirá un error `ValueError`.
*   La conversión de `True` a `float` da como resultado `1.0`, y la conversión de `False` da como resultado `0.0`.
*   Es útil usar `.strip()` para eliminar espacios en blanco antes de convertir una cadena a float.


---

# Siguiente: [Estructuras de control de flujo →](201-Control-de-flujo.md)