import re #则表达式

match =r'>; rel="last"'
s =r'''<https://api.unsplash.com/topics/travel/photos?page=331>; rel="last", <https://api.unsplash.com/topics/travel/photos?page=2>; rel="next"'''


def getMaxPageByCookies(link):
    # print(link)
    for item in link.split(r','):
        # print(item)
        if item.endswith(match):
            str.__subclasses__()
            # number =filter(str.isdigit, item)
            number = re.sub("\D", '', item)
            if  number == None:
                number =0
            # print(number)
    return  number
