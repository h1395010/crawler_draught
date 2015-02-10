from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
#from hz_sample.items import HzSampleItem

class DmozSpider(BaseSpider):
    name = "hzIII"
    allowed_domains = ["tool.httpcn.com"]
    start_urls = ["http://tool.httpcn.com/Html/Zi/28/PWMETBAZTBTBBDTB.shtml"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")

        for titles in titles:
	    tester = titles.xpath('id('div_a1')/x:div[3]').extract() 
            print tester
