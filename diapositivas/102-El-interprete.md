---
marp: true
title: El intérprete de Python
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## El intérprete de Python

### 2005 - Instituto Tecnológico de Mexicali

![bg right](imagenes/interpretes-3.jpg)

---

<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# El intérprete de Python

Al igual que PHP, Ruby, PowerShell o Groovy, Python es un lenguaje interpretado.

***CPython*** es la implementación por defecto y más utilizada del lenguaje de programación Python

- https://github.com/python/cpython 
- Escrito en C
- Se compila a *bytecode* intermedio

---

# Funcionamiento del intérprete

![El intérprete de Python](imagenes/interprete-4.png)

---

# Implementaciones alternativas


- [IronPython](https://ironpython.net/) para **.NET**
- [MicroPython](https://micropython.org/): Python dentro de microcontroladores.
- [RustPython](https://rustpython.github.io/): Implementación de Python en Rust.
  - Python empotrado en programas escritos en Rust.
  - Compilar programas de Python a Webassembly
  


---

# Actividad

## Ejecutando un programa de Python directamente con el interprete

---

# Hola mundo

- Crea un archivo `hola.py`
- Escribe la siguiente línea de código:
```python
print('Hola desde Python')
```

- Guarda los cambios
- Toma nota de la ruta completa al archivo (p.ej. `C:\Users\MiUsuario\Documentos\hola.py`)


---

# Determinar la ruta al intérprete de python

En Windows/Powershell usar `Get-Command python.exe`

```powershell
PS C:\Users\nniet> Get-Command python.exe

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Application     python.exe                                         3.13.11... C:\Users\nniet\AppData\Local\Programs\Python\Python313\python.exe
```

En Linux/OSX usar `which python3`

```bash
$ which python3
/usr/bin/python3
```

---

# Varias maneras de correr `hola.py`

Nombre del interprete de python + ruta al script. 
  - Windows:
  ```powershell
   python.exe C:\Users\nniet\Documents\hola.py
   ```
  - Linux/OSX:
  ```bash
   python3 /home/nnieto/hola.py
   ```

---

# Varias maneras de correr `hola.py`

Interprete de python y nombre del script relativo al directorio actual 
  - Windows:
  ```powershell
   cd C:\Users\nniet\Documents\
   python.exe hola.py
   ```
  - Linux/OSX:
  ```bash
   cd /home/nnieto/
   python3 hola.py
   ```

---

# Varias maneras de correr `hola.py`

Ruta completa al intérprete de python y nombre del script relativo al directorio actual

  - Windows:
  ```powershell
   cd C:\Users\nniet\Documents\
   C:\Users\nniet\AppData\Local\Programs\Python\Python313\python.exe hola.py
   ```
  - Linux/OSX:
  ```bash
   cd /home/nnieto/
   /usr/bin/python3 hola.py
   ```

---

# Varias maneras de correr `hola.py`

Ruta completa al intérprete de python y ruta completa al script.

  - Windows:
  ```powershell
   C:\Users\nniet\AppData\Local\Programs\Python\Python313\python.exe C:\Users\nniet\Documents\hola.py
   ```
  - Linux/OSX:
  ```bash
   /usr/bin/python3 /home/nnieto/hola.py
   ```

---

# Varias maneras de correr `hola.py`

## Sin `hola.py`


  - Windows:
  ```powershell
   C:\Users\nniet\AppData\Local\Programs\Python\Python313\python.exe -c "print('Hola desde Python')"
   ```
  - Linux/OSX:
  ```bash
   /usr/bin/python3 -c -c "print('Hola desde Python')"
   ```

---

# Varias maneras de correr `hola.py`

## Como un script ejecutable

- Usando un comentario mágico llamado shebang (`#!`)
- Este debe estar definido en la primera linea del script.
- No es específico de python, puede ser bash, php, perl o cualquier otro intérprete.

```python
#!/usr/bin/python3
print('Hola desde Python')
```

Pero es mejor usar /usr/bin/env para que funcione en todo tipo de configuraciones.


```python
#!/usr/bin/env python
print('Hola desde Python')
```

---

# Varias maneras de correr `hola.py`

## Como un script ejecutable

Adicionalmente, en Linux/OSX es necesario marcar el archivo como ejecutable.

```bash
chmod +x hola.py
./hola.py
```

---

# Siguiente: [Sintaxis básica de Python →](103-Sintaxis-basica.md)