from flask import Flask
import requests
import json
from amazon.paapi import AmazonAPI

app = Flask(__name__)


def get_products_list(access_key,secret_key,associate_tag,country,keywords,prodct_qtd):
    
  product_list = []
  count = 0

  amazon = AmazonAPI(access_key, secret_key, associate_tag, country)
  products = amazon.search_items(keywords=keywords)
  
  print(products)
  
  for count in range(prodct_qtd):
    product_url = (products['data'][count].detail_page_url)
    product_title = (products['data'][count].item_info.title.display_value)
    product_primary_image = (products['data'][count].images.primary.large.url)
    product_current_price =  (products['data'][count].offers.listings[0].price.amount)
    product_higgest_price = (products['data'][count].offers.summaries[0].highest_price.amount)
    product_lowest_price = (products['data'][count].offers.summaries[0].lowest_price.amount)

    if str(products['data'][count].offers.listings[0].price.savings) == 'None':
      product_savings_percentage = 0
    else:
      product_savings_percentage =  (products['data'][count].offers.listings[0].price.savings.percentage)

    product = { 
      "url": str(product_url),
      "title": str(product_title),
      "primary_image": product_primary_image,
      "current_price": product_current_price,
      "higgest_price": product_higgest_price,
      "lowest_price": product_lowest_price,
      "savings_percentage": product_savings_percentage      
    }

    product_list.append(product)
  
  return json.dumps(product_list)

@app.route("/product")
def get_products():
  keywords = 'macbook air m1'
  prouct_qtd = 10

  return get_products_list(access_key=access_key,secret_key=secret_key,associate_tag=associate_tag,country=country,keywords=keywords,prodct_qtd=prouct_qtd)

  