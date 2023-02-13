from pyecharts import options as opts
from pyecharts.charts import Line, Page, WordCloud
from pyecharts.globals import SymbolType

"""
参考地址: https://echarts.apache.org/examples/editor.html?c=line-marker
        https://pyecharts.org/
"""


def WordCloud_(city, words_count) -> WordCloud:
    c = (
        WordCloud()
            .add("", words_count, pos_top='10', word_size_range=[12, 55], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{city}近日天气变化词云图", subtitle="数据来自tianqishi.com"))
    )
    return c


def line_markpoint(city, time_list, high_temperature, low_temperature) -> Line:
    c = (
        Line()
            .add_xaxis(xaxis_data=time_list['日期时间'])
            .add_yaxis(
            series_name="最高气温",
            y_axis=high_temperature,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(type_="max", name="最大值")]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )
            .add_yaxis(
            series_name="最低气温",
            y_axis=low_temperature,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(type_="min", name="最小值")]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值"), ]
            ),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{city}近90天气温变化", subtitle="数据来自tianqishi.com"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(
                feature={
                    "saveAsImage": {},
                    "restore": {},
                    "dataZoom": {},
                    "dataView": {},
                    "magicType": {"show": True, "type": ['line', 'bar', 'stack', 'tiled']},
                },
            ),
            datazoom_opts=[opts.DataZoomOpts(start_value=30, end_value=70, )],  # 下方缩放轴
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )
    return c


def page_simple_layout(city, words_count, time_list, high_temperature, low_temperature):
    page = Page(page_title="city_message_show",layout=Page.SimplePageLayout)
    page.add(
        line_markpoint(city, time_list, high_temperature, low_temperature),
        WordCloud_(city, words_count),
    )
    page.render(f"D:/pythonProject/show/{city}.html")
