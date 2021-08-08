# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BuscapeItem(scrapy.Item):
	modelo = scrapy.Field()
	titulo = scrapy.Field()
	comentario = scrapy.Field()
	user = scrapy.Field()
	tipo_user = scrapy.Field()
	nota = scrapy.Field()
	data = scrapy.Field()
	achou_util = scrapy.Field()
	n_achou_util = scrapy.Field()
	recomendacao = scrapy.Field()
