import scrapy
from ..items import FlickzeeItem

class FlickZee(scrapy.Spider):
    name = 'flickzee'
    start_urls = [
        'https://www.flickzee.com/'
    ]
    def parse(self, response):
        Movies = FlickzeeItem()
        div_all_owl_item = response.css('div.owl-item')



        for item in div_all_owl_item:
                Movie_Name = item.css('p::text').extract()
                Movie_Url = item.css('a').xpath('@href').extract()
                Image_Name = item.css('img').xpath('@alt').extract()




                Movies['Movie_Name'] = Movie_Name
                Movies[ 'Movie_Url'] = Movie_Url
                Movies ['Image_Name'] = Image_Name


                yield Movies







