import numpy as np
from scipy import stats
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

item_name = []
prices = []

for i in range(1, 20):
    print(i)
    ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=electric+scooter&_sacat=0&_ipg=240&_pgn=" + \
        str(i) + "&rt=nc"
    r = requests.get(ebayUrl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    listings = soup.find_all('li', attrs={'class': 's-item'})
    for listing in listings:
        print(i)
        prod_name = " "
        prod_price = " "
        for name in listing.find_all('h3', attrs={'class': "s-item__title"}):
            if(str(name.find(text=True, recursive=False)) != "None"):
                prod_name = str(name.find(text=True, recursive=False))
                item_name.append(prod_name)

        if(prod_name != " "):
            price = listing.find('span', attrs={'class': "s-item__price"})
            prod_price = str(price.find(text=True, recursive=False))
            #prod_price = int(re.sub(",", "", prod_price.split("INR")[1].split(".")[0]))
            prices.append(prod_price)

data_scooters = pd.DataFrame({"Name": item_name, "Prices": prices})
data_scooters = data_scooters.drop(labels=0, axis=0)
print(data_scooters)
