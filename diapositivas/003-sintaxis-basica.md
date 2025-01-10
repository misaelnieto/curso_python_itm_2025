---
marp: true
title: 03 - Sintaxis básica
---
# Aplicaciones web con Python

## Enero 2025

### Instituto Tecnológico de Mexicali

<!--
theme: default
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

---

# Sintaxis básica de Python

---

# Resumen de la sintaxis de Python

- Un programa de Python esta dividido en líneas
- Las líneas vacías se ignoran
- Los comentarios comienzan con el caracter `#` 
- **Los bloques de código se delimitan con espacios y tabuladores**.
- Los símbolos se separan con espacios.



---

# Un programa de Python esta dividido en líneas


```python
el_mundo_es_plano = True
dos_mas_dos = 5
print("Hola mundo")
```

---

# Las líneas vacías se ignoran

```python
el_mundo_es_plano = True


dos_mas_dos = 5

print("Hola mundo")
```

---

# Los comentarios comienzan con el caracter `#` 


```python
# Esta variable es un booleano
el_mundo_es_plano = True

# Otro comentario
dos_mas_dos = 5

print("Hola mundo")  # Los comentarios terminan hasta el fin de linea
```

---

# Los bloques de código se delimitan con espacios y tabuladores

```python
dos_mas_dos = 5
if dos_mas_dos == 4:
    forma = "redonda"
else:
    forma = "plana"

print(f"La tierra es {forma})
```

