import scrapy
import re
from data_collection.items import ComputerItem

class ComputersSpider(scrapy.Spider):
    name = "computers"
    allowed_domains = ["desktop.bg"]
    start_urls = ["https://desktop.bg/computers-all"]

    def parse(self, response):
        computers = response.css('article')
        for computer in computers:
            product_url = computer.css('a::attr(href)').get()
            if product_url:
                yield scrapy.Request(url=response.urljoin(product_url), callback=self.parse_product)
            else:
                self.logger.warning(f'Could not find product URL in {computer}')

        # Follow pagination links
        next_page = response.css('a.next_page::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_product(self, response):
        item = ComputerItem()
        item['computer_name'] = response.xpath("//header/h1/text()").get().strip()

        multiple_processor_options = response.xpath("//tr[@id='DesktopCpu']//div[@class='default-option options']")
        if multiple_processor_options:
            item['processor'] = multiple_processor_options.xpath("./label/span[1]/text()").get().strip()
        else:
            item['processor'] = response.xpath("//tr[th[contains(text(), 'Процесор')]]/td/text()").get().strip()

        multiple_gpu_options = response.xpath("//tr[@id='DesktopVideoCard']//div[@class='default-option options']")
        if multiple_gpu_options:
            item['gpu'] = multiple_gpu_options.xpath("./label/span[1]/text()").get().strip()
        else:
            item['gpu'] = response.xpath("//tr[th[contains(text(), 'Видеокарта')]]/td/text()").get().strip()

        multiple_motherboard_options = response.xpath("//tr[@id='Motherboard']//div[@class='default-option options']")
        if multiple_motherboard_options:
            item['motherboard'] = multiple_motherboard_options.xpath("./label/span[1]/text()").get().strip()
        else:
            item['motherboard'] = response.xpath("//tr[th[contains(text(), 'Дънна платка')]]/td/text()").get().strip()

        multiple_ram_options = response.xpath("//tr[@id='DesktopRam']//div[@class='default-option options']")
        if multiple_ram_options:
            ram_text = multiple_ram_options.xpath("./label/span[1]/text()").get().strip()
            ram_match = re.search(r'(\d+)\s*GB', ram_text)
            if ram_match:
                item['ram'] = ram_match.group(1) + 'GB'
            else:
                item['ram'] = ram_text.strip()
        else:
            ram_text = response.xpath("//tr[th[contains(text(), 'Оперативна памет')]]/td/text()").get().strip()
            ram_match = re.search(r'(\d+)\s*GB', ram_text)
            if ram_match:
                item['ram'] = ram_match.group(1) + 'GB'
            else:
                item['ram'] = ram_text.strip() if ram_text else 'N/A'

        yield item

        # multiple_ram_options = response.xpath("//tr[@id='DesktopRam']//div[@class='default-option options']")
        # if multiple_ram_options:
        #     item['ram'] = multiple_ram_options.xpath("./label/span[1]/text()").get().strip()
        # else:
        #     item['ram'] = response.xpath("//tr[th[contains(text(), 'Оперативна памет')]]/td/text()").get().strip()
