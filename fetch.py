import scrapy
import time

class lbcTabletsSpider(scrapy.Spider):
    name = 'leboncoin_tablets'
    allowed_domains = ['leboncoin.fr']
    start_urls = ['https://www.leboncoin.fr/recherche/?category=9&text=maison&owner_type=private&real_estate_type=1&square=100-max']

    def parse(self, response):
        print("procesing:" + response.url)
        # Extract data using css selectors
        offer_name = response.xpath(
            "/html/body/div/div/div/section/main/div/div[2]/div[6]/div/div[7]/div[1]/div/div[1]/ul/li[1]/a/section/div[1]/p/span").extract()
        price = response.xpath("/html/body/div/div/div/section/main/div/div[2]/div[6]/div/div[7]/div[1]/div/div[1]/ul/li[1]/a/section/div[1]/div/span/span[2]").extract()
        pictures = response.xpath("/html/body/div/div/div/section/main/div/div[2]/div[6]/div/div[7]/div[1]/div/div[1]/ul/li[1]/a/div/span[1]/div/img").extract()
        address = response.xpath("/html/body/div/div/div/section/main/div/div[2]/div[6]/div/div[7]/div[1]/div/div[1]/ul/li[1]/a/section/div[2]/p[2]").extract()
        date = response.xpath("/html/body/div/div/div/section/main/div/div[2]/div[6]/div/div[7]/div[1]/div/div[1]/ul/li[1]/a/section/div[2]/p[3]").extract()
        href = response.xpath("/html/body/div/div/div/section/main/div/div[2]/div[6]/div/div[7]/div[1]/div/div[1]/ul/li[1]/a").extract()
        row_data = zip(offer_name, price, pictures, address,date,href)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'offer_name': item[0],
            # item[0] means product in the list and so on, index tells what value to assign
                'price': item[1],
                'pictures': item[2],
                'address': item[3],
                'date': item[4],
                'href': item[5],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
