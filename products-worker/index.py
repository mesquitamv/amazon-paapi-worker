from flask import Flask, request
import json
from amazon.paapi import AmazonAPI
from .model.product import Product

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route("/product", methods=['GET'])
def get_products_list():
    
    args = request.json
    
    access_key = args['access_key']
    secret_key = args['secret_key']
    associate_tag = args['associate_tag']
    country = args['country']
    keywords = args['keywords']
    product_qty = args['product_qty']
    
    product_list = []
    count = 0

    amazon = AmazonAPI(access_key, secret_key, associate_tag, country)
    products = amazon.search_items(keywords=keywords)
    
    for count in range(product_qty):
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

if __name__ == "__main__":
    app.run()