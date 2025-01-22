---
marp: true
title: Aplicación web con Flask
author: Noe Nieto
theme: curso-python
---

# Aplicaciones web con Python

## Aplicación web con Flask

### 2005 - Instituto Tecnológico de Mexicali

#### https://tinyurl.com/pyitm2025

![bg right](imagenes/flask.jpg)

---

<!--
paginate: true
header: Aplicaciones web con Python
footer: Instituto Tecnológico de Mexicali
-->

# Aplicación web con Flask

- [Flask](https://flask.palletsprojects.com/en/stable/)
  - Servidor web
  - Plantillas html (Jinja)
  - CLI
- [Flask-Restless](https://flask-restless.readthedocs.io/en/stable/)
  - [SQLAlchemy](https://www.sqlalchemy.org/)

---

# Proyecto: alcancía

- Alcancía es una aplicacion web que
  - Mantiene un balance del dinero que contiene
  - Registra depósitos
  - Registra retiros

---

# Creación del proyecto

Creamos el proyecto inicial con `uv`

```
uv init alcancia
cd alcancia
uv run .\hello.py
```

Instalamos Flask

```
uv add Flask
```



---

# Hola Mundo en flask

- Creamos `app.py` con el siguiente contenido
  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route("/")
  def hello_world():
      return "<p>Bienvenido a mi alcancia!</p>"
  ```
- Levantamos el servidor de Flask
  ```
  uv run flask run --debug
  ```
- Abrir http://127.0.0.1:5000

---

# Rutas

<div class="columnas">
<div class="col">

- `/` > Raiz de la aplicacion. Muestra el balance
- `/deposito` > Hacer un deposito
- `/retiro` > Hacer un retiro
- `/movimientos` > Histórico de movimientos

</div>
<div class="col">

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def saldo():
    return "<p>Bienvenido a mi alcancia!</p><p>Tenemos <b>$0.00</b> pesos</p>"


@app.route("/deposito")
def deposito():
    return "<p>Aqui podras hacer un deposito</p>"


@app.route("/retiro")
def retiro():
    return "<p>Aqui podras hacer un retiro</p>"


@app.route("/movimientos")
def movimientos():
    return "<p>Lista de movimientos</p>"
```

</div>
</div>

Reiniciamos flask y probamos las rutas en el navegador.

---


# Plantillas

- Flask usa [Jinja2](https://jinja.palletsprojects.com/en/stable/)
  - Herencia de plantillas, macros, autoescape, cacheo, etc.
- Las plantillas se buscan en `templates` (relativo a `app.py`)

Layout de plantillas:

- `base.html` -> Estructura comun de las demas.
- `saldo.html`
- `deposito.html`
- `retiro.html`
- `movimientos.html`

---


# Plantilla base

- Flask no tiene un framework CSS, ni JS.
- Usaremos BulmaCSS. https://bulma.io/documentation/start/overview/#starter-template
- Copiar el starter template y guardarlo en `base.html`
- Modificar `base.html` para agregar los placeholders de:
  - Titulo
  - Contenido

---

# Plantilla de saldo

- Crear `saldo.html`
  - No olvidar mostrar el valor de la variable `saldo`.
- Modificar la ruta de saldo para usar la plantilla
  ```python
  from flask import render_template

  @app.route("/")
  def saldo():
      return render_template('saldo.html', saldo=0.0)

  ```


---

# Plantilla de deposito

- Crear `deposito.html`
- Modificar la ruta de saldo para usar la plantilla
  ```python
  from flask import render_template

  @app.route("/")
  def deposito():
      return render_template('deposito.html')

  ```

---

# Plantilla de retiro

- Crear `retiro.html`
- Modificar la ruta de saldo para usar la plantilla
  ```python
  from flask import render_template

  @app.route("/")
  def retiro():
      return render_template('retiro.html')

  ```

---

# Plantilla de movimientos

- Crear `movimientos.html`
- Modificar la ruta de saldo para usar la plantilla
  ```python
  from flask import render_template

  @app.route("/")
  def movimientos():
      return render_template('movimientos.html')

  ```

---

# Mensajes flash

Muy últiles para dar retroalimentación al usuario.

<div class="columnas">
<div class="col">

- Configuración en Python
  ```python
  from flask import flash


  app = Flask(__name__)
  app.secret_key = b'SVVMH3-lx0x1_jQ9LfBLWjo%qP'

  ```

</div>
<div class="col">

- Configuración en `base.html`
  ```html
        <div class="content">
          <div class="block">
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                <div class="notificaciones">
                {% for category, message in messages %}
                  <div class="notification {{ category }}">
                    <button class="delete"></button>
                    {{ message }}
                  </div>
                {% endfor %}
                </div>
              {% endif %}
            {% endwith %}
          </div>
          <div class="block">
            {% block contenido %}{% endblock %}
          </div>
        </div>
  ```
</div>
</div>


---
# Formularios

- Especificar methods en `app.route()`: `POST` y `GET`.
- Flask define un objeto global llamado `request`.
- El tipo de petición esta disposible desde `request.method`
- Los datos del formulario estan en `request.form`.

![bg right h:100% h:90%](imagenes/formulario.png)

---

# Primer formulario: `/deposito` - plantilla

<div class="columnas">
<div class="col">

- Mensajes flash
  ```html
    <form method="POST">
      {% if error %}
      <article class="message is-danger">
          <div class="message-body">
              Cantidad invalida
          </div>
      </article>
      {% endif %}
      <div class="field has-addons">
        ...
      </div>
    </form>
  ```


</div>
<div class="col">

- Formularios
  ```html
    <form method="POST">
      {% if error %}
      ...
      {% endif %}
      <div class="field has-addons">
          <div class="control">
              <input class="input is-large" 
              type="number"
              min="0" 
              step="0.01" 
              placeholder="$ 0.00" 
              name="cantidad">
          </div>
          <div class="control">
              <input type="submit" value="&#x1FA99; Depositar"
              class="button is-info is-large">
          </div>
      </div>
    </form>
  ```


</div>
</div>


---

# Primer formulario: `/deposito` - Python

<div class="columnas">
<div class="col">

```python
@app.route("/deposito")
def deposito():
    return render_template('deposito.html')
```

</div>
<div class="col">

```python
from flask import request, flash

@app.route("/deposito", methods=['POST', 'GET'])
def deposito():
    error = ''
    if request.method == 'POST':
        cantidad = request.form.get('cantidad', 0, type=int)
        if not cantidad:
            error = "Cantidad invalida"
        else:
            flash(f'Depositaste ${cantidad}')
    return render_template('deposito.html', error=error)

```

</div>
</div>

---

# Actividad

Hacer el formulario de retiro

---

## Listado de movimientos: plantilla

```html
{% block contenido %}
  <table class="table is-bordered is-hoverable is-fullwidth">
    <thead>
      <tr>
        <td class="is-primary">Fecha</td>
        <td class="is-info">Cantidad</td>
      </tr>
    </thead>
    <tbody>
      {% for m in movimientos %}
      <tr>
        <td>{{ m.fecha }}</td>
        <td>{{ "${:,.2f}".format(m.cantidad) }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

---

## Listado de movimientos - Python

<div class="columnas">
<div class="col">

```python
from flask import render_template

@app.route("/")
def movimientos():
    return render_template('movimientos.html')

```

</div>
<div class="col">

```python
  from datetime import datetime

  @app.route("/movimientos")
  def movimientos():
      return render_template('movimientos.html', movimientos=[
          {'fecha': datetime(year=2025, month=1, day=1), 'cantidad': 10},
          {'fecha': datetime(year=2025, month=1, day=2), 'cantidad': 10},
          {'fecha': datetime(year=2025, month=1, day=3), 'cantidad': 10},
          {'fecha': datetime(year=2025, month=1, day=4), 'cantidad': 10},
          {'fecha': datetime(year=2025, month=1, day=5), 'cantidad': -30},
      ])
```
</div>
</div>

---

# Lo que tenemos hasta ahora

- Aplicación básica con 4 rutas
- Plantilla base configurada
- Reporte de saldo
- Dos formularios: depósitos y retiros
- Reporte de movimientos

## Lo que sigue

- Persistencia de datos

---

# SQLAlchemy

<div class="columnas">
<div class="col">

![sql alchemy](imagenes/sqla_arch_small.png)

</div>
<div class="col">

- ORM para Python
- Dialectos soportados: **SQLite**, Postgresql, MySQL/MariaDB, Oracle, MS SQLServer. +30 dialectos soportados mediante librerías externas.
- **Flask-SQLAlchemy**: integración de Flask con modelos de SQLAlchemy
</div>
</div>

### Instalación

```sh
uv add Flask-SQLAlchemy
```

---

# Configurar ORM

<div class="columnas">
<div class="col">

- Importar `SQLAlchemy` y `click`
- Definir URI de la base de datos
- Escribir clase para `Movimiento`
- Escribir script para inicializar la bd
  - Correr script
  - Verificar que la bd se escribió

</div>
<div class="col">

```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import click

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alcancia.db"
db = SQLAlchemy(app)


class Movimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, server_default=func.now())
    cantidad = db.Column(db.Numeric)


@app.cli.command()
def initdb():
    """
    Inicializa la base de datos de la alcancia
    """
    click.echo('Inicializando la base de datos')
    db.create_all()
```

</div>
</div>


---

# Persistir datos en la BD: depósitos

```python
depo = Movimiento(cantidad=cantidad)
db.session.add(depo)
db.session.commit()
```


---


# Actividad

Implementar la ruta de retiros

---

# Reporte de saldo



# Siguiente: [Agregando un API Rest →](302-REST.md)