from flask import Flask, request, render_template

from sqlalchemy.orm import Session

from hw_21_flask_contract.db import Product, engine

app = Flask(__name__)


@app.route('/product', methods=['POST', 'GET'])
def get_products():
    if request.method == 'GET':
        with Session(engine) as sss:
            products = sss.query(Product).all()
        return render_template('products.html', products=products)

    elif request.method == 'POST':
        product = Product(**request.form)
        with Session(engine) as sss:
            sss.add(product)
            sss.commit()

            products = sss.query(Product).all()
        return render_template('products.html', products=products)
