from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
#from hz_sample.items import HzSampleItem

class DmozSpider(BaseSpider):
    name = "hzIII"
    allowed_domains = ["tool.httpcn.com"]
    start_urls = ["http://tool.httpcn.com/Html/Zi/28/PWMETBAZTBTBBDTB.shtml"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        ###root = hxs.select("//p")

        tester = hxs.xpath('//*[@id="div_a1"]/div[2]').extract()
        retester = hxs.xpath('//*[@id="div_a1"]/div[3]').extract()
        ###retester = root.xpath('//*[@id="div_a1"]/div[2]').extract()
        ###tester = root.xpath('//*[@id="div_a1"]/div[3]').extract() 
        print tester
        print("BREAK")
        print retester

##ORIGINAL VIDEO DEMO
#    def parse(self, response):
#        hxs = HtmlXPathSelector(response)
#        titles = hxs.select("//p")

#        for titles in titles:
#	     tester = titles.xpath('//*[@id="div_a1"]/div[3][1]').extract()
#	     jester = titles.xpath('//*[@id="div_a1"]/div[2]').extract() 
#            print tester

##ALTERNATE STACK SOLUTION
# class Spider(BaseSpider):
#     name = "hzIII"
#     allowed_domains = ["tool.httpcn.com"]
#     start_urls = ["http://tool.httpcn.com/Html/Zi/28/PWMETBAZTBTBBDTB.shtml"]
#     def parse(self, response):
#         print  response.xpath('//*[@id="div_a1"]/div[2]').extract()
#         print("BREAK")
#         print  response.xpath('//*[@id="div_a1"]/div[3]').extract() 
