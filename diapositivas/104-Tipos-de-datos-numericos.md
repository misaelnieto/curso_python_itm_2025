---
marp: true
title: Tipos de datos numéricos
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Tipos de datos numéricos

### 2005 - Instituto Tecnológico de Mexicali

#### https://tinyurl.com/pyitm2025

![bg right](imagenes/numeros.jpg)


---

<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->
# Tipos de datos numéricos en Python

* **Entero**
  * Booleano
  * Octal
  * Hexadecimal
  * Binario
* **Coma flotante**
  * Numeros complejos

---

# Tipos de datos básicos: **números enteros**

## int

```py
>>> 100 == int(100)
True
```

> **Notas**:
> - En Python 3 desapareció la distinción entre enteros largos y cortos o enteros sin signo o con signo. Internamente, el intérprete limita el tamaño de un número entero basado en el tamaño de la memoria virtual disponible en el sistema. Para las operaciones shift y mask el intérprete asume una representación binaria.
[Fuente](https://docs.python.org/3/reference/datamodel.html#numbers-integral).

---

# Tipos de datos básicos: **`bool`**

```python
>>> True == bool(True) == 1
True
>>> True == bool(False) == bool(0)
False
```

> **Nota**: El intérprete de Python representa internamente a los números booleanos como `0` (`False`) o `1` (`True`).

---

# Tipos de datos básicos: **`oct`**

```python
>>> 0o10 == 0O10
True
>>> 10 == 10.0 == 0o12
True
```

> **Nota**: El intérprete de Python representa internamente a los números `oct` como enteros.

---

# Tipos de datos básicos: **`hex`**

```python
>>> 0x0a == 0x0A == 0X0a == 0X0A
True
>>> 10 == 10.0 == 0o12 == 0x0a
True
```

> **Nota**: El intérprete de Python representa internamente a los números `hex` como enteros.


---
# Tipos de datos básicos: **`bin`**


```python
>>> 0b1010 == 0B1010
True
>>> 10 == 10.0 == 0o12 == 0x0a == 0b1010
True
```

---

# Tipos de datos básicos: **`float`**


```python
>>> 100.1 == float (100.1)
True
>>> 100.0 == 100
True
```

> - Implementados como `double` en `C`
> - Los detalles de precisión y representación interna están disponibles en `sys.float_info`

---

# Tipos de datos básicos: **`sys.float_info`**

```python
>>> import sys
>>> sys.float_info
sys.float_info(
    max=1.7976931348623157e+308, 
    max_exp=1024, max_10_exp=308, 
    min=2.2250738585072014e-308, min_exp=-1021, 
    min_10_exp=-307, dig=15, 
    mant_dig=53, epsilon=2.220446049250313e-16, 
    radix=2, rounds=1
)
>>>
```

---

# Tipos de datos básicos: **números complejos**

```python
>>> 1 + 2j == (1 + 2j) == complex(1,2)
True
>>> 10 == 10.0 == 0o12 == 0x0a == (10 +0j)
True
```

> **Nota**: La parte real y la parte imaginaria son `float`


---

# Siguiente: [Manupulación de texto →](105-Manipulación-de-texto.md)
