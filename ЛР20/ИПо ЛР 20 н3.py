from urllib.parse import urlparse
url=urlparse('https://sputnik.by/20231228/pravitelstvo-sokratilo-raskhody-na-kosmos-radi-postroyki-kartofelekhranilischa-1082426340.html')
url1 = url
#<Протокол><Домен><Путь><Параметры><Запрос><Якорь>
print(f'ссылка на новостной канал : {url1.scheme}://{url1.netloc}?{url1.path}{url1.params}{url1.query}{url1.fragment}')