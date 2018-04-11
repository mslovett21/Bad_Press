import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name="jsfoxnews_westvirginia"
    start_urls = ["http://www.foxnews.com"]

    def parse(self,response):
      first_names = ["Don",       "Bo",    "Evan",    "Joe",    "Patrick",   "Jack",    "Paula Jean",   "Tom"]
      last_names = ["Blankenship","Copley","Jenkins", "Manchin", "Morrisey", "Newbrough","Swearengin",  "Willis" ]
      #first_names = ["Don","Joe"]
      #last_names = ["Blankenship","Manchin"]
      for i in range(len(first_names)):
        #http://www.foxnews.com/search-results/search?q=don%20blankenship&ss=fn&start=0
        candidate_link = "http://www.foxnews.com/search-results/search?q=" + first_names[i] + "%20" + last_names[i] + "&ss=fn&start=0"
        first_name = first_names[i]
        last_name = last_names[i]
        yield SplashRequest(url=candidate_link, callback=self.parse_the_search_results,
        args={
          'wait': 10,
        }, endpoint='render.html', meta={'first_name': first_name, 'last_name': last_name})

    def parse_the_search_results(self, response):
      number_of_pages = []
      number_of_pages = response.css('a.ng-binding.ng-scope::text').extract()
      print("Printing <number_of_pages>")
      print(number_of_pages)
      candidate_links=[]
      candidate_links=response.css('a.ng-binding::attr(href)').extract()
      first_name = response.meta.get('first_name')
      last_name = response.meta.get('last_name')
      for link in candidate_links:
        if link:
          yield SplashRequest(url=link, callback=self.parse_the_article,
          args={
            'wait': 10,
          }, endpoint='render.html', meta={'first_name': first_name, 'last_name': last_name})
      for page in number_of_pages:
        page_format = int(page)
        print(page_format-1)
        next_page = response.url
        next_page = next_page[:-1]
        next_page = next_page + str(page_format-1) + "0"
        print(next_page)
        yield SplashRequest(url=next_page, callback=self.parse_next_pages,
        args={
          'wait': 10,
        }, endpoint='render.html', meta={'first_name': first_name, 'last_name': last_name})

    def parse_next_pages(self, response):
      candidate_links=[]
      candidate_links=response.css('a.ng-binding::attr(href)').extract()
      first_name = response.meta.get('first_name')
      last_name = response.meta.get('last_name')
      for link in candidate_links:
        if link:
          yield SplashRequest(url=link, callback=self.parse_the_article,
          args={
            'wait': 10,
          }, meta={'article_link': link, 'first_name': first_name, 'last_name': last_name}, endpoint='render.html')

    def parse_the_article(self, response):
      if response.css("time::attr(datetime)").extract_first():
        if response.css("div.article-text p::text").extract():
          link = response.meta.get('article_link')
          first_name = response.meta.get('first_name')
          last_name = response.meta.get('last_name')
          yield {
            'newspaper_name': "foxnews",
            'first_name': first_name,
            'last_name': last_name,
            'articles_date': response.css("time::attr(datetime)").extract_first(),
            'articles_link': link,
            'articles_title': response.css('h1::text').extract_first(),
            'article_text': response.css("div.article-text p::text").extract()
          }


