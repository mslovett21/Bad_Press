import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
  name = "jsfoxnews"
  first = "name"
  last = "name"
  start_urls = ["http://www.foxnews.com"]

  def start_requests(self):
    first_names = ["Don",       "Bo",    "Evan",    "Joe",    "Patrick",   "Jack",    "Paula Jean",   "Tom"]
    last_names = ["Blankenship","Copley","Jenkins", "Manchin", "Morrisey", "Newbrough","Swearengin",  "Willis" ]
    for i in range(len(first_names)):
      candidate_link = "http://www.foxnews.com/search-results/search?q=" + first_names[i] + "+" + last_names[i]
      self.first = first_names[i]
      self.last = last_names[i]
      yield SplashRequest(url=candidate_link, callback=self.parse,
        args={
          'wait': 5,
        }, endpoint='render.html')

  def parse(self, response):
    for q in response.css("div.search-directive.ng-scope"):
      yield {
        'newspaper_name' : "http://www.foxnews.com",
        #'candidate_name': self.first + " " + self.last,
        'articles_date': q.css("span.search-date.ng-binding::text").extract_first(),
        'articles_title': q.css("a.ng-binding::text").extract_first(),
        'article_text': q.css("p.ng-binding.ng-scope::text").extract_first()
      }
    #next_page = response.css('li.arrow.no-margin a::attr(href.ng-click)').extract_first()
    #if next_page is not None:
    #    next_page = response.urljoin(next_page)
    #    yield SplashRequest(next_page, callback=self.parse,
    #      args={
    #        'wait': 1,
    #      }, endpoint='render.html')
