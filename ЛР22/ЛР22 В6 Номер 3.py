import requests

link = "https://icanhazip.com/"
responce=requests.get(link)
print(responce.text)
