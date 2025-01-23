from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import flash

app = Flask(__name__)
app.secret_key = b'SVVMH3-lx0x1_jQ9LfBLWjo%qP'


##############################################
# ORM

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


##############################################
# Rutas

@app.route("/")
def saldo():
    return render_template(
        'saldo.html',
        saldo=db.session.scalar(func.sum(Movimiento.cantidad))
    )


@app.route("/deposito", methods=['POST', 'GET'])
def deposito():
    error = False
    if request.method == 'POST':
        cantidad = request.form.get('cantidad', 0, type=int)
        if not cantidad:
            flash(f'Invalido', 'is-danger')
        else:
            depo = Movimiento(cantidad=cantidad)
            db.session.add(depo)
            db.session.commit()
            flash(f'Depositaste ${cantidad}', 'is-success')
    return render_template('deposito.html', error=error)


@app.route("/retiro", methods=['POST', 'GET'])
def retiro():
    error = False
    if request.method == 'POST':
        cantidad = abs(request.form.get('cantidad', 0, type=int)) * - 1
        if not cantidad:
            flash(f'Invalido', 'is-danger')
        else:
            depo = Movimiento(cantidad=cantidad)
            db.session.add(depo)
            db.session.commit()
            flash(f'Retiraste ${cantidad}', 'is-success')
    return render_template('retiro.html', error=error)


@app.route("/movimientos")
def movimientos():
    q = db.session.execute(db.select(Movimiento).order_by(Movimiento.fecha))
    return render_template('movimientos.html', movimientos=q.scalars())

##############################################
# Rutas JSON

@app.route("/api/v1/saldo")
def api_saldo():
    return {
        'saldo': db.session.scalar(func.sum(Movimiento.cantidad))
    }


@app.route("/api/v1/deposito", methods=['POST'])
def api_deposito():
    payload = request.get_json()
    response = {}
    if 'cantidad' in payload:
        db.session.add(
            Movimiento(cantidad=abs(float(payload['cantidad'])))
        )
        db.session.commit()
        response['status'] = 'OK'
    else:
        response['status'] = 'FAIL'
        response['message'] = 'Cantidad es requerido'

    return response


@app.route("/api/v1/retiro", methods=['POST'])
def api_retiro():
    payload = request.get_json()
    response = {}
    if 'cantidad' in payload:
        db.session.add(
            Movimiento(cantidad=-abs(float(payload['cantidad'])))
        )
        db.session.commit()
        response['status'] = 'OK'
    else:
        response['status'] = 'FAIL'
        response['message'] = 'Cantidad es requerido'

    return response


@app.route("/api/v1/movimientos")
def api_movimientos():
    q = db.session.execute(db.select(Movimiento).order_by(Movimiento.fecha))
    movimientos = []
    for m in q.scalars():
        movimientos.append({
            'fecha': m.fecha,
            'cantidad': m.cantidad
        })
    return {'movimientos': movimientos}
