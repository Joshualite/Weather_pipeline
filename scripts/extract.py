import requests

LATITUDE = 19.43
LONGITUDE = -99.1


def extract(latitud : float , longitud: float)-> dict:
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&hourly=temperature_2m'

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    json_response = response.json()
    return json_response
        
 
    
if __name__ == '__main__':
    j_dict = extract(LATITUDE , LONGITUDE)
    print(j_dict)



