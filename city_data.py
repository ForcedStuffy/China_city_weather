import os
import re
import jieba
from collections import Counter
import pandas as pd
from city_data_show import page_simple_layout

if __name__ == "__main__":
    dirs = os.listdir('E:/dataSave')
    for filename in dirs:
        path = 'E:/dataSave/' + filename
        city = re.findall(r"历史天气(.*?).csv", path)[0]
        data = pd.read_csv(path, encoding='gbk')

        data['日期时间'] = data['日期时间'].apply(lambda x: pd.to_datetime(x, format="%Y%m%d"))
        data['日期时间'] = data['日期时间'].dt.date
        high_temperature = []
        low_temperature = []
        for temeratrue in data['气温']:
            low, high = re.split('[~℃]', temeratrue)[0:2]
            low_temperature.append(int(low))
            high_temperature.append(int(high))

        text = ""
        for i in data['天气情况']:
            text = text + ',' + i
        words = [x for x in jieba.lcut(text) if x != ',']
        words_count = Counter(words).most_common(40)

        page_simple_layout(city, words_count, data, high_temperature, low_temperature)
