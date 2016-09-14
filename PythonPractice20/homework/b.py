__author__ = 'liuchang'

from a import func


class WeatherPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('wea.txt', 'w+') as file:
            city = item['city'][0].encode('utf-8')
            file.write('city:' + str(city) + '\n\n')

            date = item['date']

            desc = item['dayDesc']
            dayDesc = desc[1::2]
            nightDesc = desc[0::2]

            dayTemp = item['dayTemp']

            weaitem = zip(date, dayDesc, nightDesc, dayTemp)

            for i in range(len(weaitem)):
                item = weaitem[i]
                d = item[0]
                dd = item[1]
                nd = item[2]
                ta = item[3].split('/')
                dt = ta[0]
                nt = ta[1]
                txt = 'date:{0}\t\tday:{1}({2})\t\tnight:{3}({4})\n\n'.format(
                    d,
                    dd.encode('utf-8'),
                    dt.encode('utf-8'),
                    nd.encode('utf-8'),
                    nt.encode('utf-8')
                )
                file.write(txt)
        return item
代码比较简单，都是python比较基础的语法，如果您感觉比较吃力，建议先去学一下python基础课。

7. 把 ITEM_PIPELINES 添加到设置中

写好ITEM_PIPELINES后，还有很重要的一步，就是把 ITEM_PIPELINES 添加到设置文件 settings.py 中。

ITEM_PIPELINES = {
    'weather.pipelines.WeatherPipeline': 1
}
另外，有些网站对网络爬虫进行了阻止（注：本项目仅从技术角度处理此问题，个人强烈不建议您用爬虫爬取有版权信息的数据），我们可以在设置中修改一下爬虫的 USER_AGENT 和 Referer 信息，增加爬虫请求的时间间隔。

整个 settings.py 文件内容如下：

# -*- coding: utf-8 -*-

# Scrapy settings for weather project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['weather.spiders']
NEWSPIDER_MODULE = 'weather.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weather (+http://www.yourdomain.com)'
USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

DEFAULT_REQUEST_HEADERS = {
    'Referer': 'http://www.weibo.com'
}

ITEM_PIPELINES = {
    'weather.pipelines.WeatherPipeline': 1
}

DOWNLOAD_DELAY = 0.5
到现在为止，代码主要部分已经写完了。

8. 运行爬虫

在项目的scrapy.cfg同级目录下用下面的命令运行爬虫：

$ scrapy crawl myweather
正常情况下，效果如下：

enter image description here

然后，在当前目录下会多一个 wea.txt 文件，内容如下：

enter image description here

到此我们基于scrapy的天气数据采集就完成了。

四、答疑

1、关于结果只出现城市的问题

最近看到有同学反馈代码按课程运行后，最后的数据中只有城市数据，没有天气数据，我检查了一下代码，找到了问题存在的原因。

scrapy内置的html解析是基于lxml库的，这个库对html的解析的容错性不是很好，通过检查虚拟机中获取到的网页源码，发现有部分标签是不匹配的（地区和浏览器不同取到的源码可能不同），检查结果如图：

图片描述信息

所以导致在spider中取到的日期数据(item['date'])为空，然后在pilepine代码中做zip操作后，整个 weaitem 为空，所以最终只有城市数据了。

既然找到了原因，我们换个html代码解析器就可以了，这里建议用 BeautifulSoup （官网： http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html ），这个解析器有比较好的容错能力，具体用法可以参考上面的文档。

BeautifulSoup安装：

#下载BeautifulSoup
$ wget http://labfile.oss.aliyuncs.com/beautifulsoup4-4.3.2.tar.gz

#解压
$ tar -zxvf beautifulsoup4-4.3.2.tar.gz

#安装
$ cd beautifulsoup4-4.3.2
$ sudo python setup.py install
安装成功后，优化WeatherSpider代码，改进后的代码如下：

# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from weather.items import WeatherItem

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
            desc = item['dayDesc']
            desc_str = []
            for item in desc:
            	desc_str.append(item.encode('utf-8'))
            file.write('date:' + str(desc_str) + '\n\n')
        return item