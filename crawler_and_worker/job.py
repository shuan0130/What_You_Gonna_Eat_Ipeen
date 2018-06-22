import crawler

_url = 'http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p={}&adkw=%E5%8F%B0%E5%8C%97%E5%B8%82'

path = './single_thread_restaurant_urls_{}.txt'

for i in range(1,100):
    url = _url.format(i)
    crawler.get_urls.delay(url,path)
    print(i)