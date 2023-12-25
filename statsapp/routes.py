from flask import jsonify
import shopify
from statsapp import app


@app.route('/get_products', methods=['GET'])
def get_products():
    try:
        # Make a request to get a list of products
        products = shopify.Product.find()

        # Extract relevant information from the products
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'title': product.title,
                'price': product.variants[0].price,
            })

        return jsonify({'products': product_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500