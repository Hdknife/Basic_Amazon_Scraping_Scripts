import amazon
import pandas as pd
from Savefile.constant import animation
import asyncio

def main():
    SEARCH = "Laptop"
    Total = 50
#asynchronous web scraping class for extracting product information 
# from Amazon's search results.
    scraper = amazon.Amazon(SEARCH = SEARCH, pages = Total)
    asyncio.run(scraper.run())
    database =  scraper.database
    file = pd.DataFrame(database)
    file.to_csv('amazon.csv')
    animation()
    scraper.Summary()

if __name__ == "__main__":
    main()
         
