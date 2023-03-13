import csv
import time
import requests
from lxml import etree
import random

def get_WeatherMessage(provinceName, city_name, city_url):
    html_text = requests.get(city_url, headers).content.decode('UTF-8', 'ignore')
    city_tree = etree.HTML(html_text)

    title_list = city_tree.xpath("//tbody/tr/th//text()")
    with open(fr'E:/dataSave/{provinceName}{city_name}.csv', 'a', encoding='gbk', newline="") as writer:
        csv_write = csv.writer(writer, dialect='excel')
        csv_write.writerow(title_list)
    writer.close()

    for box in range(1, 90):
        data = city_tree.xpath(f"//tr[{box}]/td//text()")
        with open(fr'E:/dataSave/{provinceName}{city_name}.csv', 'a', encoding='gbk', newline="") as writer:
            csv_write = csv.writer(writer, dialect='excel')
            csv_write.writerow(data)
        writer.close()
    print('已完成对', city_name, '的爬取', '\n')

if __name__ == "__main__":

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    headers = {'User-Agent': random.choice(user_agent_list)}
    start_url = 'https://www.tianqishi.com/lishi/'
    start_html_text = requests.get(start_url, headers).content.decode('UTF-8', 'ignore')
    tree = etree.HTML(start_html_text)
    url_head = 'https://www.tianqishi.com'
    for i in tree.xpath("//div[@class='box p']/ul"):
        provinceName = i.xpath('./li[1]//text()')[0]
        for city in i.xpath('./li/a'):
            city_url = url_head + city.xpath('./@href')[0]
            city_name = city.xpath('.//text()')[0]
            get_WeatherMessage(provinceName, city_name, city_url)
        time.sleep(6)
        headers = {'User-Agent': random.choice(user_agent_list)}
