# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv
# import os

# load_dotenv()

# print('APPP',os.environ.get('APP_SETTINGS'))
 
# app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# @app.route("/")
# def hola():
#   return "Hola mundo"

# @app.route("/name/<name>")
# def get_book_name(name):
#   return "name : {}".format(name)

# @app.route("/details")
# def get_book_details():
#   author=request.args.get('author')
#   published=request.args.get('published')
#   return "Author : {}, Published: {}".format(author,published)

# if __name__ == "__main__":
#   app.run(debug=True)