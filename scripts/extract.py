import requests



cities = {"CDMX": (19.43, -99.13),
    "Guadalajara": (20.67, -103.35)}


def extract(latitud : float , longitud: float)-> dict:
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&hourly=temperature_2m'

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    json_response = response.json()
    return json_response
        
 
    
if __name__ == '__main__':
    lat , long = cities["CDMX"]
    j_dict = extract(lat , long)
    print(j_dict)



