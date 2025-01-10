---
marp: true
title: "05 - Estructuras de datos: Secuencias"
---

# Aplicaciones web con Python

## Enero 2025

### Instituto Tecnológico de Mexicali

#### 05 - Estructuras de datos: secuencias

---
<!--
theme: default
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Estructuras de datos: secuencias


- Secuencia: un conjunto ordenado de objetos
  - tuplas (`tuple`)
  - listas (`list`)
  - texto (`str`)
  - Datos binarios (`bytes`, `bytearray`)

---

# Secuencias (tuplas)
* Tupla: es una lista con un número ***limitado*** de objetos.
* En python, una tupla es una secuencia de valores u objetos separados por comas.

---

```python
>>> 1 , 12.9, 0x0fe, 0b10001
(1, 12.9, 254, 17)
>>> (1, 2, 3, 4)
(1, 2, 3, 4)
>>> (1, 2, 3, 4, (1 , 12.9), 0b10001 )
(1, 2, 3, 4, (1, 12.9), 17)
```
---


# Secuencias (tuplas)

## Rebanadas e índices

```python
>>> t = (1, 2, 3, 4)
>>> t[0]
1
>>> t[3]
4
>>> t[1:3]
(2, 3)
>>> t[1]
4
>>> t[1:3]
(2,3)
>>> t[2:]
(3, 4)
>>> t[2:][1]
4
```

---

# Secuencias (listas)
* Lista: es una lista con un número ***ilimitado*** de objetos.
* En python, una lista es una secuencia de valores u objetos separados por comas y delimitadas por corchetes.

---

```python
>>> [1 , 12.9, 0x0fe, 0b10001]
[1, 12.9, 254, 17]
>>> [1, 2, 3, 4]
(1, 2, 3, 4)
>>> [1, 2, 3, 4, (1 , 12.9), 0b10001 ]
[1, 2, 3, 4, (1, 12.9), 17]
```

--- 


# Secuencias (listas)

## Rebanadas e índices

```python
>>> l = [1, 2, 3, 4]
>>> l[0]
1
>>> l[3]
4
>>> l[1:3]
(2, 3)
>>> l[1]
4
>>> l[1:3]
(2,3)
>>> l[2:]
(3, 4)
>>> l[2:][1]
4
```

---

# Tuplas vs listas

| Tuplas                               | Listas                    |
|--------------------------------------|---------------------------|
| Colección ***finita*** de objetos          | Colección ***infinita***        |
| Delimitado por `()` (opcional) | Delimitado por `[]`        |
| No es mutable.                       | **Mutable**                   |


---

# Inmutabilidad de tuplas

```python
>>> t = (1, 2, 3, 4)
>>> t[1] = 27
Traceback ...
``` 

---

# Mutando listas

```python
>>> t = [1, 2, 3, 4]
>>> t[1] = 27
>>> t
[1, 27, 3, 4]
>>> t.append(33)
>>> t
[1, 27, 3, 4, 33]
>>> t.insert(2, 400)
>>> t
[1, 27, 400, 3, 4, 33]
```
---


```python 
>>> t = [1, 27, 400, 3, 4, 33]
>>> t.pop()
33
>>> t
[1, 27, 400, 3, 4]
>>> t.remove(27)
[1, 400, 3, 4]
>>> t.sort()
>>> t
[1, 3, 4, 400]
>>> t.reverse()
>>> t
[400, 4, 3, 1]
```