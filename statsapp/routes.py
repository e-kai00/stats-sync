from flask import jsonify
import requests
from statsapp import app
from statsapp import SHOPIFY_API_BASE_URL, SHOPIFY_HEADERS 


@app.route('/get-shopify-data', methods=['GET'])
def get_shopify_data():

    order_query_params = {
        'status': 'any',
        'created_at_min': '2023-09-31T15:57:11-04:00',
        'fields': 'id,created_at,subtotal_price,total_price,total_tax,total_shipping_price_set,line_items'
    }

    shopify_response = requests.get(
        f"{SHOPIFY_API_BASE_URL}/orders.json",
        params=order_query_params,
        headers=SHOPIFY_HEADERS
    )

    print(shopify_response.url)
    orders = shopify_response.json()

    for order in orders.get('orders', []):

        order_id = order.get('id', None)
        order_total = order.get('total_price', None)
        order_subtotal = order.get('subtotal_price', None)
        shipping = order.get('total_shipping_price_set', {}).get('shop_money', {}).get('amount', None)
        
        for line_item in order.get('line_items', []):
            sku = line_item.get('sku', None)


        print(
            f'Order ID: {order_id}, Order total: {order_total}, Order subtotal: {order_subtotal}, Shipping: {shipping}, SKU: {sku}' 
        )

    return orders
   



# TenderTransaction
# orders: orders.json?status=any&fields=id,...
    #    {
    #   "id": 5580255101088
    # },
    # {
    #   "id": 5566800396448
    # },
    # {
    #   "id": 5465509986464
    # },
    # {
    #   "id": 5421844693152
    # },
# handle errors


# @app.route('/get_products', methods=['GET'])
# def get_products():
#     try:
#         # Make a request to get a list of products
#         products = shopify.Product.find()

#         # Extract relevant information from the products
#         product_data = []
#         for product in products:
#             product_data.append({
#                 'id': product.id,
#                 'title': product.title,
#                 'price': product.variants[0].price,
#             })

#         return jsonify({'products': product_data})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500