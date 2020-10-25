import time
import requests
import json
import os
import random
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jd_home1

from wordcloud import WordCloud

WC_MASJ_IMG = "yun1.jpg"
comment_file_path = 'id.txt'
WC_FONT_PATH = 'zitiku/汉仪楷体简.ttf'
number = jd_home1.spider_home()



def cut_word():
    """
    对数据分词
    :return:分词后的数据
    """
    with open(comment_file_path) as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
        return wl


def create_word_cloud():
    """
    生成词云
    :return:
    """
    # 设置词云形状图片
    wc_mask = np.array(Image.open(WC_MASJ_IMG))
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=2000, mask=wc_mask, scale=4,
                   max_font_size=50, random_state=42, font_path=WC_FONT_PATH)
    # 生成词云
    wc.generate(cut_word())

    # 在只设置mask的情况下，你将会的到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("ciyun.png", bbox_inches='tight') # 不要白色
    plt.show()


if __name__ == '__main__':

    create_word_cloud()
    jd_home1.file_rename()
