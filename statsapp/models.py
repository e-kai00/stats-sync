from statsapp import db
# from datetime import datetime

"""
origin field: Etsy / Shopify / Custom App;

main_category field: platform billing / production costs / taxes / marketing / shipping;

sub_category field: used for main_category 'marketing' and incudes: Google ads / FB / IG / Etsy ads, 
and for main_category 'production costs' and includes: materials / supplies / labor;
"""

class Order(db.Model):
    order_number = db.Column(db.String(50), primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'), nullable=False)
    product_sku = db.Column(db.String(100), nullable=True)
    total_amount = db.Column(db.Integer, nullable=False)
    subtotal_amount = db.Column(db.Integer, nullable=False)
    order_discount = db.Column(db.Integer, nullable=True)
    shipping_cost = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    platform = db.relationship('Platform', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f'<Order {self.order_number}>'
    

class Metrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'), nullable=False)
    visits = db.Column(db.Integer, nullable=False)
    number_of_orders = db.Column(db.Integer, nullable=False)
    revenue = db.Column(db.Numeric(10, 2), nullable=False)

    platform = db.relationship('Platform', backref=db.backref('metrics', lazy=True))

    def __repr__(self):
        return f'<Metrics {self.date}>'
    

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    date = db.Column(db.Date, nullable=False)

    category = db.relationship('Category', backref=db.backref('expenses', lazy=True))
    platform = db.relationship('Platform', backref=db.backref('expenses', lazy=True))

    def __repr__(self):
        return f'<Expense {self.id}>'
    

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Platform {self.name}>'
    
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Category {self.name}>'
    

class SubCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)

    category = db.relationship('Category', backref=db.backref('subcategories', lazy=True))

    def __repr__(self):
        return f'<SubCategory {self.name}>'
    
    
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    revenue_total = db.Column(db.Numeric(10, 2), nullable=False)
    net_profit = db.Column(db.Numeric(10, 2), nullable=False)
    av_order_val = db.Column(db.Numeric(10, 2), nullable=False)
    conversion_rate = db.Column(db.Numeric(5, 2), nullable=False)

    def __repr__(self):
        return f'<Report {self.date}>'
