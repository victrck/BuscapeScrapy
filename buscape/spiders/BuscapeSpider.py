import scrapy
import re
from scrapy.selector import Selector
from scrapy.http import Request,Response
from buscape.items import BuscapeItem

class BuscapeSpider(scrapy.Spider):
	name = "buscape"
	start_urls = [
		"http://www.buscape.com.br/celular-e-smartphone"
	]


	#Variáveis que são uteis na formação de outros links
	def __init__(self):
		self.avaliacoes = "http://www.buscape.com.br/avaliacoes/"
		self.base_url = "http://www.buscape.com.br"
		self.base = "http://www.buscape.com.br/celular-e-smartphone?"
		self.final = "/?pagina=2#avaliacoes"

		
	#Primeira chamada, coleta primeira lista de links de celulares e avança pra próxima página
	def parse(self, response):
		sel = Selector(response)
		links = sel.xpath("//*[@class='card-layout-TestAB bui-card card--grid card--product w_button_compare']/div[@class = 'inner']/a/@href").extract()
		phones = []
		for i in links:
			if i not in phones:
				phones.append(i)
		# exit()		
		# print(phones)

		for phone in phones:
			half = phone.split('/')[-1]
			# print("MODELO:"+ half)
			# url = self.avaliacoes + half + self.final
			print(url)
			new_request = Request(url, callback=self.parse_phone)
			yield 

		try:
			next_page = sel.xpath("//*[@id='app']/div/div[4]/div[2]/nav/ul/li[@class='pagination__item pagination__icon button-tab-links']/a/@href").extract()[1]
		# 	produto = sel.xpath("//*[@id='app']/div/div[2]/div/div[1]/div/div/section[1]/div[2]/div[1]/h1/text()").extract()[0]
		except:
			next_page = sel.xpath("//*[@id='app']/div/div[4]/div[2]/nav/ul/li[8]/a/@href").extract()[0]


		print(next_page)
		url = self.base + next_page
		new_new_request = Request(url, callback=self.parse)
		yield new_new_request



	#Coleta os reviews de cada celular e avança entre páginas de reviews
	def parse_phone(self,response):
		pass
# 		sel = Selector(response)

# 		try:
# 			produto = sel.xpath("//*[@id='main-container']/section/div/div[2]/div[@class='row row--info']/h1/span[1]/text()").extract()[0]
# 		except:
# 			produto = ""

# 		# ids = sel.xpath("//*[@class='consumer-opinion']/div/section/div/@data-reactid").extract()

# 		# for id in ids:
# 			item = BuscapeItem()
# 			item['produto'] = produto
# 		try:
# 			item['titulo'] = sel.xpath("//*[@class='review-content']/h4[@class='review-content__title']/a/text()").extract()
# 		except:
# 			item['titulo'] = ""
# 		try:
# 			item['texto'] = sel.xpath("//*[@class='review-content']/p/text()").extract()
# 		except:
# 			item['texto'] = ""
# 		try:
# 			item['user'] = sel.xpath("//*[@class='review-meta']/a/text()").extract()
# 		except:
# 			item['user'] = ""
# 		try:
# 			item['stars'] = sel.xpath("//*[@class='review-meta']/span/div[@class='rating-stars']/span/span[1]/text()").extract()
# 		except:
# 			item['stars'] = ""
# 		try:
# 			item['data'] = sel.xpath("//*[@class='review-meta']/time/text()").extract()
# 		except:
# 			item['data'] = ""
# 		try:
# 			item['recomendacao'] = sel.xpath("//*[@class='consumer-opinion']/div/section/div[@data-reactid ='"+id+"']/div/div[@class='consumer-header']/div/span[2]/span/text()").extract()
# 				# //*[@class='consumer-opinion']/div/section/div[@data-reactid ='"+id+"']/div/div[@class='consumer-header']/div/span[2]/span/text()
# 		except:
# 			item['recomendacao'] = ""		
# 		yield item

# //*[@class='small-10 medium-11 columns']/div[@class='review-ebit-certificate']
# 		next_url = sel.xpath("//*[@class='pagination__item button-tab-links pagination__active']/following-sibling::li/a/@href").extract()[0]
# 		next_url_full = self.base_url+next_url
# 		next_request = Request(next_url_full, callback=self.parse_phone)
# 		yield next_request

