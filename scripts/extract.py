import requests

LATITUDE = 19.43
LONGITUDE = -99.13
url = f'https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&hourly=temperature_2m'


try:    
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    json_response = response.json()
    print(json_response)
    

except requests.exceptions.HTTPError  as http_err:
    print('HTTPError : ', http_err)
except requests.exceptions.RequestException as e :
    print('A request error ocurred : ', e)


