from scrapy.item import Item, Field


class HzSampleItem(Item):
    theStrokes = Field()
    character = Field()
    
