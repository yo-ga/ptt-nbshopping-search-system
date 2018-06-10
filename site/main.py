from flask import Flask, render_template
from flask_restful import Api

from resources.product import Product


app = Flask(__name__)
api = Api(app)

api.add_resource(Product, '/product/<pid>', '/product/')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
