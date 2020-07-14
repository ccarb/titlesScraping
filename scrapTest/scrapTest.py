import json
import os
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if os.path.exists("titles.json"):
    os.remove("titles.json")

process = CrawlerProcess(get_project_settings())

process.crawl('titles')

process.start() # the script will block here until the crawling is finished

searchStrings=[
    'Cristina',
    'Coronavirus'
]
with open('titles.json', 'r') as f:
    data=json.load(f)
    total=len(data)
    for string in searchStrings:
        count=0
        for entry in data:
            if entry['title'].find(string)>=0:
                count=count+1    
        print('I found %d titles with "%s" in them.\nThat is %.2f%% of the total'%(count,string,count*100/total))