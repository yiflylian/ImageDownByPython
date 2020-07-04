import requests #网络请求
from retrying import retry #重试
from MatchEndPage import  getMaxPageByCookies
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

# with requests.get('') as f:


# def downimageTask():


@retry(stop_max_attempt_number=3)
def getjsondata(url,headers=headers,isfirst=False):
    with requests.get(url) as r:
        # print(r.status_code)
        if r.status_code == 200:
            if isfirst:
                Link =""
                link=r.headers.get('Link')
                # print(link)
                Link+=link
                # print(Link)
                endpage = getMaxPageByCookies(Link)
                # print(endpage)
                return  r.json(),int(endpage)
            else: return  r.json()
        else: return None






