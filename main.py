import time
import asyncio
import aiohttp
from fake_useragent import UserAgent
from models import *
import csv

async def fetch(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def collect_data():
    ua = UserAgent()
    headers = {
        'Accept': '*/*',
        'User-Agent': ua.random,
    }
    __create_csv()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 6):
            url = f'https://catalog.wb.ru/catalog/men_shoes/v2/catalog?cat=8194&limit=60&sort=benefit&page={i}&appType=128&curr=byn&lang=ru&dest=-59208&spp=30&xsubject=105'
            tasks.append(fetch(session, url, headers))
        
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            items_info = Products_name.parse_obj(response["data"])
            __save_csv(items_info)

def __create_csv():
    with open("wb_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'Бренд', 'Название', 'Начальная цена', 'Цена со скидкой', 'Количество'])

def __save_csv(Products_name):
    with open("wb_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for product in Products_name.products:
            if product.sizes:
                basic_price = product.sizes[0].price.basic
                total_price = product.sizes[0].price.total
            else:
                basic_price = None
                total_price = None

            writer.writerow([
                product.id,
                product.brand,
                product.name,
                basic_price,
                total_price,
                product.totalQuantity
            ])

def main():
    start_time = time.time()
    asyncio.run(collect_data())
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")

if __name__ == '__main__':
    main()
