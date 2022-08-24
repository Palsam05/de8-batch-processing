#!/usr/bin/python3

import os
import json
import sqlparse

import pandas as pd
import numpy as np

import connection
import conn_warehouse

if __name__ == '__main__':
    print(f"[INFO] Service ETL is Starting .....")
    conn_dwh, engine_dwh  = conn_warehouse.conn()
    cursor_dwh = conn_dwh.cursor()

    conf = connection.config('postgresql')
    conn, engine = connection.psql_conn(conf)
    cursor = conn.cursor()
############################
    path_query = os.getcwd()+'/query/'
    query = sqlparse.format(
        open(
            path_query+'query.sql','r'
            ).read(), strip_comments=True).strip()

    query_dim_users = sqlparse.format(
        open(
            path_query+'dim_users.sql','r'
            ).read(), strip_comments=True).strip()
    
    query_dwh_dim_users = sqlparse.format(
        open(
            path_query+'dwh_dim_users.sql','r'
            ).read(), strip_comments=True).strip()

    query_fact_orders = sqlparse.format(
        open(
            #select dengan join table
            path_query+'fact_orders.sql','r'
            ).read(), strip_comments=True).strip()
            
    query_dwh_fact_orders = sqlparse.format(
        open(
            path_query+'dwh_fact_orders.sql','r'
            ).read(), strip_comments=True).strip()

    query_dwh = sqlparse.format(
        open(
            path_query+'dwh_design.sql','r'
            ).read(), strip_comments=True).strip()
    try:
        print(f"[INFO] Service ETL is Running .....")
        df = pd.read_sql(query, engine)
        df_dim_users = pd.read_sql(query_dim_users, engine)
        df_fact_orders = pd.read_sql(query_fact_orders, engine)
        
        cursor_dwh.execute(query_dwh)
        cursor_dwh.execute(query_dwh_dim_users)
        cursor_dwh.execute(query_dwh_fact_orders)
        conn_dwh.commit()


        df_dim_users.to_sql('dim_users', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Service ETL dim users is Success .....")

        df.to_sql('dim_orders', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Service ETL dim orders is Success .....")

        df_fact_orders.to_sql('fact_orders', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Service ETL fact orders is Success .....")
    except:
        print(f"[INFO] Service ETL is Failed .....")

    

    