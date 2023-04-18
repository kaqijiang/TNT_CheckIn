import requests
import time
import random

session = requests.session()
# 注册地址 https://www.hjtnt.pro/auth/register?code=hwWF
url = 'https://www.hjtnt.co'
payload = {'email': '你的账号', 'passwd': '你的密码', 'code': ''}
headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

response = session.post(url + '/auth/login', headers=headers, data=payload)

# Check the response status code to make sure the login was successful
if response.status_code == 200:
    print('Login successful!')
else:
    print('Login failed.')

time.sleep(random.randint(1, 5))

response = session.post(url + '/user/checkin')

if response.status_code == 200:
    print('checkin successful!')
else:
    print('checkin failed.')