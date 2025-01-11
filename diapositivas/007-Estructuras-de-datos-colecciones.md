---
marp: true
title: "07 - Estructuras de datos: Colecciones"
---

# Aplicaciones web con Python

## Enero 2025

### Instituto Tecnológico de Mexicali

#### 07 - Estructuras de datos: **Colecciones**

---
<!--
theme: default
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Estructuras de datos: Colecciones

- Propósito general: `list`, `tuple`, `set`, `dict`
- Propósito específico: `named_tuple()`, `deque`, `ChainMap`, `Counter`, `OrderedDict`, `UserDict`, `UserList`, `UserString`.



---

# Estructuras de datos: Conjuntos (`set`)

- En Python es una secuencia de objetos únicos, separados por comas y delimitados por `{}`. El orden no está garantizado.
- Operaciones soportadas más comunes:
  - pertenencia/no pertenencia al conjunto
  - subconjunto/superconjunto
  - Union
  - Intersección
  - diferencia

---

# Creacion de conjuntos

```python
>>> frutas = set()
>>> frutas
{}

>>> type(frutas)
<class 'set'>

# Usar corchetes vacíos crea un dict
>>> frutas = {}
>>> type(frutas)
<class 'dict'>
```

---

# Los conjuntos eliminan duplicados automaticamente

```python
>>> frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
>>> frutas
{'manzana', 'naranja', 'pera', 'banana'}
```



---

# Pertenencia/no pertenencia de conjuntos

```python
>>> frutas
{'manzana', 'naranja', 'pera', 'banana'}
```

## Pertenencia

Usando el operador `in`

```python
>>> # Tenemos uvas?
>>> 'uvas' in frutas
False
```
---

# Pertenencia/no pertenencia de conjuntos

```python
>>> frutas
{'manzana', 'naranja', 'pera', 'banana'}
```

## No pertenencia

Usando el operador `not in`

```python
>>> # No tenemos durazno, correcto?
>>> 'durazno' not in frutas
False
```

---
# Subconjuntos

```python
>>> frutas = {'manzana', 'naranja', 'pera', 'banana'}
>>> frutas_tropicales = {'mango', 'piña', 'banana', 'maracuyá'}
```


## ¿ `frutas` es un subconjunto de `frutas_tropicales` ?

Usando el método `issubset` o el operador `<=`

```python
>>> frutas.issubset(frutas_tropicales)
False

>>> frutas <= frutas_tropicales
False
```

---

# Subconjuntos

```python
>>> frutas = {'manzana', 'naranja', 'pera', 'banana'}
>>> frutas_completas = {'manzana', 'naranja', 'banana', 'pera', 'uva', 'fresa', 'mango'}

```

## ¿ `frutas` es unsubconjunto de `frutas_completas` ?

Usando el método `issubset` o el operador `<=`

```python
>>> frutas.issubset(frutas_completas)
True

>>> frutas <= frutas_completas
True
```

---

# Superconjuntos

```python
>>> frutas = {'manzana', 'naranja', 'pera', 'banana'}
>>> frutas_completas = {'manzana', 'naranja', 'banana', 'pera', 'uva', 'fresa', 'mango'}

```

## ¿ `frutas_completas` es un superconjunto de `frutas` ?

Usando el método `issuperset` o el operador `>=`


```python
>>> frutas_completas.issuperset(frutas)
True

>>> frutas_completas > frutas
True
```

---

# Superconjuntos

```python
>>> frutas = {'manzana', 'naranja', 'pera', 'banana'}
>>> frutas_tropicales = {'mango', 'piña', 'banana', 'maracuyá'}
```

## ¿ `frutas_tropicales` es un superconjunto de `frutas` ?

Usando el método `issuperset` o el operador `>=`

```python
>>> frutas_tropicales.issuperset(frutas)
False

>>> frutas_tropicales >= frutas
False
```

---

# Superconjuntos

```python
>>> frutas = {'manzana', 'naranja', 'pera', 'banana'}
>>> frutas_tropicales = {'mango', 'piña', 'banana', 'maracuyá'}
```

## ¿ `frutas` es un superconjunto de si mismo ?

```python
>>> frutas.issuperset(frutas)
True
```

---

# Union

```python
frutas = {'manzana', 'naranja', 'pera', 'banana'}
frutas_tropicales = {'mango', 'piña', 'banana', 'maracuyá'}
frutas_completas = {'manzana', 'naranja', 'banana', 'pera', 'uva', 'fresa', 'mango'}
```

## Unión de `frutas` y `frutas_tropicales`

Usando el método `union()` o el operador `|`

```python
>>> frutas.union(frutas_tropicales)
{'manzana', 'naranja', 'piña', 'banana', 'mango', 'pera', 'maracuyá'}

>>> frutas | frutas_tropicales
{'manzana', 'naranja', 'piña', 'banana', 'mango', 'pera', 'maracuyá'}
```

---

# Union

```python
frutas = {'manzana', 'naranja', 'pera', 'banana'}
frutas_tropicales = {'mango', 'piña', 'banana', 'maracuyá'}
frutas_completas = {'manzana', 'naranja', 'banana', 'pera', 'uva', 'fresa', 'mango'}
```

## Unión de multiples conjuntos

```python
>>> frutas | frutas_tropicales | frutas_completas
{'manzana', 'naranja', 'piña', 'uva', 'fresa', 'mango', 'banana', 'pera', 'maracuyá'}
```

---

# Union

```python
frutas = {'manzana', 'naranja', 'pera', 'banana'}
frutas_tropicales = {'mango', 'piña', 'banana', 'maracuyá'}
frutas_completas = {'manzana', 'naranja', 'banana', 'pera', 'uva', 'fresa', 'mango'}
```

## Unión de un conjunto consigo mismo

```python
>>> frutas | frutas == frutas
True
```

# Union con un conjunto vacío

```python
>>> frutas | set() == frutas
True
```

---

# Estructuras de datos: Diccionarios (`dict`)

- Otros nombres: Hashmaps, memoria asociativa, arreglos asociativos
- Es un mapa de un valor ***hashable*** (**key**) a un objeto (**value**).
  - Llave (key): Cualquier objeto o valor **inmutable**: números, texto. No: `list`, `dict`
  - Valor (value): Cualquier objeto.


---

# Estructuras de datos: Diccionarios (`dict`)


- Operaciones soportadas más comunes:
  - pertenencia/no pertenencia al conjunto **de llaves**.
  - Acceso/inserción y borrado de pares llave/valor.
  - Iteración sobre llaves y valores
  - Union
  - Intersección
  - diferencia

---

# Creación de diccionarios

Mediante la funcion `dict()` o `{}`

```python
>>> dict()
{}

>>> {}
{}
```

---

# Creación de diccionarios con valores

## Creación con pares llave-valor directamente

```python
>>> dict(manzana=1.50, banana=0.75, naranja=0.90)
{'manzana': 1.5, 'banana': 0.75, 'naranja': 0.9}
```

## Creación a partir de una lista de tuplas

```python
>>> dict([('manzana', 'roja'), ('banana', 'amarilla'), ('uva', 'morada')])
{'manzana': 'roja', 'banana': 'amarilla', 'uva': 'morada'}
```

---

# Diccionario con llaves repetidas

Se queda con el ultimo valor asignado a la llave

```python
>>> dict([('manzana', 'roja'), ('banana', 'amarilla'), ('manzana', 'verde')])
{'manzana': 'verde', 'banana': 'amarilla'}
```

---

# Las llaves pueden ser cualquier objeto inmutable

```python
>>> {'foo': 'bar', 777: 'A sus ordenes jefe', 3.1416: 'pi', (1,2): 'coordenadas'}

{'foo': 'bar', 777: 'A sus ordenes jefe', 3.1416: 'pi', (1, 2): 'coordenadas'}
```

## Pero no objetos mutables

```python
>>> {(1,2): 'coordenadas'}
{(1,2): 'coordenadas'}

>>> {[1,2]: 'coordenadas'}
Traceback (most recent call last):
  File "<python-input-55>", line 1, in <module>
    {[1,2]: 'coordenadas'}
TypeError: unhashable type: 'list'
```

---

# Modificando diccionarios: agregar

**Asignación directa** con corchetes (la forma más común)

```python
frutas_origen = {}
frutas_origen['manzana'] = 'Chile'
frutas_origen['banana'] = 'Ecuador'
frutas_origen['naranja'] = 'España'
```

---

# Modificando diccionarios: agregar


Método `update()`> para agregar múltiples elementos a la vez o fusionar diccionarios.

- *Duplica* `'naranja'` con valor `'España'` (duplicado)
- Agrega `'uva'` con valor `'Perú'`
- Cambia `'manzana'`, ahora tiene valor `` 

```python
>>> frutas_origen.update({'naranja': 'España', 'uva': 'Perú', 'manzana': 'Mexico' })
>>> frutas_origen
{'manzana': 'Mexico', 'banana': 'Ecuador', 'naranja': 'España', 'uva': 'Perú'}
```

---

# Modificando diccionarios: agregar

Método `setdefault()` (agrega un elemento solo si la llave no existe)

```python
>>> frutas_origen.setdefault('banana', 'Colombia')
'Ecuador'

>>> frutas_origen
{'manzana': 'Mexico', 'banana': 'Ecuador', 'naranja': 'España', 'uva': 'Perú'}

>>> frutas_origen.setdefault('tomate', 'Canada')
'Canada'

>>> frutas_origen
{'manzana': 'Mexico', 'banana': 'Ecuador', 'naranja': 'España', 'uva': 'Perú', 'tomate': 'Canada'}
```

---

# Modificando diccionarios: eliminar

```python
frutas_origen = {'manzana': 'Chile', 'banana': 'Ecuador', 'naranja': 'España', 'uva': 'Perú'}
```

## Usando `del`

Elimina el elemento con la llave especificada.

```python
>>> del frutas_origen['naranja']
>>> frutas_origen
{'manzana': 'Mexico', 'banana': 'Ecuador', 'uva': 'Perú', 'tomate': 'Canada'}
```

---

# Modificando diccionarios: eliminar

Usar una llave que no existe genera un error.


```python
>>> del frutas_origen['mandarina']
Traceback (most recent call last):
  File "<python-input-70>", line 1, in <module>
    del frutas_origen['mandarina']
        ~~~~~~~~~~~~~^^^^^^^^^^^^^
KeyError: 'mandarina'
```


---

# Modificando diccionarios: eliminar

Usando `pop()` (elimina el elemento y devuelve su valor)

```python
>>> frutas_origen
{'manzana': 'Mexico', 'banana': 'Ecuador', 'uva': 'Perú', 'tomate': 'Canada'}

>>> origen_banana = frutas_origen.pop('banana')
>>> origen_banana
'Ecuador'

>>> frutas_origen
{'manzana': 'Mexico', 'uva': 'Perú', 'tomate': 'Canada'}

```

---

# Modificando diccionarios: eliminar

Podemos pasar a `pop()` un valor por defecto, por si la llave no existe.

```python
>>> origen_mandarina = frutas_origen.pop('mandarina', 'Desconocido')
>>> origen_mandarina
'Desconocido'
```

---

# Modificando diccionarios: eliminar

Usando `popitem()` (elimina y devuelve un par (llave, valor) arbitrario en orden LIFO.

```python
>>> frutas_precios = {'manzana': 1.50, 'banana': 0.75, 'naranja': 0.90, 'uva': 2.00}

>>> frutas_precios.popitem()
('uva', 2.0)

>>> frutas_precios['membrillo'] = 4.7
>>> frutas_precios.popitem()
('membrillo', 4.7)

>>> frutas_precios.popitem()
('naranja', 0.9)

```

---

# Modificando diccionarios: eliminar todo

Usando `clear()`

```python
>>> frutas_precios = {'manzana': 1.50, 'banana': 0.75, 'naranja': 0.90, 'uva': 2.00}
>>> frutas_precios.clear()
>>> frutas_precios
{}
```

