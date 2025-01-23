---
marp: true
title: Agregando un API REST
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Agregando un API REST

### 2005 - Instituto Tecnológico de Mexicali

#### https://tinyurl.com/pyitm2025

![bg right](imagenes/rest.jpg)

---

<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Agregar las siguientes rutas:

- `/api/v1/saldo` -> **GET** -> `{saldo:1.0}`
- `/api/v1/deposito` -> **POST** > `{cantidad: 1.0}`
- `/api/v1/retiro` -> **POST** > `{cantidad: 1.0}`
- `/api/v1/movimientos` -> **GET** > `{movimientos:[ {fecha: '2025-01-02 20:37', cantidad: 1.0}, ...]}`

> **Magia**: Cuando una ruta en flask regresa un diccionario, flask lo serializara a json.

---

# Actividad: Conectar frontend de React

---

# Siguiente: [Despliegue de la aplicación →](303-Deploy.md)