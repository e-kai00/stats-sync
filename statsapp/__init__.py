import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError
# from werkzeug.exceptions import HTTPException
from errors.handlers import (
    handle_bad_request,
    page_not_found,
    internal_server_error,
    handle_generic_error,
    handle_sqlalchemy_error
)
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# database
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    print("External DB")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# error handlers
app.register_error_handler(SQLAlchemyError, handle_sqlalchemy_error)
app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_server_error)
app.register_error_handler(Exception, handle_generic_error)

# 3d party APIs
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
   
