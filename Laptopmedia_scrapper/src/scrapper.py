from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm.notebook import tqdm

import time
import pandas as pd
from bs4 import BeautifulSoup

class Product(object):
    def __init__(self, WebElement):
        self.ID = WebElement.find('a')['href'].split('/')[-2]
        self.Name = WebElement.find('a').find('h2').get_text()
    
        self.CPU, self.RAM, self.GPU, self.Display, self.Storage = None, None, None, None, None

        cpu = WebElement.find(class_="cpu")
        ram = WebElement.find(class_="ram")
        gpu = WebElement.find(class_="gpu")
        display = WebElement.find(class_="display")
        storage = WebElement.find(class_="storage")

        if cpu is not None:
            self.CPU = cpu.get_text()
        if ram is not None:
            self.RAM = ram.get_text()
        if gpu is not None:
            self.GPU = gpu.get_text()
        if display is not None:
            self.Display = display.get_text()
        if storage is not None:
            self.Storage = storage.get_text()

        self.Link = WebElement.find('a')['href']
        self.Image = WebElement.find('img')['src']
        self.Price = WebElement.find('span', class_='text-lm-darkBlue').get_text()
        self.Price = int(self.Price[1:])

    def print(self):
        attrs = vars(self)
        print('\n'.join("%s: %s" % item for item in attrs.items() if item[0] != 'WebElement'))

    def extract_to_dataframe(self):
        return pd.DataFrame([vars(self)])


def main():
    no_page = 1
    while(True):
        driver = webdriver.Chrome()
        driver.get(f"https://laptopmedia.com/specs/?current=n_{no_page}_n&size=n_1000_n&filters%5B0%5D%5Bfield%5D=availability&filters%5B0%5D%5Bvalues%5D%5B0%5D%5Bto%5D=n_2_n&filters%5B0%5D%5Bvalues%5D%5B0%5D%5Bfrom%5D=n_1_n&filters%5B0%5D%5Bvalues%5D%5B0%5D%5Bname%5D=Show%20only%20available%20laptops&filters%5B0%5D%5Btype%5D=any&filters%5B1%5D%5Bfield%5D=brand&filters%5B1%5D%5Bvalues%5D%5B0%5D=AORUS&filters%5B1%5D%5Bvalues%5D%5B1%5D=Gigabyte&filters%5B1%5D%5Bvalues%5D%5B2%5D=Alienware&filters%5B1%5D%5Bvalues%5D%5B3%5D=Microsoft&filters%5B1%5D%5Bvalues%5D%5B4%5D=Samsung&filters%5B1%5D%5Bvalues%5D%5B5%5D=Apple&filters%5B1%5D%5Bvalues%5D%5B6%5D=Panasonic&filters%5B1%5D%5Bvalues%5D%5B7%5D=Razer&filters%5B1%5D%5Bvalues%5D%5B8%5D=Google&filters%5B1%5D%5Bvalues%5D%5B9%5D=ACEMAGIC&filters%5B1%5D%5Bvalues%5D%5B10%5D=Jumper&filters%5B1%5D%5Bvalues%5D%5B11%5D=Toshiba&filters%5B1%5D%5Bvalues%5D%5B12%5D=ApoloSign&filters%5B1%5D%5Bvalues%5D%5B13%5D=BHWW&filters%5B1%5D%5Bvalues%5D%5B14%5D=Dynabook&filters%5B1%5D%5Bvalues%5D%5B15%5D=Fusion5&filters%5B1%5D%5Bvalues%5D%5B16%5D=Packard%20Bell&filters%5B1%5D%5Bvalues%5D%5B17%5D=LG&filters%5B1%5D%5Btype%5D=any")
        time.sleep(10)
        page_source = driver.page_source
        driver.close()

        soup = BeautifulSoup(page_source, 'html.parser')

        list_all = soup.find_all(class_="flex items-center gap-2 list-none border-b py-1 mb-2")
        if len(list_all) == 0:
            break

        df = None

        print(no_page)

        for ele in tqdm(list_all):
            item = Product(ele)

            if df is not None:
                df = pd.concat([df, item.extract_to_dataframe()], ignore_index=True)
            else:
                df = item.extract_to_dataframe()

        df.to_csv(f'./other/{no_page}.csv', index=False)
        no_page = no_page + 1

if __name__ == "__main__":
    main()