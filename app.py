#!/usr/bin/python3

import os
import json
import psycopg2 

if __name__ == '__main__':
    path = os.getcwd()
    with open(path+'/'+'config.json') as file:
        conf = json.load(file)['postgresql']  
#print(type(conf))
    try:
      conn = psycopg2.connect(host=conf['host'], database=conf['db'], user=conf['user'], password=conf['pwd'])
      print(f"[info] Sucsess Connect PostgreSQL...")
    except:
      print(f"[info] Can't Sucsess Connect PostgreSQL...")