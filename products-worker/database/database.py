from pymongo import MongoClient

class Database(object):
  
  def __init__(self, host, port, username, password):
    
    self.client = MongoClient(host, port, username = username, password = password)
    self.db = self.client.productsWorkerDB
    
  def insert_one(self, data):
    self.db.product.insert_one(data)
    
  def insert_many(self, data):
    self.db.product.insert_many(data)
  
  def return_conn(self):
    return self.db