import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(url)
    
    if vastaus.status_code == 200:
        data = vastaus.json()
        print(data["value"])
    else:
        print("Virhe vitsin hakemisessa.")

if __name__ == "__main__":
    hae_chuck_norris_vitsi()
