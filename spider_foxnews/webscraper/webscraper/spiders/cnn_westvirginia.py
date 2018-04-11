import scrapy
from scrapy_splash import SplashRequest


first_names = ["Don",       "Bo",       "Joe",    "Patrick",   "Jack",    "Paula Jean",   "Tom"]
last_names = ["Blankenship", "Copley","Manchin", "Morrisey", "Newbrough","Swearengin",  "Willis" ]



class QuotesSpider(scrapy.Spider):
	name="cnn_westvirginia"
	start_urls = [
		'https://www.cnn.com',

	]

	def parse(self, response):
		for i in range(len(first_names)):
			results_link="https://www.cnn.com/search/?size=10&q=" + first_names[i] + "%20" + last_names[i]
			first_name = first_names[i]
			last_name = last_names[i]
			yield SplashRequest(results_link, callback=self.parse_results, meta={'splash' : {'endpoint' : 'render.html', 'args' : { 'wait' : 5.0 }}, 'first_name': first_name, 'last_name': last_name})

	def parse_results(self,response):
		first_name = response.meta.get('first_name')
		last_name = response.meta.get('last_name')
		number_of_pages = 1
		response_str = str(response)
		response_str = response_str.split("<200 ",1)[1]
		response_str = response_str.split(">",1)[0]
		string_number_results = response.css(".cnn-search__results-count ::text").extract()
		if len(string_number_results) == 0:
			number_of_pages=0
		else:
			string_pages = string_number_results[0].split("of ",1)[1]
			string_pages = string_pages.split(" for",1)[0]
			number_of_pages = int(string_pages)
			number_of_pages = int(number_of_pages/10) + 1
			print(number_of_pages)
		if number_of_pages > 30:
			number_of_pages = 30

		k=-10
		for j in range(number_of_pages):
			k = k + 10
			candidate_link = response_str+ "&from=" + str(k) + "&page=" + str(j)
			print(candidate_link)
			yield SplashRequest(candidate_link, callback=self.parse_the_candidate, meta={'splash' : {'endpoint' : 'render.html', 'args' : { 'wait' : 6.0 }}, 'first_name': first_name, 'last_name': last_name})

	def parse_the_candidate(self, response):
		candidate_links=[]
		candidate_links=response.css('h3.cnn-search__result-headline a::attr(href)').extract()
		first_name = response.meta.get('first_name')
		last_name = response.meta.get('last_name')
		for link in candidate_links:
			link = "https:"+ link
			yield SplashRequest(link, callback=self.parse_the_article, meta={'splash' : {'endpoint' : 'render.html', 'args' : { 'wait' : 3.0 }}, 'article_link': link, 'first_name': first_name, 'last_name': last_name})


	def parse_the_article(self, response):
		link = response.meta.get('article_link')
		first_name = response.meta.get('first_name')
		last_name = response.meta.get('last_name')
		yield {
			   	'newspaper_name' : "CNN",
			   	'first_name': first_name,
				'last_name': last_name,
				'articles_date' :response.css('.update-time ::text').extract(),
				'articles_link': link,
				'articles_title' :response.css('h1.pg-headline ::text').extract(),
				'articles_text': response.css('.zn-body__paragraph ::text').extract()
			}





