import scrapy


class QuotesSpider(scrapy.Spider):
	name="nyt_westvirginia"
	start_urls = [
		'https://www.nytimes.com',

	]

	def parse(self,response):
		first_names = ["Don",       "Bo",    "Evan",    "Joe",    "Patrick",   "Jack",    "Paula Jean",   "Tom"]
		last_names = ["Blankenship","Copley","Jenkins", "Manchin", "Morrisey", "Newbrough","Swearengin",  "Willis" ]
		for i in range(len(first_names)):
			candidate_link = "https://www.nytimes.com/search/" + first_names[i] + " " + last_names[i] + "/newest"
			first_name = first_names[i]
			last_name = last_names[i]
			yield scrapy.Request(candidate_link, callback=self.parse_the_candidate, meta={'first_name': first_name, 'last_name': last_name})

	def parse_the_candidate(self, response):
		candidate_links=[]
		candidate_links=response.css('li.SearchResults-item--3k02W a::attr(href)').extract()
		first_name = response.meta.get('first_name')
		last_name = response.meta.get('last_name')
		for link in candidate_links:
			yield scrapy.Request(link, callback=self.parse_the_article, meta={'article_link': link, 'first_name': first_name, 'last_name': last_name})


	def parse_the_article(self, response):
		link = response.meta.get('article_link')
		first_name = response.meta.get('first_name')
		last_name = response.meta.get('last_name')
		yield {
				 'newspaper_name' : "NYT",
				 'first_name': first_name,
				 'last_name': last_name,
				 'articles_date' :response.css('time ::text').extract_first(),
				 'articles_link': link,
				 'articles_title' :response.css('h1.headline ::text').extract(),
				 'article_text' : response.css('.story-body-text ::text').extract(),
			}


