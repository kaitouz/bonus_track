import requests
import json
import config
from bs4 import BeautifulSoup

import pandas as pd


class API(object):
    def __init__(self):
        self.ProductsList = []
        self.LastProductsList = None

    def send_request(self, page):

        cookies = config.COOKIES
        headers = config.HEADERS

        params = {
            'categoryId': '118',
            'offset': page * 24,
            'limit': '24',
            'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
            'doTranslit': 'true',
        }

        response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers)

        print(page, response.status_code)

        json_data = response.json()
        # with open('test.json', 'w') as file:
        #     json.dump(json_data, file, indent=4)
        products_list = json_data.get("body").get("products")
        self.LastProductsList = products_list

        if products_list != None:
            return True
        else:
            return False

    def get_products_from_page(self):
        no_page = 0
        while True:
            res = self.send_request(no_page)
            if res and no_page <= 10:
                no_page = no_page + 1
                # temp_df = pd.DataFrame(list(zip(self.LastProductsList, [None])), columns=['ID', 'link'])
                
                # self.ProductsLinkList = pd.concat([self.ProductsLinkList, temp_df], ignore_index=True)
                # self.ProductsLinkList.to_csv('first.csv', index=False) 
                self.ProductsList = self.ProductsList + self.LastProductsList
            else:
                break
        
        print(self.ProductsList)
        

bot = API()
bot.get_products_from_page()