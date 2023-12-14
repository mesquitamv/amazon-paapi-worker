import datetime as dt
from marshmallow import Schema, fields

class Product(object):
  def __init__(access_key, secret_key, associate_tag, country, keywords, product_qty):  
      self.access_key = access_key
      self.secret_key = secret_key
      self.associate_tag = associate_tag
      self.country = country
      self.keywords = keywords
      self.product_qty = product_qty
      self.created_at = dt.datetime.now()

class ProductSchema(Schema):
    access_key = fields.Str()
    secret_key = fields.Str()
    associate_tag = fields.Str()
    country = fields.Str()
    keywords = fields.Str()
    product_qty = fields.Number()
    created_at = fields.Date()