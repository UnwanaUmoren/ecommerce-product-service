from flask import Flask


app = Flask(__name__)

@app.route('/')
def homepage():
    return ("Welcome to Wannie's E-commerce website")

@app.route('/products')
def products():
    return [
        {'id': 1, 'name':'Sweatshirt', 'price':'£30.99'},
        {'id': 2, 'name':'Jeans', 'price':'£49.99'},
        {'id': 3, 'name':'Jacket', 'price':'£89.99'}
    ]

if __name__ == '__main__':
    app.run(host='0.0.0.0')