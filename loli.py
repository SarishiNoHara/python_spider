# -*- coding: utf-8 -*-
import urllib 
import urllib2
import re
import os

class LoliSpider(object):

    num = 1;

    def __init__(self):
        pass

    def saveImage(self, imgUrl, imgPath):
        imgData = urllib.urlopen(imgUrl).read()
        f = open(imgPath, 'w')
        f.write(imgData)
        print "saving images...", imgPath
        f.close()

    def getImgUrl(self, url):
        response = urllib2.urlopen(url)
        text = response.read()

        pattern = re.compile(r'<div.*?class="list-item-image fluid-size">.*?src="(.*?)".*?>.*?</div>',re.S)
        imgs = re.findall(pattern, text)

        for img in imgs:
            imgUrl = img.replace(".md.",".") #download full size image
            print imgUrl
            imgPath = "Loli/%d.jpg" % (LoliSpider.num)
            self.saveImage(imgUrl, imgPath)
            LoliSpider.num += 1

    def getImgPage(self, fromP, toP):

        os.system("mkdir Loli")

        i = int(fromP)
        while i <= int(toP):
            url = "https://img.myhloli.com/explore/?list=images&sort=views_desc&page=" + str(i)
            print "%d", i
            self.getImgUrl(url)
            i += 1
            print "%d", i

loliSpider = LoliSpider()
beginPage = raw_input("start page(start from 3): ") #cannot print page 2
endPage = raw_input("end page: ")
loliSpider.getImgPage(beginPage, endPage)
