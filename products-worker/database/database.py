from pymongo import MongoClient

class Database(object):
  
  def __init__(self, host, port, username, password):
    
    self.client = MongoClient(host, port, username = username, password = password)
    self.db = self.client.productsWorkerDB
    
  def insert_single(self, data):
    self.db.product.insert_one(data)
    
  def return_conn(self):
    return self.db