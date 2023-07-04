import requests
make='toyota'
model='camry'
api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}'.format(make, model)
response=requests.get(api_url, headers={'X-Api-Key': 'XBxnUM794qVefDSOxDFL9g==JeszY3re8Qi4vaDo'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)