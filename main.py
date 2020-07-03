
import os #系统
from  requestjsondata import getjsondata
import checkdestfile
from urllib.request import urlretrieve #下载图片
import json
import time
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
print(len(urls))
# /photos?page=183&per_page=10

checkdestfile.checkdestdir(imagedownpath) #检查下载目录文件是否存在，不存在及创建


for item in urls:
  page = 1
  url = 'https://unsplash.com/napi/topics/%s/photos?page=%d' %(item,page)
  print(url)
  if page==1:
    itemdir =os.path.join('.', imagedownpath)
    checkdestfile.checkdestdir(item,itemdir)
    jsondata,end =getjsondata(url,isfirst=True)
    if not jsondata == None and not end == None and item == urls[0]:
          if item==urls[0]:
              end = int(('%s'%(end))[2:])
          #解析json、 写入文件

          for i in range(len(jsondata)):
              #下载文件
                # imagelink = str.split(jsondata[i]['user']['profile_image']['small'], '?')[0]
                # imagelink = str.split(jsondata[i]['urls']['raw'], '?')[0]
                imagelink = jsondata[i]['urls']['raw']
                imagepathname= os.path.join(itemdir,item,'page%d_%d.jpg' % (page,i))
                print(imagelink)
                print(imagepathname)
                if  not os.path.exists(imagepathname):
                    # urlretrieve(imagelink,imagepathname)
                    try:
                       time.sleep(1)
                       threadPool.submit(urlretrieve, imagelink, imagepathname)
                    finally:pass
          page=page+1
          # break
          while page<end:
              url = 'https://unsplash.com/napi/topics/%s/photos?page=%d' % (item, page)
              print(url)
              jsondata =getjsondata(url)
              if not json == None:
                  for i in range(len(jsondata)):
                      # 下载文件
                      # imagelink = str.split(jsondata[i]['user']['profile_image']['small'], '?')[0]
                      # imagelink = str.split(jsondata[i]['urls']['raw'], '?')[0]
                      imagelink = jsondata[i]['urls']['raw']
                      imagepathname = os.path.join(itemdir, item, 'page%d_%d.jpg' % (page, i))
                      print(imagelink)
                      print(imagepathname)
                      if not os.path.exists(imagepathname):
                       try:
                        time.sleep(1)
                        threadPool.submit(urlretrieve,imagelink, imagepathname)
                       finally:pass
                      # urlretrieve(imagelink, imagepathname)
              page = page + 1
threadPool.shutdown(wait=True)















