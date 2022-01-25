import requests as re

url='http://127.0.0.1/api/register2/'
tok='http://127.0.0.1/api/tokenLogin/'
test='http://127.0.0.1/api/'

dat={
    "username": "admin2",
    # "email": "admin@bot.com",
    "password": "123"
}
h={
    "Content-Type": "application/json" ,
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzMDU0NTg2LCJpYXQiOjE2NDMwNTQyODYsImp0aSI6IjdiZjRhZDVhM2I1MzQxNGRhOGIyN2QyZjI3ZDhiYzUxIiwidXNlcl9pZCI6MjB9.6EubMk67_KKcqhi8cpXshyq-YtXNKZpuwy7ZsSM_VM0"
}
import json

with re.Session() as s:
    # res=s.post(url,json=dat,headers=h)
    res=s.post(tok,json=dat,headers=h)
    # res=s.get(test,headers=h)

    print(res.content)