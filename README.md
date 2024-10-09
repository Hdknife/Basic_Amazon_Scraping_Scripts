Basic Amazon Scraping Scripts
Welcome to the Basic Amazon Web Scraping Script project! This script is designed to extract product data from Amazon using Python’s powerful asynchronous programming capabilities.
<img width="893" alt="Screenshot 2024-10-09 160658" src="https://github.com/user-attachments/assets/b004cea7-56f8-47e0-928a-d5093f7f029b">

What This Script Does
This script efficiently scrapes product data from Amazon by making multiple requests at the same time. By using asynchronous programming with asyncio and aiohttp, it speeds up the scraping process significantly compared to traditional synchronous methods.

Key Features
Asynchronous Requests: Scrape multiple pages concurrently to gather data much faster.
User-Agent Rotation: Automatically changes the user agent with the help of the fake_useragent library to help avoid IP blocks.
Error Handling: Uses the backoff library to handle temporary issues, automatically retrying failed requests for more reliable data collection.
Structured Data: The scraped data is organized in a structured format, making it easy to analyze.
Logging: Includes built-in logging to keep track of the scraping process, helping you monitor what's happening behind the scenes.

Required
pip install aiohttp pandas beautifulsoup4 fake-useragent backoff

Example
if __name__ == "__main__":
    scraper = Amazon("laptop", pages=5)  # Change "laptop" to whatever you want to search for
    asyncio.run(scraper.run())
     scraper.Summary()

https://github.com/user-attachments/assets/1c3ad683-ad74-4b33-976a-82e4241cdca2

<img width="512" alt="5e794861-407c-4961-bc6f-8244046997e1" src="https://github.com/user-attachments/assets/df1b1e1c-ba40-49fb-94ca-3be405df6da5">

Important Note
Before you dive in, please be mindful of Amazon's terms of service regarding web scraping. Make sure to use this script responsibly!



   
