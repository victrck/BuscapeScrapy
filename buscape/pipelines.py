import sys
import mysql.connector
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import json

class BuscapePipeline(object):
	def __init__(self):
		self.conn = mysql.connector.connect(host= "localhost", user="root", passwd="sckk", db="buscape2018",charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		i = 0;    
		try:
			self.cursor.execute("INSERT INTO buscape(modelo, titulo, comentario, user, tipo_usuario, nota, data, achou_util, n_achou_util, recomendacao) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (item['modelo'],item['titulo'],item['comentario'], item['user'],item['tipo_user'], item['nota'], item['data'], item['achou_util'], item['n_achou_util'], item['recomendacao'])) 
			self.conn.commit()	
		except mysql.connector.Error as e:
			print (e)
		return item
	


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item