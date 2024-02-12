import requests
from bs4 import BeautifulSoup
import csv

url = "https://belgazprombank.by"
user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'
}
r = requests.get(url, headers=user_agent)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
items = soup.find_all("tr")
items.pop(0)
print(items)
curr = []
for i in range(0, 3):
    print(items[i])
    temp = items[i].find_all("td")
    curr.append({
        'Валюта': temp[0].get_text(),
        'Покупка': temp[1].get_text().replace('.', ','),
        'Продажа': temp[2].get_text().replace('.', ',')
    })

with open('curse.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['Валюта', 'Покупка', 'Продажа'],
        delimiter=';',
        lineterminator='\r',
        quoting=csv.QUOTE_MINIMAL
    )
    writer.writeheader()
    for elem in curr:
        writer.writerow(elem)
print('Запись окончена')
