import crawler
import pandas as pd
import asyncio
import time
import os

#Our crawler is having trouble with some links. It is generating urls like :///programs/voyage-of-discovery/.
#It appears to be truncating https and the host domain. We need to fix this in crawler.py

#There also might be a multithreading solution to this, but crawler was giving me issues with that.

def crawl():
    c = 0
    df = pd.read_csv('cleaned.csv')
    #Is there an infinite loop?? aws is taking forever to complete
    for index, row in df.iterrows():
        if 'niaf' in row['Link']:
            continue
        pr = os.fork()
        if pr == 0:
            output = []
            crawl = crawler.Crawler(domain=row['Link'], num_workers=100)
            output = crawl.run()
            if output:
                return (index, output)
            #print(df)
            print("Done with: ", row['Link'])
            exit()
        c+=1
        if c > 6:
            break

crawl()
