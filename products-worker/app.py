from flask import Flask, request
from .routes.routes import routes_bp
from pymongo import MongoClient

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