
# coding: utf-8

import twitter
import zipfile
import pandas as pd
from config import *
        

if __name__ == "__main__":
    
    api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)
    
    
    
    zip=zipfile.ZipFile('archivo.zip')
    file=zip.open('tweets.csv')
    df=pd.read_csv(file)
    filtrado=df[ntuits:]
    id_list=filtrado['tweet_id']
    
    
    counter=0
    for id in id_list:
        counter+=1
        try:
            api.DestroyStatus(id)
        except Exception:
            pass
        if counter%1000 ==0:
            print('Another block of 1000 tweets have been deleted')
    
    
    
    time.sleep(1)

