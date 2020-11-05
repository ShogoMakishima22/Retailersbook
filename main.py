from xlwings.rest.api import api
import pandas as pd
import requests, json

base_url='http://127.0.0.1:8000/'
endpoint= '/book/bill.csv/names/bill/range'
r=requests.get(base_url+endpoint)
data=r.json()
data

ds=pd.read_excel('bill.xlsx')
print("12345")
print(ds)
print (ds.shape)
print(type(ds))
print(ds.iloc[0:10,2:4])
print(ds.iloc[0:10,1:15])
