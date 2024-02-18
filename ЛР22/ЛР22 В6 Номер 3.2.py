import requests
from bs4 import BeautifulSoup


header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

link='https://browser-info.ru/'
responce = requests.get(link, headers = header).text
soup = BeautifulSoup(responce,'lxml')
block= soup.find('div', id='tool_padding')


#check java
check_java = block.find('div', id='javascript_check')
status_java = check_java.find_all('span')[1].text
result_java = f'javascript:{status_java}'



#check flash
check_flash = block.find('div', id='flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'



#check user...
check_user = block.find('div',id='user_agent').text
#value_user = check_user.find('span')
#res_user = f'user-agent:{check_user}'

print (result_java)
print (result_flash)
print(check_user)



