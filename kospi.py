import requests;

URL = 'https://finance.naver.com/sise/'

res = requests.get(URL)

print(res.text)