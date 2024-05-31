# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComputerItem(scrapy.Item):
    computer_name = scrapy.Field()
    processor = scrapy.Field()
    gpu = scrapy.Field()
    motherboard = scrapy.Field()
    ram = scrapy.Field()
