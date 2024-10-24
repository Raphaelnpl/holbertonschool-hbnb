from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Bienvenue dans l'API HBnB !"

if __name__ == '__main__':
    app.run(debug=True)
