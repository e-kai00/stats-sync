from flask import jsonify, render_template
import requests
from requests.exceptions import RequestException
from datetime import datetime
from statsapp import app, db
from statsapp.models import Order
from statsapp import SHOPIFY_API_BASE_URL, SHOPIFY_HEADERS 
# import logging

# logging.basicConfig(level=logging.DEBUG)


def fetch_shopify_data():
    try: 
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

        shopify_response.raise_for_status()
        orders = shopify_response.json()

        return orders
    
    except RequestException as e:
        print(f'Error fetching Shopify data: {e}')
        return {'error': str(e)}

    
# def fetch_etsy_data():
    

def save_orders_to_db(orders):

    for order in orders.get('orders', []):
        order_id = order.get('id', None)
        order_total = order.get('total_price', None)
        order_subtotal = order.get('subtotal_price', None)
        shipping = order.get('total_shipping_price_set', {}).get('shop_money', {}).get('amount', None)
        
        order_created_at_str = order.get('created_at', None)
        order_created_at = datetime.strptime(order_created_at_str, '%Y-%m-%dT%H:%M:%S%z')

        for line_item in order.get('line_items', []):
            sku = line_item.get('sku', None)
        
        new_order = Order(
            platform='Shopify',
            order_total_amount=order_total,
            order_subtotal_amount=order_subtotal,
            shipping=shipping,
            platform_order_id=order_id,
            product_sku=sku,
            date=order_created_at
        )
        db.session.add(new_order) 
        print(f'Order ID: {order_id}, Order total: {order_total}, Order subtotal: {order_subtotal}, Shipping: {shipping}, SKU: {sku}')

    db.session.commit()


@app.route('/get-shopify-data', methods=['GET'])
def get_shopify_data():
    shopify_orders = fetch_shopify_data()

    if shopify_orders is not None:
        save_orders_to_db(shopify_orders)
        return jsonify({'success': True, 'msg': 'Shopify orders saved to DB', 'data': shopify_orders})
    else:
        return jsonify({'success': False, 'msg': 'Error fetching Shopify data'})
    

@app.route('/checker') 
def checker():
    saved_orders = Order.query.all()
    print(type(saved_orders))

    orders_list = []
    for saved_order in saved_orders:
        order_data = {
            'id': saved_order.id,
            'order_total_amount': saved_order.order_total_amount,
            'product_sku': saved_order.product_sku,
            'date': saved_order.date.strftime("%Y-%m-%dT%H:%M:%S%z") if saved_order.date else None
        }
        orders_list.append(order_data)

    print("Orders saved to the database.")
    return jsonify(saved_orders=orders_list)


# custom app data
@app.route('/spend-snap', methods=['GET', 'POST'])
def custom_app_data():

    return render_template('spend_snap.html')
   



# TenderTransaction
# orders: orders.json?status=any&fields=id,...
    #    {
    #   "id": 5580255101088
    # },
    # {
    #   "id": 5566800396448
    # },
   


