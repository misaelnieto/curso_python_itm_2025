---
marp: true
title: Estructuras de control de flujo
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Estructuras de control de flujo

### 2005 - Instituto Tecnológico de Mexicali

![bg right](imagenes/control-flujo.jpg)

---

<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Uso de if-then-else en Python

Python usa `if`, `elif` (abreviatura de "else if") y `else` para controlar el flujo del programa según condiciones.

Ejemplo:

```python
edad = 20

if edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")
```

---

# Operación ternaria

También existe la expresión condicional ternaria (en una línea):


```python
resultado = "Es par" if numero % 2 == 0 else "Es impar"
```

---

# Uso de bucles `for`

El bucle `for` en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena o rango) o cualquier objeto que sea ***iterable***. La sintaxis básica es:

```python
for elemento in iterable:
    # Código a ejecutar en cada iteración
```

---

# Iteración sobre una cadena y un rango

<div class="columnas">
<div class="col">

- Directamente sobre una cadena
    ```python
    cadena = "Python"
    for caracter in cadena:
        print(caracter)
    ```

</div>
<div class="col">

- Iterando sobre un rango:
    ```python
    for i in range(5):  # Itera del 0 al 4
        print(i)
    ```

</div>
</div>


---

# Iteración sobre listas

<div class="columnas">
<div class="col">

- Iterando directamente sobre una lista

    ```python
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(fruta)
    ```

</div>
<div class="col">

- Iterando con enumeración

    ```python
    frutas = ["manzana", "banana", "cereza"]
    for indice, fruta in enumerate(frutas):
        print(f"Índice {indice}: {fruta}")
    ```

</div>
</div>

---

# Saltos con `continue`

La sentencia `continue` hace que el bucle salte directamente a la siguiente iteración

```python
for num in range(2, 10):
    if num % 2 == 0:
        print(f"{num} es par")
        continue
    print(f"{num} es impar")

2 es par
3 es impar
4 es par
5 es impar
6 es par
7 es impar
8 es par
9 es impar
```

---

# Rompiendo el bucle con `break`

`break` sirve para terminar la iteración inmediatamente

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n//x)
            break

4 es igual a 2 * 2
6 es igual a 2 * 3
8 es igual a 2 * 4
9 es igual a 3 * 3
```

---

# Blucle for con sentencia `else`

<div class="columnas">
<div class="col">

En un bucle `for`, se puede usar la cláusula `else` para ejecutar instrucciones **después de que el bucle termina su iteración final**, con la condición de que el bucle haya terminado por causa de un `break`, una excepción o `return`.


</div>
<div class="col">

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'es un número primo')

2 es un número primo
3 es un número primo
4 es igual a 2 * 2
5 es un número primo
6 es igual a 2 * 3
7 es un número primo
8 es igual a 2 * 4
9 es igual a 3 * 3
```

</div>
</div>


---

# Bucles con `while`

## Bucle básico

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Al igual que en el bucle `for`, es posible usar `break`, `continue` y `else`.

---

# La sentencia `match`

Introducido en Python 3.10, `match` permite la coincidencia de patrones, comparando un valor con múltiples patrones definidos en bloques `case`.

```python
match valor:
    case patron1:
        # Código a ejecutar si valor coincide con patron1
    case patron2:
        # Código a ejecutar si valor coincide con patron2
    case _: # Caso por defecto
        # Código a ejecutar si no coincide ningún patrón anterior
```

---

# Ejemplo de `match` con valores literales

```python
estado = "conectado"
match estado:
    case "conectado":
        print("Usuario conectado.")
    case "desconectado":
        print("Usuario desconectado.")
    case "esperando":
        print("Usuario en espera.")
    case _:
        print("Estado desconocido.") #Caso por defecto
```

---

# Ejemplo de `match` con múltiples valores (OR implícito)

```python
comando = "cerrar"
match comando:
    case "cerrar" | "salir" | "fin": 
    #Equivalente a comando == "cerrar" or comando == "salir" or comando == "fin"
        print("Cerrando la aplicación.")
    case _:
        print("Comando no reconocido.")
```

---

# Ejemplo de `match` con patrones de secuencias

Se pueden capturar valores dentro de un patrón y usarlos dentro del bloque `case`

```python
punto = (10, 20)
match punto:
    case (0, 0):
        print("Origen.")
    case (x, 0): #Captura el valor de la x
        print(f"Eje X, x={x}.")
    case (0, y): #Captura el valor de la y
        print(f"Eje Y, y={y}.")
    case (x, y): #Captura el valor de la x e y
        print(f"Punto en x={x}, y={y}.")
```

La sentencia `match` es una herramienta potente para simplificar el código con múltiples condiciones, especialmente cuando se trabaja con estructuras de datos complejas

---

# Manejo de excepciones

`try` se utiliza para manejar excepciones, evitando que el programa falle abruptamente.

```python
try:
    # Código que podría generar una excepción
except TipoDeExcepcion:
    # Código para manejar la excepción si ocurre
except OtraExcepcion:
    #Código para manejar otra excepción diferente] #Se pueden poner varios except para diferentes excepciones.
else:
    # Código que se ejecuta si NO hay excepciones
finally:
    # Código que se ejecuta SIEMPRE, haya o no excepción
```

---

# Ejemplo más simple de manejo de excepciones

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero.")
```

---

# Manejo de múltiples excepciones


```python
try:
    valor = int(input("Introduce un número: "))
    resultado = 10 / valor
except ZeroDivisionError:
    print("Error: división por cero.")
except ValueError:
    print("Error: entrada no válida. Debes introducir un número.")
```


---

# Manejor de excepciones con `else` y `finally`

```python
try:
    f = open("archivo.txt", "r")
    contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Contenido del archivo:", contenido)
    f.close() #Es mejor ponerlo en el finally para asegurar que se cierra el archivo.
finally:
    try:
        f.close()
        print("Cerrando el archivo.")
    except NameError:
        pass #Si f no se abrio por un error anterior, no existe y daria error al intentar cerrarlo.
```
---

# Puntos importantes:

- Se pueden especificar múltiples bloques `except` para diferentes tipos de excepciones.
- El bloque `else` se ejecuta solo **si el bloque `try` se completa sin excepciones**.
- El bloque `finally` se ejecuta **siempre**, independientemente de si se produce una excepción o no. Se usa típicamente para liberar recursos (como cerrar archivos).
- Si no se especifica el tipo de excepción en el except (ej: `except:`), captura cualquier excepción, lo cual generalmente **no es una buena práctica porque dificulta la depuración**. Es mejor ser específico con los tipos de excepción que se esperan.

---

# Siguiente: [Funciones →](202-Funciones.md)