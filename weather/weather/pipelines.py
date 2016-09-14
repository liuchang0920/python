# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy 

class WeatherPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('weather-final.txt', 'w+') as file:
            city = item['city'][0].encode('utf-8')
            file.write('city:' + str(city) + '\n\n')

            date = item['date']
            date_str = []
            for item in date:
            	date_str.append(item.encode('utf-8'))
            file.write('date:' + str(date_str) + '\n\n')
            # desc = item['dayDesc'].encode('utf-8')
            
            # file.write('date:' + str(desc) + '\n\n')
        return item