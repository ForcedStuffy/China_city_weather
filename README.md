# China_city_weather
实现中国城市天气数据可视化


对最后生成的html文件，在网页中自行添加鼠标事件获取响应信息，解析pramas获得URL地址，而后通过window.open实现新网页页面的打开。
chart_46c9f11bad4044d2aa5bde8fd9fda973.on("click", function (params) {
    url ='file:///'+params.data.value;
    window.open(url);
    // window.location.href=url;    //更新窗口
});
