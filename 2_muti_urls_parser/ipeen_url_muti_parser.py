import concurrent.futures
import requests
import json
import re
from pprint import pprint
from datetime import datetime
import time

path = './data_test/restaurant_urls_{}.txt'
today = datetime.today().date()
headers = json.loads(r'''{
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=0d237aad103c0d6d7174795ae2ff1a47; ipeen_anonymous=8b8f8b0febf8c7e64dfde838d656b3fe; lbss=0; lbsa=taiwan; appier_uid_1=856ac46a-5dfe-42ca-8605-c3679bf20553; _ga=GA1.3.1455135742.1529145414; _gid=GA1.3.107138922.1529145414; appier_utmz=%7B%22csr%22%3A%22google%22%2C%22timestamp%22%3A1529145415%7D; _atrk_sync_cookie=true; _atrk_ssid=gF2z3V-n_zMOa0C79BbCqq; _atrk_siteuid=YTzYlkNxC1U19srK; __asc=05fae1a5164082b5613d5ed7634; __auc=05fae1a5164082b5613d5ed7634; _ipeen_search_category=100; shop-score-tour=showed; search_othkw=0; _gat=1; _gat_newTracker=1; _ias_lastreferrer=; _atrk_sessidx=13",
    "Host": "www.ipeen.com.tw",
    "Referer": "http://www.ipeen.com.tw/search/all/000/0-100-0-0/?p=503&adkw=%E5%8F%B0%E5%8C%97%E5%B8%82",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}''')

_url = 'http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p={}&adkw=%E5%8F%B0%E5%8C%97%E5%B8%82'


submit_queue = []
# get_result_queue = []

def get_urls(url):
    resp = requests.get(url, headers=headers)
    # return resp
    # if resp.text.find('很抱歉，無法找到符合條件的店家資料，你可以嘗試以下動作') != -1:
    #     break
    restaurant_urls = ['http://www.ipeen.com.tw' + url for url in re.findall('<a href="(.+)" target="_blank" class="a37 ga_tracking" data-category="search"', resp.text)]
    return restaurant_urls

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    start_time = time.time()

    # submit many task to workers
    i = 1
    while True:
        if i == 2500:
            break
        url = _url.format(i)
        submit_queue.append(executor.submit(get_urls,url))
        i += 1

    # Result queue
    for future in concurrent.futures.as_completed(submit_queue):
        print(future.result())
        with open(path.format(str(today)),'a',encoding='utf8') as f:
            for url in future.result():
                f.write(url+'\n')
        i += 1

    end_time = time.time()
time_cost = end_time - start_time
print(time_cost)