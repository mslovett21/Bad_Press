# spider_foxnews
Scrapes fox news articles. Uses scrapy splash to obtain list of articles in Fox News search results, for each article, script follows the link to the full article and scrapes the articles date, title, and body. If a candidate has multiple pages on the search page, script follows the link to those pages and scrapes those articles as well.
## To get it running
Download and install [Scrapy](https://scrapy.org) (preferably in virtual environmnent).
```python
pip install scrapy
```
Download and install [Scrapy+Splash](https://github.com/scrapy-plugins/scrapy-splash).
```python
pip install scrapy-splash
```
Download and install [Docker](https://docs.docker.com/install/). Configure [scrapy+splash](https://github.com/scrapy-plugins/scrapy-splash#configuration) and run:
```
docker run -p 8050:8050 scrapinghub/splash
```
To start the spider, go to the top directory of spider\_foxnews and type:
```
scrapy crawl jsfoxnews_v1 -o jsfoxnews_v1.json
```
This will scrape fox news articles on West Virginia candidates and save the results to jsfoxnews\_v1.json file for viewing. 
