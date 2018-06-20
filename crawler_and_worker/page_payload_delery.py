import requests
import json
from bs4 import BeautifulSoup
import concurrent.futures
import time
start = time.time()
def page_parser(url):
    headers = json.loads(r'''{
        "x-devtools-emulate-network-conditions-client-id": "B43B96809F7811724C4D6C64FD56CAFD",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "upgrade-insecure-requests": "1"
    }''')
    resp = requests.get(url, headers=headers)
    print(resp)
    _url = url.replace('/','_').replace(':','')
    path = 'E:\\data_food\\' + _url
    with open(path,'w',encoding='utf8') as f:
        f.writelines(resp.text)


if __name__ == '__main__':
    with open(r'./data_test/single_thread_restaurant_urls_2018-06-17.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        fus = []
        count_executor = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
            for line in lines:
                url = line.strip()
                fus.append(executor.submit(page_parser,url))
                count_executor += 1
                print("Workers: ", count_executor)
            count_futures = 0
        # print(concurrent.futures.as_completed(fus))
            for futures in concurrent.futures.as_completed(fus):
                count_futures += 1
                print("Back Works: ",count_futures)

    end = time.time()
    print(end-start)
    
# for url in urls:
#     print(url)
#     # print('\n')
#     count += 1
# print(count)
# with open(path,'r',encoding='utf8') as f:
#     soup = BeautifulSoup(f.read())
#     print(type(soup))