import scrapy
import json
import os
import time
import random
import jd_home1
import jd_main
import UserAgent

number = jd_home1.spider_home()  # 获取产品id
comment_file_path = '../../../id.txt'  # 文件存储位置
headers = UserAgent.get_headers()  # 随机获取headers表头


class JdHomeSpider(scrapy.Spider):
    name = 'jd_home'

    # allowed_domains = [' ']
    # start_urls = ['http:// /']

    def start_requests(self):
        number_page = 10
        try:
            for page in range(1, number_page):
                url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={number}' \
                      '&score=0&sortType=5&page={page}&pageSize=10&isShadowSku=0&fold=1'.format(
                    page=page,
                    number=number
                )
                yield scrapy.Request(
                    url=url,
                    callback=self.parse1,
                    headers=headers,
                )
                time.sleep(random.random() * 2)  # 每次间隔2秒
                # print('京东评论数据：' + r.text[:500])
                if os.path.exists(comment_file_path):
                    os.remove(comment_file_path)
        except:
            print('爬取失败')

    def parse1(self, response):
        r = response.text
        r_json_str = r[20:-2]
        r_json_obj = json.loads(r_json_str)
        r_json_comments = r_json_obj['comments']
        for r_json_comments in r_json_comments:
            with open(comment_file_path, 'a+') as file:
                file.write(r_json_comments['content'] + '\n')
                file.write("===================================" + '\n\r')
            print(r_json_comments['content'])


    def parse(self, response):
        pass
