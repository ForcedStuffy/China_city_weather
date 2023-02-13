import csv
import time
import requests
from lxml import etree
from fake_useragent import UserAgent


def get_WeatherMessage(provinceName, city_name, city_url):
    headers = {'User-Agent': UserAgent().random}
    html_text = requests.get(city_url, headers).content.decode('UTF-8', 'ignore')
    city_tree = etree.HTML(html_text)

    title_list = city_tree.xpath("//tbody/tr/th//text()")
    with open(fr'D:/dataSave/{provinceName}{city_name}.csv', 'a', encoding='utf-8', newline="") as writer:
        csv_write = csv.writer(writer, dialect='excel')
        csv_write.writerow(title_list)
    writer.close()

    for box in range(1, 90):
        data = city_tree.xpath(f"//tr[{box}]/td//text()")
        with open(fr'D:/dataSave/{provinceName}{city_name}.csv', 'a', encoding='utf-8', newline="") as writer:
            csv_write = csv.writer(writer, dialect='excel')
            csv_write.writerow(data)
        writer.close()
    print('已完成对', city_name, '的爬取', '\n')


if __name__ == "__main__":
    headers = {'User-Agent': UserAgent().random}
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
        time.sleep(30)
