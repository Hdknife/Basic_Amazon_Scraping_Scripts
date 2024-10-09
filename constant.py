import time


decription = """
**Status**

Search : {}
pages : Total number of pages {}
failed : Total Failed pages {}
database : Total number of records {}
Excution Time : {}

**Excution Sucessful '\__-_/'**"""

HEADERS = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
                'cache-control': 'no-cache',
                'connection': 'keep-alive',
                  # Rotate user agent
                'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"'
            }

##just for fun not for regular usage animation fuction 
def animation():
    for i in range(1, 10):
        pattern = "."*i
        time.sleep(1)
        print(f"\r{pattern}'\___-/'", end= "")
        
animation()
