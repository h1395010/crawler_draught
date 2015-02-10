from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hz_sample.items import HzSampleItem

class DmozSpider(BaseSpider):
    name = "hzII"
    allowed_domains = ["zdic.net"]
    start_urls = ["http://zdic.net/z/19/js/5DCD.htm"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        items = []

        for titles in titles:
            item = HzSampleItem()
            item["theStrokes"] = titles.xpath("id('z_i_t2_bis')").extract()
            item["character"] = titles.xpath("id('ziip')").extract()
            items.append(item) 
            #print the_strokes, character
        return items
