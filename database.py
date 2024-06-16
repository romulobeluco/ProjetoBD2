
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['restaurante']
colecao_comidas = db['comidas']
colecao_clientes = db['clientes']
colecao_vendas = db['vendas']
