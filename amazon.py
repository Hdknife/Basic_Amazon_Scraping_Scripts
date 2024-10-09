import logging
from typing import List
import time
import asyncio
import aiohttp
import backoff
from bs4 import BeautifulSoup
import fake_useragent
from Savefile.constant import decription, HEADERS
import os


logging.basicConfig(
    filename=r'amazon_scraper.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

class Amazon:

    """Amazon Basic Web scraping script Some pages
    failed because this script currently not using
    IP address"""
    def __init__(self, SEARCH: str, pages: int = 10):
        self.SEARCH = SEARCH
        self.pages = pages
        self.database = []
        self.failed: list | None = []
        self.summary = None
        self.ua__ = fake_useragent.UserAgent()

    "get_html method take one argument content content = reponse.text. "
    async def get_html(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        elements = soup.find_all('div', attrs={'data-component-type': "s-search-result"})
        for tag in elements:
            dic = {'Title': None, 'Price': None, 'Discount': None,
                   'Rating': None, 'URL': None, 'Image': None}
            dic['Title'] = tag.find('div', attrs={'data-cy': "title-recipe"}).text
            price = tag.find('span', attrs={'class': 'a-price'})
            dic['Price'] = ''.join(set(price.text.split('₹'))) if price else 'N/A'
            rating = tag.find('i')
            dic['Rating'] = rating.text if rating else 'N/A'
            discount = tag.find('span', class_="a-letter-space").text
            dic['Discount'] = discount if discount else 'N/A'
            dic['URL'] = "https://www.amazon.in" + tag.find('a').get('href')
            dic['Image'] = tag.find('img', class_='s-image').get('src')
            self.database.append(dic)

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=20)
    async def session(self, session: aiohttp.ClientSession, URL):
        try:
            HEADERS.update({'user-agent': self.ua__.random})
            logger.info(f"Starting request for URL: {URL}")
            async with session.get(URL, headers=HEADERS) as response:
                if response.status == 503:
                    self.failed.append(URL)
                    raise aiohttp.ClientError(f"Invalid response: {response.status}")

                content = await response.text()  # Get the content as text
                await self.get_html(content)  # Pass the content to get_html
                logger.info(f"Successfully scraped URL: {URL}")

        except aiohttp.ClientError as e:
            logger.error(f"Client error for URL {URL}: {e}")
        except Exception as e:
            logger.exception(f"Unexpected error occurred for URL {URL}: {e}")

    """It's a run method which return the data.
    ***example***
    scraper = Amazon("laptop", pages=20)
    SC = await scraper.run()
    scraper.Summary()
    """
    async def run(self):
        logger.info(f"Scraping process started for search term: {self.SEARCH}, Pages: {self.pages}")
        start_time = time.time()

        urls = [f"https://www.amazon.in/s?k={self.SEARCH}&page={number}" for number in range(1, self.pages)]
        async with aiohttp.ClientSession() as session1:  # Use aiohttp for async HTTP requests
            tasks = [asyncio.create_task(self.session(session1, URL)) for URL in urls]
            results = await asyncio.gather(*tasks)

        end_time = time.time()
        t_m = end_time - start_time
        self.summary = decription.format(self.SEARCH, self.pages, len(self.failed), len(self.database), t_m)

        logger.info(f"Scraping process completed. {self.summary}")
        return results

    "Summary show the status of the code."
    def Summary(self):
        logger.info(f"Summary: {self.summary}")
        print(self.summary)
