from flask import Flask, render_template, request
from flask_restful import Api

from resources.product import Product
from utils.search import product_search, pick_search


app = Flask(__name__)
api = Api(app)

api.add_resource(Product, '/product/<pid>', '/product/')

@app.route('/search')
def search():
    query = request.args.get('q')
    price = request.args.get('priceRange')
    screen = request.args.get('Size')
    ram = request.args.get('Ram')
    product_result = product_search(query=query, price=price, screen=screen, ram=ram)
    post_result = pick_search(query=query, price=price, screen=screen, ram=ram)
    result = {'products': product_result, 'posts':post_result, 'q':query, 'price':price, 'screen':screen, 'ram':ram}
    return render_template('index.html', context=result)

@app.route('/')
def index():
    return render_template('index.html', context={'price':'0', 'screen':'0', 'ram':'0'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
