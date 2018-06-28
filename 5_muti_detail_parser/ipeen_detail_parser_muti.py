import re
import glob
from bs4 import BeautifulSoup
import csv
import concurrent.futures
import time

def detail_parser(path,filewriter):
    print(path)
    try:
        with open(path,'r',encoding='utf8') as f:
            html = f.read()
        soup = BeautifulSoup(html)

        name = re.findall('<span itemprop="name">(.+?)</span>',html)[0]
        status = re.findall('<span class="mark-text gray">(.+?)</span>',html)
        if len(status) == 0:
            status = '營業中'
        else:
            status = status[0]
        address = soup.find('a',{'data-label':'上方地址'}).text.strip()
        type_one = soup.findAll('span',{'itemprop':'title'})[-2].text
        type_two = soup.findAll('span', {'itemprop': 'title'})[--4].text
        price_find = re.findall('本店均消(.+?)元',html)
        if len(price_find) == 0:
            price = None
        else:
            price = str(price_find[0].strip())

        # print(type(avg_price))
        # lat = re.findall('<meta property="place:location:latitude" content="(.+?)">',html)
        lat = soup.findAll('meta',{'property':'place:location:latitude'})[0]['content']
        lon = soup.findAll('meta',{'property':'place:location:longitude'})[0]['content']

        # status = soup.select_one('span > 'class' > 'mark-text gray'')
        # status = soup.find('span',{'class':'mark-text gray'}).text
        # name = soup.find('span',{'itemprop':'name'}).text
        # print(name,status,address,type_one,type_two,price,lat,lon)
        restaurant = [name,status,address,type_one,type_two,price,lat,lon]
        print('ok')
        filewriter.writerow(restaurant)
    except:
        with open('erorlog.txt','a',encoding='utf8') as f:
            f.write(path+'\n')

if __name__ =='__main__':
    start = time.time()
    filewriter = csv.writer(open('./data', 'a', encoding='utf8',newline=''), delimiter=',')
    # attribute = [name,status,address,type_one,type_two,price,lat,lon]
    filewriter.writerow(['name','status','Address','type_one','type_two','price','lat','lon'])

    pages_list = glob.glob(r'E:\data\data_food\*')
    # print(pages_list)
    total = len(pages_list)
    print(total)
    print(type(pages_list))
    test_list = ['E:\\data\\data_food\\http__www.ipeen.com.tw_shop_998418-Dear-Abbie-甜心蛋糕棒棒糖',
                 'E:\\data\\data_food\\http__www.ipeen.com.tw_shop_43130-鮮芋仙-西湖店',
                 'E:\\data\\data_food\\http__www.ipeen.com.tw_shop_6287-KIKI餐廳-復興旗艦店',
                 'E:\\data\\data_food\\http__www.ipeen.com.tw_shop_1074108-大釧鍋物']
    fus = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        proccess_number = 1
        for i in range(len(pages_list)):
            fus.append(executor.submit(detail_parser,pages_list[i],filewriter))
            print(proccess_number)
            proccess_number += 1
    end = time.time()
    cost = end - start
    print(cost)