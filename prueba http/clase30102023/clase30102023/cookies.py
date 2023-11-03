import requests
url='http://httpbin.org/cookies'
response = requests.get(url)

print(response.content)
print('*'*20)
print(response.cookies)