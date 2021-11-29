from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

USER_DB = 'postgres'
PASS_DB = ''
HOST_DB = 'localhost'
NAME_DB = 'sap'
PORT_DB = '5432'

URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{HOST_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
  print(f'Index { request.query_string }')
  return '<h1>Página de inicio</h1>'

# print('app', app)
if __name__ == '__main__':
  app.run(port='3333', debug=True)


class Persona(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(250))
  apellido = db.Column(db.String(250))
  email = db.Column(db.String(250))

  def __str__(self):
    return (
      f'Id: {selt.}'
    )
