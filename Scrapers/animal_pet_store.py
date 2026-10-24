import requests
from bs4 import BeautifulSoup
import time

url = "https://www.animalpetstorebr.com.br/bioativo/isopodes/"
session = requests.Session()

headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1"
    }

#Entering the site
def enter_site():
    for trin in range(1, 6):
        try:
            time.sleep(2)
            code = session.get(url, headers=headers, timeout=20)

            if code.status_code == 200:
                print("Here we go!")
                return code

            print(
                f"Try {trin}/5: "
                f"HTTP {code.status_code}"
            )

        except requests.exceptions.RequestException as error:
            print(f"Try {trin}/5: {error}")

        if trin < 5:
            time.sleep(5)

    print("Site cannot be acessed in 5 trys.")
    return None

def scraper():
    #Acessing
    code = enter_site()
    if code is None:
        print ("Error at entering website")
        return []
    else:
        soup = BeautifulSoup(code.text, 'html.parser')


    #getting stuff info
        #Pick offers
        time.sleep(2)
        offers_products = soup.find_all("div", attrs={"class": "item-description py-4 px-3"})

        list_products = []

        for b in (offers_products):
            try:
                #title
                title = b.find("div", attrs={"class": "js-item-name item-name mb-3"}).text.strip()
                #price
                price = b.find("span", attrs={"class": "js-price-display item-price"}).text.strip()
            
                list_products.append({"Product": title, "Price": price})
                print(f"Product: {title} | Price: {price}")

            except Exception as error:
                print(f"Error at processing ad: {error}")
                continue
        return list_products

if __name__ == "__main__":
    produtos = scraper()
    print(f"\nTotal: {len(produtos)} produtos encontrados.")