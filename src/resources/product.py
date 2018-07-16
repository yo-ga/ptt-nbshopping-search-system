from flask_restful import Resource

class Product(Resource):
    def get(self, pid=None):
        if pid:
            return {'pid': pid,
                    'product_name': 'Computer',
                    'product_link': 'www.google.com',
                    'product_price': 500,
                    'product_content': 'Just test'}
        else:
            return {}