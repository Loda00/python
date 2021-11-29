from flask import Flask, request, render_template, url_for, abort, jsonify, session
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'

@app.route('/')
def home():
  # app.logger.info(f'A nivel info { request.path }')
  # app.logger.debug('A nivel debug')
  # app.logger.warning('A nivel warning')
  # app.logger.error('A nivel error')
  # return render_template('home.html', env = 'development 1')
  if 'username' in session:
    return 'Logueado'
  return 'Logueese'

@app.route('/test')
def test():
  print('query string' , str(request.query_string.decode("utf-8")).split("&"))
  return 'Vista de prueba'

@app.route('/saludar/<nombre>')
def saludar(nombre):
  return f'Saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def edad(edad):
  return f'Tu edad es : {edad}'

@app.route('/mostrar/<nombre>', methods=['POST'])
def mostrar(nombre):
  return f'Tu nombre es: {nombre}'

@app.route('/redirect')
def redireccionar():
  return redirect(url_for('saludar', nombre='Teofilo'))

@app.route('/exit')
def exit():
  return abort(404)

@app.errorhandler(404)
def notFound(error):
  return (render_template('notFound.html', error=error), 404)
# request.get_json()
@app.route('/api/<name>')
def api(name):
  array = {
    'reply': [
      {
        'id': 1,
        'name': 'Juan'
      },
      {
        'id': 2,
        'name': 'Chato'
      },
      {
        'id': 2,
        'name': name.capitalize()
      }
    ]
  }
  return jsonify(array)



if __name__ == '__main__':
  app.run(debug = True)