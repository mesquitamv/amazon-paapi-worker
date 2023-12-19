import datetime, bson, json
from marshmallow import Schema, fields

class Product(object):
  
  def __init__(self, 
               asin,
               product_url,
               product_title, 
               product_primary_image,
               product_current_price,
               product_higgest_price,
               product_lowest_price):
      
      self.asin = asin
      self.product_url = product_url
      self.product_title = product_title
      self.product_primary_image = product_primary_image
      self.product_current_price = product_current_price
      self.product_higgest_price = product_higgest_price
      self.product_lowest_price = product_lowest_price
      self.created_at = datetime.datetime.now()

  def to_json(self):
    product_json = {
            "asin": self.asin,
            "product_url": self.product_url,
            "product_title": self.product_title,
            "product_primary_image": self.product_primary_image,
            "product_current_price": self.product_current_price,
            "product_higgest_price": self.product_higgest_price,
            "product_lowest_price": self.product_lowest_price,
            "created_at": self.created_at.isoformat()
            }
    return json.loads(bson.json_util.dumps(product_json))

  def to_bson(self):
      data = self.dict(by_alias=True, exclude_none=True)
      if data["_id"] is None:
          data.pop("_id")
      return data
