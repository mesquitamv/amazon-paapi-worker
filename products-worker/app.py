from flask import Flask, request
from .routes.routes import routes_bp
from pymongo import MongoClient

# class FlaskAppWrapper(object):
#     def __init__(self, app_name): 
#         self.app = Flask(app_name)
#         self.client = MongoClient('mmvtech.duckdns.org', 27017, username='username', password='password')
#         self.db = self.client.productsWorkerDB
#         self.app.register_blueprint(routes_bp)
        
#     def run(self):
#         self.app.run()

# if __name__ == "__main__":
#     product_worker = FlaskAppWrapper(__name__)
#     product_worker.app.run()

app = Flask(__name__)

app.register_blueprint(routes_bp)

def get_app():
    return app

def get_database_conn():
    client = MongoClient('mmvtech.duckdns.org', 27017, username='username', password='password')
    db = client.productsWorkerDB
    
    return db

if __name__ == "__main__":
    app.run()