# -*- coding: utf-8 -*-
import scrapy
from aus.items import AusItem

class AuSpider(scrapy.Spider):
    name = 'au'
    # allowed_domains = ['https://www.aut.ac.nz']
    start_urls = [
    'https://www.aut.ac.nz/study/study-options/architecture/courses/master-of-architecture-professional',
    'https://www.aut.ac.nz/courses/master-of-philosophy?source=/architecture',
    'https://www.aut.ac.nz/courses/doctor-of-philosophy?source=/architecture'
   
    ]

    def parse(self, response):
        print("Response Type >>> ", type(response))
        item = AusItem()
        item['Course_Name'] = response.css('h1::text').extract_first()
        # item['Category'] = response.css('a:nth-child(7)::text').extract_first()
        item['Category'] = response.xpath('//*[@id="breadcrumb"]/a[4]/text()').extract_first()
        # item['Sub_Category'] = response.css('')
   
        item['Course_Website'] = response.url
        item['Duration'] = response.css('.row:nth-child(4) .value::text').extract_first().strip()
        yield item

        # item['Duration_Term'] = response.css('')
        # item['Study_Mode'] = response.css('')
        # item['Degree_Level'] = response.css('.quickFactsTable .row:nth-child(2) .value::text')
        # item['Monthly_Intake'] = response.css('')
        # item['Intake_Day'] = response.css('.progStart').extract_first()
        # item['Apply_Day'] = response.css('').extract_first()
        # item['Apply Month'] = response.css('').extract_first()
        # item['City'] = response.css('.row:nth-child(5) .value').extract_first()
        # item['Domestic Only'] = response.css('').extract_first()
        # item['International Fee'] = response.css('span:nth-child(10)::text').extract_first()
        # item['Domestic Fee'] = response.css('span:nth-child(4)::text').extract_first()
        # item['Fee Term'] = response.css('').extract_first()
        # item['Currency'] = response.css('').extract_first()
        # item['Study Load'] = response.css('').extract_first()
        # item['IELTS Listening'] = response.css('').extract_first()
        # item['IELTS_Speaking'] = response.css('').extract_first()
        # item['IELTS Writing'] = response.css('').extract_first()
        # item['IELTS Reading'] = response.css('').extract_first()
        # item['IELTS Overall'] = response.css('').extract_first()
        # item['PTE Listening'] = response.css('').extract_first()
        # item['PTE Speaking'] = response.css('').extract_first()
        # item['PTE Writing'] = response.css('').extract_first()
        # item['PTE_Reading'] = response.css('').extract_first()
        # item['PTE Overall'] = response.css('').extract_first()
        # item['TOFEL Listening'] = response.css('').extract_first()
        # item['TOFEL Speaking'] = response.css('').extract_first()
        # item['TOFEL_Writing'] = response.css('').extract_first()
        # item['TOFEL Reading'] = response.css('').extract_first()
        # item['TOFEL Overall'] = response.css('').extract_first()
        # item['English Test'] = response.css('').extract_first()
        # item['Reading'] = response.css('').extract_first()
        # item['Listening'] = response.css('').extract_first()
        # item['Speaking'] = response.css('').extract_first()
        # item['Writing'] = response.css('').extract_first()
        # item['Overall'] = response.css('').extract_first()
        # item['Academic Level'] = response.css('').extract_first()
        # item['Academic Score'] = response.css('').extract_first()
        # item['Overall'] = response.css('').extract_first()
        # item['Score Type'] = response.css('').extract_first()
        # item['Academic Country'] = response.css('').extract_first()
        # item['Other Test'] = response.css('').extract_first()
        # item['Score'] = response.css('').extract_first()
        # item['Other Requirements'] = response.css('').extract_first()
        # item['Course_Description'] = response.css('.intro+ div p::text').extract_first()
        # item['Course Structure'] = response.css('ul+ h2 , ul+ p , li , .paperbox , h2:nth-child(2) , .r-tabs-state-active p:nth-child(1)').extract_first()
        # item['Career'] = response.css('.r-tabs-state-active p::text').extract_first()
        # item['Scholarship'] = response.css('').extract_first()





	
 
