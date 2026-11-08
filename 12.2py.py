import requests

def hae_saa():
    # Korvaa 'OMA_API_AVAIN' omalla OpenWeather-palvelusta saamallasi API-avaimella
    api_key = "OMA_API_AVAIN"
    kaupunki = input("Anna paikkakunnan nimi: ")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"
    
    vastaus = requests.get(url)
    
    if vastaus.status_code == 200:
        data = vastaus.json()
        
        # Lämpötila on oletuksena kelvineinä
        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15
        saatila = data["weather"][0]["description"]
        
        print(f"\nSäätila paikkakunnalla {kaupunki}: {saatila}")
        print(f"Lämpötila: {lampotila_celsius:.1f} °C")
    else:
        print("Paikkakuntaa ei löytynyt tai API-avaimessa / pyynnössä on virhe.")

if __name__ == "__main__":
    hae_saa()
