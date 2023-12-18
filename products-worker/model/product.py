import datetime
from marshmallow import Schema, fields

class Product(object):
  
  def __init__(self,product_url ,product_title ,product_primary_image ,product_current_price ,product_higgest_price ,product_lowest_price):        
      self.product_url = product_url
      self.product_title = product_title
      self.product_primary_image = product_primary_image
      self.product_current_price = product_current_price
      self.product_higgest_price = product_higgest_price
      self.product_lowest_price = product_lowest_price
      self.created_at = datetime.now()

  def to_json(self):
      return jsonable_encoder(self, exclude_none=True)

  def to_bson(self):
      data = self.dict(by_alias=True, exclude_none=True)
      if data["_id"] is None:
          data.pop("_id")
      return data