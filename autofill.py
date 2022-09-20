import requests

cookies = {
    '0ctf_csrf_cookie': 'c8b2b3e5930e7767c1d620c49617d153',
    'ctf_session': '876b83d103423dbefdbcbc9b45550c99c4d8fe28',
}

headers = {
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
}

data = {
    '0ctf_csrf_token': 'c8b2b3e5930e7767c1d620c49617d153',
    'email': 'diwashm.189@gmail.com',
    'password': '12345678',
}

response = requests.post('https://ctf.0ops.sjtu.cn/login', cookies=cookies, headers=headers, data=data)
print(response.text)
