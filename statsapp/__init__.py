import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    print("External DB")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

SHOPIFY_API_BASE_URL = f'https://{os.environ.get("SHOPIFY_SHOP_NAME")}/admin/api/2023-10'
SHOPIFY_HEADERS = {
    'X-Shopify-Access-Token': os.environ.get("SHOPIFY_ACCESS_TOKEN"),
    'Content-Type': 'application/json' 
}

# Set Etsy API configuration
# ETSY_API_BASE_URL = "https://openapi.etsy.com/v2"
# ETSY_API_KEY = config.ETSY_API_KEY
# ETSY_API_SECRET = config.ETSY_API_SECRET


from statsapp import routes
from statsapp import models

   
