import scrapy

class SpaceNewsSpider(scrapy.Spider):
    name = 'spacenews.com-spider'
    start_urls = ['http://spacenews.com']

    def parse(self, response):
        """
        Get title links of articles.
        """
        # print('status: {0}'.format(response.status))
        # print('body: {0}'.format(response.body))
        for url in response.css('.article-content h1 a::attr(href)').extract():
            # print('url: {0}'.format(url))
            yield scrapy.Request(url, self.parse_titles)

    def parse_titles(self, response):
        """
        Get a title of posts.
        """
        for post_title in response.css('.post-title::text').extract():
            yield {'title': post_title}
