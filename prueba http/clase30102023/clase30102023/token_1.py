import requests

url= 'https://github.com/login'
sesion=requests.Session()
sesion.auth= ('luisa.reyescbxviqgmail.com', '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')
response=sesion.get(url)

if response.status_code==200:
    response1=sesion.get('https://github.com/fernanda2901')
    print(response1.cookies)
    print(response.content)
