---
marp: true
title: 06 - Texto
---

# Aplicaciones web con Python

## Enero 2025

### Instituto Tecnológico de Mexicali

#### 05 - Texto

---
<!--
theme: default
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Texto en Python

- Sólo hay un tipo de datos para texto: `str`.
  - ***Inmutable***
  - Indexable (***slice***)
- El texto se delimita por comillas simples (`'`) o comillas dobles (`"`).
- Múltiples líneas:
  - `\n`
  - Delimitado por tres comillas simples/dobles: `'''` / `"""`
- No hay tipo de datos para caracteres (`char`) debido a que por default, el codificado de texto en Python 3 es UTF-8 y ya no se puede asumir que un caracter tenga 8 bytes.

---


# Ejemplo 1

```python
>>> '' == str() == ""
True
>>> 'hola mundo'
'hola mundo'
>>> " ' "
" ' "
>>> ' " '
' " '
>>> '"' == "\""
True
>>> "'" == '\''
True
```

---

# El texto es indexable ...

```python
>>> a = 'foo bar'
>>> a[0]
'f'
>>> a[-1]
'r'
```

## Pero inmutable

```python
>>> a = 'foo bar'
>>> a[2] = 'z'
Traceback (most recent call last):
  File "<python-input-35>", line 1, in <module>
    a[2] = 'z'
    ~^^^
TypeError: 'str' object does not support item assignment
>>>
```

---

# Texto con líneas múltiples

```python
>>> """
... Cadena con multiples lineas.
... Puede contener " y ' sin problemas.
... """
'\nCadena con multiples lineas.\nPuede contener " y \' sin problemas.\n'
>>> print _
Cadena con multiples lineas.
Puede contener " y ' sin problemas.
```

---

# Texto con acentos y caracteres especiales

```python
>>> 'áéíóúñ⌚⏰✅'
'áéíóúñ⌚⏰✅'
```
