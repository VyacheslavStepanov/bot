# -*- coding: utf-8 -*-
import requests
from lxml import html
from lxml.etree import tostring

url = 'https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?f-promotion%3Aglobalpromo=true&pageSize=120'
r = requests.get(url)

# with open('c:\\Users\\sveta\\test.html', 'w', encoding='utf-8') as output_file:
#     output_file.write(r.text)

tree = html.fromstring(r.text)
item_list = tree.xpath('//div[@data-selenium="product_item"]')
for item in item_list:
    href = item.xpath('.//div/a/@href')[0]
    print(href)
    img = item.xpath('.//div/a/img/@src')[0]
    print(img)
    title = item.xpath('.//h2/a/@title')[0]
    print(title)
    price = item.xpath('.//div/div/span/sm-amount/@params')[0].split(':')[-1]
    print(price)
