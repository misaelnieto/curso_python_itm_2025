---
marp: true
title: 02 - Configuración e instalación
---
# Aplicaciones web con Python

## Enero 2025

### Instituto Tecnológico de Mexicali

---
<!--
theme: default
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# 02

## Entorno de desarrollo

---

# Instalacion de Python en Windows

- python.org
- winget
- WSL

---

# Instalacion de Python en Windows - Python.org


- Descargar instalador Python desde www.python.org
- Tomar nota de la ruta de instalación de Python
- Configurar variable PATH para incluir Python

---

# Instalacion de Python en Windows - Winget

```powershell
winget install Python3
```

Ventajas:

- Descarga el instalador msi desde Python.org
- Configura la ruta de instalación de Python

Nota:

- Reiniciar la sesión de Powershell despues de instalar Python para acceder al comando `python.exe`.

---

# Instalacion de Python en Windows - WSL

Si WSL aun no está instalado:

```powershell
wsl --install
```

Con WSL instalado:

```powershell
wsl
```

Para entrar en Ubuntu y luego

```bash
python3
```

---

# Instalación de Python en OSX

- https://www.python.org/downloads/
- Brew
  ```
  brew install python@3.13
  ```

---

# Instalacion en Linux

- Ubuntu LTS
  - https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
- Fedora
  ```
  sudo dnf update
  sudo dnf install python3.13
  ```

---

# Configuración del editor

- Python no esta asociado a ningún editor ni IDE en específico. Se puede usar cualquier editor de texto.
- En Windows se instala IDLE.
- Otras opciones populares son VSCode o pycharm
- **Pero es imprescindible saber ejecutar los scripts de python desde la línea de comandos**.


---

# Actividad

## Ejecutando un programa de Python directamente con el interprete

---

# Hola mundo

```python
print('Hola desde Python')
```

- Guardar en un archivo `hola.py`
- tomar nota de la ruta completa al archivo (p.ej. `C:\Users\\MiUsuario\Documentos\hola.py`)


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

En Windows no funciona tan bien :(

