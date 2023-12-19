from flask import Blueprint, request
from amazon.paapi import AmazonAPI
from dotenv import load_dotenv
from ..database.database import Database
from ..model.product import Product
from bson import json_util
import json, os, datetime

routes_bp = Blueprint('routes',__name__)

load_dotenv()
access_key = os.environ.get('AMAZON_PAAPI_ACCESS_KEY')
secret_key = os.environ.get('AMAZON_PAAPI_SECRET_KEY')
associate_tag = os.environ.get('ASSOCIATE_TAG')
country = os.environ.get("COUNTRY")
db_host = os.environ.get("DATABASE_HOST")
db_port =  int(os.environ.get("DATABASE_PORT"))
db_username =  os.environ.get("DATABASE_USERNAME")
db_password =  os.environ.get("DATABASE_PASSWORD")

db = Database(host = db_host, port = db_port, username = db_username, password = db_password)

@routes_bp.route("/ping", methods=['GET'])
def ping():
    return "pong"

@routes_bp.route("/search", methods=['GET'])
def get_products_list():
    
    args = request.json
    
    keywords = args['keywords']
    product_qty = args['product_qty']
        
    product_list = []
    count = 0

    amazon = AmazonAPI(access_key, secret_key, associate_tag, country)
    products = amazon.search_items(keywords=keywords)
        
    for count in range(product_qty):
        
        product_asin = (products['data'][count].asin)
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
        
        product = Product(product_asin, 
                          product_url,
                          product_title,
                          product_primary_image,
                          product_current_price,
                          product_higgest_price,
                          product_lowest_price
                          )
        
        product_list.append(product.to_json())
    
    data = json.loads(json_util.dumps(product_list))
    db.insert_many(data)
    
    return json.dumps(product_list)

@routes_bp.route('/item', methods=['GET'])
def get_item():
    
    args = request.json
    
    asins = args['asins']
    
    print(type(asins))
    
    product_list = []
    
    amazon = AmazonAPI(access_key, secret_key, associate_tag, country)
    products = amazon.get_items(item_ids=asins)
    
    for asin in asins:
       
        product_asin = (products['data'][asin].asin)
        product_url = (products['data'][asin].detail_page_url)
        product_title = (products['data'][asin].item_info.title.display_value)
        product_primary_image = (products['data'][asin].images.primary.large.url)
        product_current_price =  (products['data'][asin].offers.listings[0].price.amount)
        product_higgest_price = (products['data'][asin].offers.summaries[0].highest_price.amount)
        product_lowest_price = (products['data'][asin].offers.summaries[0].lowest_price.amount)
        
        if str(products['data'][asin].offers.listings[0].price.savings) == 'None':
            product_savings_percentage = 0
        else:
            product_savings_percentage =  (products['data'][asin].offers.listings[0].price.savings.percentage)
            
        product = Product(product_asin, 
                          product_url,
                          product_title,
                          product_primary_image,
                          product_current_price,
                          product_higgest_price,
                          product_lowest_price
                          )
        
        product_list.append(product.to_json())
    
    data = json.loads(json_util.dumps(product_list))
    db.insert_many(data)
    
    return json.dumps(product_list)