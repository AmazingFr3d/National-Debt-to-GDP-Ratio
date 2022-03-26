# -*- coding: utf-8 -*-
import scrapy


class GdpDebt1Spider(scrapy.Spider):
    name = 'gdp_debt1'
    allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//tbody/tr")

        for row in rows:
            yield{
                'country_name': row.xpath(".//td[1]/a/text()").get(),
                'gdp_debt': row.xpath(".//td[2]/text()").get()

            }
