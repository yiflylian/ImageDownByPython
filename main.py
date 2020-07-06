import os #系统
from  requestjsondata import getjsondata
import checkdestfile
from urllib.request import urlretrieve #下载图片
import json
import time
from datetime import datetime #日期时间
from concurrent.futures import ThreadPoolExecutor
threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
from retrying import retry #重试
import  threading


urls = ['covid-19'
,'travel'
,'nature'
,'wallpapers'
,'textures-patterns'
,'people'
,'business-work'
,'technology'
,'animals'
,'interiors'
,'architecture'
,'food-drink'
,'work-from-home'
,'sustainability'
,'athletics'
,'spirituality'
,'health'
,'film'
,'fashion'
,'arts-culture'
,'history']

page =1
imagedownpath ='downimage'
common= '/photos?page=$page'
# https://unsplash.com/napi/topics/covid-19/
url = 'https://unsplash.com/napi/topics/%s/photos?page=%d' %(urls[0],page)
# print(len(urls))
# /photos?page=183&per_page=10

checkdestfile.checkdestdir(imagedownpath) #检查下载目录文件是否存在，不存在及创建

def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per)

# ————————————————
# 版权声明：本文为CSDN博主「逸少凌仙」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/u012424313/java/article/details/82222188


def downimage(jsondata):
    for i in range(len(jsondata)):
                      # 下载文件
                      # imagelink = str.split(jsondata[i]['user']['profile_image']['small'], '?')[0]
                      # imagelink = str.split(jsondata[i]['urls']['raw'], '?')[0]
                      imagelink = jsondata[i]['urls']['raw']
                      imagename='page%d_%d.jpg' % (page, i)
                      imagepathname = os.path.join(itemdir, item,imagename)
                      print(imagelink+':'+imagename)
                      # print(imagepathname)
                      if not os.path.exists(imagepathname):
                       try:
                        time.sleep(1)

                        threadPool.submit(urlretrieve,imagelink, imagepathname,cbk )

                       finally:pass
                      # urlretrieve(imagelink, imagepathname)


print('开始时间：%s'%datetime.now())
for item in urls:
  # if item== urls[0]:
  #     continue
  page = 1
  url = 'https://unsplash.com/napi/topics/%s/photos?page=%d' %(item,page)
  print("目录： "+item)
  if page==1:
    itemdir =os.path.join('.', imagedownpath)
    checkdestfile.checkdestdir(item,itemdir)
    jsondata,end =getjsondata(url,isfirst=True)
    if not jsondata == None and not end == None:
          if item==urls[0]:
              end = int(('%d'%(end))[2:])
              downimage(jsondata)
          page=page+1
          # break
          while int(page) <= int(end) and int(page)<=30:
              url = 'https://unsplash.com/napi/topics/%s/photos?page=%d' % (item, page)
              # print(url)
              jsondata =getjsondata(url)
              if not json == None:
                  downimage(jsondata)
              page = page + 1
threadPool.shutdown(wait=True)
print('结束时间：%s'%datetime.now())














