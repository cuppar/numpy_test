import scrapy
from ..items import YNZPItem

class YNZPSpider(scrapy.spiders.Spider):
    name = 'ynzp'
    allowed_domains = ["http://www.ynzp.com/"]
    start_urls = [
        "http://www.ynzp.com/km/all/?query=java&qtype=jobname"
    ]
 # 集体智慧编程
    def parse(self, response):
        for sel in response.xpath("//ul[@class='joblist']/li"):
            job_name = sel.xpath(".//div[@class='jt']/a/text()").extract_first()
            requirement_labels = sel.xpath(".//div[@class='rq']//label/text()").extract()
            requirement_spans = sel.xpath(".//div[@class='rq']//span/text()").extract()
            requirements_buffer = ''
            for i in range(6):
                requirements_buffer += requirement_labels[i]
                requirements_buffer += requirement_spans[i] + '\n'

            details = sel.xpath(".//div[@class='dt']/text()").extract()
            detail_buffer = ''
            for detail in details:
                detail_buffer += detail + '\n'

            item = YNZPItem()
            item['job_name'] = job_name
            item['requirements'] = requirements_buffer
            item['detail'] = detail_buffer
            yield item