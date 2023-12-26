from statsapp import db


class Expense(db.Model):
    """
    origin filed: Etsy / Shopify / Custom App;

    main_category filed: platform billing / production costs / taxes / marketing / shipping;

    sub_category filed: used for main_category 'marketing' and incudes: Google ads / FB / IG / Etsy ads, 
    and for main_category 'production costs' and includes: materials / supplies / labor;
    """

    id = db.Column(db.Integer, primary_key=True)    
    origin = db.Column(db.String(120), nullable=False)  
    main_category = db.Column(db.String(255), nullable=False)
    sub_category = db.Column(db.String(255))
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.Date)

    def __repr__(self):
        return f"Expense('{self.origin}', '{self.main_category}', '{self.amount}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(120), nullable=False)

    order_total_amount = db.Column(db.Float, nullable=False) # to extend
    order_discount = db.Column(db.Float) 
    order_id = db.Column(db.Integer, nullable=False)
    product_sku = db.Column(db.String(255))
    shipping = db.Column(db.Float)

    date = db.Column(db.Date)

    def __repr__(self):
        return f"Order('{self.platform}', '{self.amount}')"
    

# class MarketingData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     platform = db.Column(db.String(120), nullable=False)

#     campaign_cost = db.Column(db.Float)
#     campaign_revenue = db.Column(db.Float)

    #...

    # def __repr__(self):
    #     return f"MarketingData('{self.platform}', '{self.campaign_cost}')"    
    

# class CustomAppData(db.Model):



