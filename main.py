import requests
import json

i = 1
url = "https://tw.openrice.com/api/pois?uiLang=zh&uiCity=taipei&page={}&&sortBy=Default&districtId=1999&where=%E5%8F%B0%E5%8C%97%E5%B8%82".format(i)
while True:
    if i == 8:
        break
    headers = json.loads(r'''{
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh;q=0.6",
        "cookie": "_ga=GA1.3.1096550058.1528461596; _gid=GA1.3.2001389887.1528461596; __utma=158455359.1096550058.1528461596.1528461596.1528461596.1; __utmc=158455359; __utmz=158455359.1528461596.1.1.utmcsr=facebook.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_UA-652541-33=1; DefaultRegionIds=%7B%22tw%22%3A704%7D; RegionId=704; webhash=fb866e6e-2b50-4b42-9cb1-cad892bc9c68; isguest=1; autha=HRtpwbeNuwvp4Xn4UHNkasQfRGZT47-Art3vxVsldkW-V23r9m5k6LvfHvmvrU4iVJLfb6szsF88XinVLKUN_vua2mqnrS9E0N2oyZHBhwIcIbicWQSQgB3E-6ONygXJv9Xytdz6K0YIuU4gZFMl-kJ1-bWp1Fq7yRDvOgOiODnPnmQiatRG0pJHjLK3zs9JYCX3VeIvHr1R5LSL9qJ0_IyrCELcaoml-DeEr4LWNmj1a9cWcl4i4fKOAxE5akOT-QoX9rwbyWP-lS2zVEPCQ_7ATOojfgNmyReide3tNlQW6MNnI_YylhYgtrp2WeZblgyBKCjBmPbHLurI84c1hvng3pv16tLwFVxfYib3NEqM9IcqvyLfOkrWu-6Df1KInADDX_m8FhHmbID9-BnF6zlkNGCb2qItI91stNFboEF7y0KaiJnj4PBfNJL3ybYjRNn6eA; authr=6-NebrrDPCDeNgHpzcpbhdWsNcxNVmL0nYMqZbCEFWlTMeZb2yfh39NLocUvKweb3RbiJfHW8fz-dkXyA6NgHx6uOOiLP9m8hDVyu-UQnUJPV7Op0EcGJ5TyZHY1n5UOwwILC6BveMtpTcKGWHXDWZQAT7x399mgWS7jEg65QFpWXJ3UwchPPWaLPT_J0wcDPFkUwzeB_Xq_GNafTZh4i_TZQobPsZw_nbjQdW6wvv0t-4lZGOSd89IT2-M7v_hG_SG_MdT1sbP1GBBPmtTZLlZPUDDHB2zLf_1haqOMV_sh8S7OTP-4SDO7FGda4QvDHit_pCICP5S7GujhO0B0vStEnwuY9H6xjCuY3iRC1sAsKjliBGCSXHcUc6TuNyIo1K7OOshDh0yVnSRRlEwpHg3gSlekGyBvGvUvuSVNR8UATTQ8SLv9zx8alvrPqhYFcI1q6g; authe=+/MXVMVvA21WGHKPQtUJkV8XVLVxndnp72lTFUpymJcUwxdQc5PDmtsti98tuKVsQzEeZjgMnmpmILcIOeyWv/pYhXc9K9saLGzvWgbWrmw=; __utmb=158455359.12.10.1528461596",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    }''')

    resp = requests.get(url, headers=headers)
    html_search = json.loads(resp.text)
    # if len(html_search['searchResult']['paginationResult']['results']) == 0:
    #     break
    restaurants = html_search['searchResult']['paginationResult']['results']
    restaurant_dict = {}
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_dict['name'] = restaurant['name']
        restaurant_dict['address'] = restaurant['district']['name']+restaurant['address']
        restaurant_dict['source'] = 'OpenRice'
        restaurant_dict['category'] = '食'
        restaurant_dict['type'] = [cat['callName'] for cat in restaurant['categoriesUI']]
        location = {'lat':restaurant['mapLatitude'], 'lon':restaurant['mapLongitude']}
        restaurant_dict['location'] = location
        with open('./restaurants', 'a') as f:
            json.dump(restaurant_dict ,f, ensure_ascii=True)
    i += 1