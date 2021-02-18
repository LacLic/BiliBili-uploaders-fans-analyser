from urllib import parse, request
from http import cookiejar
import json


def get_user_info(uid):
    # cookie
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)

    # url
    url = f'https://api.bilibili.com/x/web-interface/card?mid={str(uid)}'

    # headers
    headers = {
        'User-Agent': 'BiliBili-uploaders-fans-analyser Client/0.0.1',
        'Referer': '',
    }

    # POST-need
    dic = {}

    # encode the data
    data = bytes(parse.urlencode(dic), encoding='utf-8',)

    # send req to web
    req = request.Request(  # make request
        url=url, data=data, headers=headers, method='GET',)
    response = opener.open(req)  # open the page / send the request

    # convert json data into python dict
    usr_info = json.loads(response.read().decode('utf-8', 'ignore'))
    print(f"fans: {usr_info['data']['card']['fans']}")


get_user_info(2)
