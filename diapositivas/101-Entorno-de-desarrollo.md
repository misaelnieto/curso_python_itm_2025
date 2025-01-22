---
marp: true
title: Entorno de desarrollo
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Configuración del entorno de desarrollo

### 2005 - Instituto Tecnológico de Mexicali

#### https://tinyurl.com/pyitm2025

![bg right](imagenes/entorno_desarrollo.jpg)

---
<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# El entorno de desarrollo de Python

![center height:10em](imagenes/interpretes-1.png)

---

# El entorno de desarrollo de Python

![center height:10em](imagenes/interpretes-2.png)

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

# Google colab


[Link a ejercicios de Google Colab](https://colab.research.google.com/drive/189BymFCmRaTJ_MpRALe1X9bUvETRRqjR?usp=sharing).


---

# Siguiente: [El intérprete de Python →](102-El-interprete.md)