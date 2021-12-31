import requests

url = 'https://api.agify.io?name=michael'

# response = requests.get(url)      # {"name":"michael","age":69,"count":233482}
# 응답 json str을 dict로 parsing 해서 response에 저장

response = requests.get(url).json()
print(response)