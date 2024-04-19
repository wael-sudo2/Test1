import requests
from bs4 import BeautifulSoup
import re
import json


class Crawler:

    def __init__(self, url: str):
        self.url = url
        self.status_code, self.response_content = self.__private_send_request()
        self.soup = self.__private_parse_response()

    def __private_send_request(self):
        """Sends an HTTP GET request to the website and returns status code and content

        Raises:
            Exception: If the request fails
        """

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(url=self.url, headers=headers)
            response.raise_for_status()  # Raise exception for unsuccessful responses
            return response.status_code, response.content
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to reach website. {e}")
            return None, None

    def __private_parse_response(self):
        """Parses the response content using BeautifulSoup if successful

        Raises:
            SystemExit: If parsing fails
        """

        if self.status_code == 200 and self.response_content:
            soup = BeautifulSoup(self.response_content, 'lxml')
            return soup
        else:
            print(f"Error: Failed to parse response")
            exit(1)

    @staticmethod
    def __private_data_parsing(data: dict):
        """Writes product data to a JSON file."""

        with open("data.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def fetch_products(self):
        """Fetches product data from the website and writes it to a JSON file"""

        panels_elements = self.soup.find_all('div', class_="uk-panel uk-position-relative")
        products = []
        for panel in panels_elements:
            product_url = panel.find('a')['href']
            image = panel.find("img", class_="product-image-photo")['data-amsrc']
            brand = panel.find("div", class_="uk-width-expand").text.strip()
            name = panel.find("h3", class_="product-name").text.strip()
            price = re.findall(r"\b\d+(?:,\d{1,2})?\b", panel.find("span", class_="uk-price").text)[0]
            price  = float(re.sub(r",", ".", price))

            products.append({
                "name": name,
                "price": price,
                "brand": brand,
                "imageUrl": image,
                "productUrl": product_url
            })

        self.__private_data_parsing(products)

if __name__ == '__main__':
    crawler = Crawler(url="https://www.pascalcoste-shopping.com/soins-cheveux/cheveu-normal.html")
    crawler.fetch_products()
