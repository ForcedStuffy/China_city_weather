import os
import re
import html
from pyecharts import options as opts
from pyecharts.charts import Map


def map_city(city_URL):
    c = (
        Map(opts.InitOpts(page_title="China_Weather"))
            .add(
            "天气数据",
            data_pair=city_URL,
            maptype="china-cities",
            label_opts=opts.LabelOpts(is_show=False),
            selected_mode='single',
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国城市地图", subtitle="数据来自tianqishi.com", ),
        )
            .render("weather_china_cities.html")
    )
    return c


if __name__ == "__main__":
    dirs = os.listdir('E:/dataSave')
    city_URL = []
    for filename in dirs:
        path = 'E:/dataSave/' + filename
        city = re.findall(r"[\u4e00-\u9fff]+", path)[0]
        city_URL.append([city, path])

    # print(city_URL)
    map_city(city_URL)
