import scrapy
import requests
import json
import lxml.etree as le

number = 3136921


class JdHomeSpider(scrapy.Spider):
    name = 'jd_home'
    # allowed_domains = [' ']
    # start_urls = ['http:// /']

    def start_requests(self, page=0):
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={number}' \
              '&score=0&sortType=5&page={page}&pageSize=10&isShadowSku=0&fold=1'.format(
            page = page,
            number = number
        )
        try:
            yield scrapy.Request(
                url = url,
                callback=self.parse1,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                },

            )
            # print('京东评论数据：' + r.text[:500])
        except:
            print('爬取失败')

    def parse1(self,response):


        r = response.text
        print(r)
        print(type(r))
        r_json_str = r[20:-2]
        print("京东评论：" + r_json_str[:500])
        r_json_obj = json.loads(r_json_str)
        r_json_comments = r_json_obj['comments']
        print("京东评论数据：")
        for r_json_comments in r_json_comments:
            print(r_json_comments['content'])


    def parse(self, response):
        pass
