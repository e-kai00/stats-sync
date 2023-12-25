import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import shopify
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    print("External DB")

db = SQLAlchemy(app)

# base site URL
shop_url = f'https://{os.environ.get("SHOPIFY_API_KEY")}:{os.environ.get("SHOPIFY_ACCESS_TOKEN")}@{os.environ.get("SHOPIFY_SHOP_NAME")}.com/admin'
shopify.ShopifyResource.set_site(shop_url)

from statsapp import routes
from statsapp import models

   
