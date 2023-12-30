from urllib.parse import urlparse
url=urlparse('https//sputnik.by/20231228/pravitelstvo-sokratilo-raskhody-na-kosmos-radi-postroyki-kartofelekhranilischa-1082426340.html')
print(url)
# протокол "https" добавлялся бы такой коммандой если бы его небыло в данной  ссылке
url._replace(scheme='https')
print(url)