import requests

# URLs das APIs
api_ip = "https://api.ipify.org?format=json"

api_localizacao = "https://ipinfo.io/{}/geo"

# Requisição

req = requests.get(api_ip)
if req.status_code == 200:
    print(req.text)
    ip = req.json()
    print(ip["ip"])

    url_localizacao = api_localizacao.format(ip)
    print(url_localizacao)

    req = requests.get(url_localizacao)
        if req.status_code == 200:
            localizacao =req.json()
            print("Cidade: {} ".format( localizacao["city"])
            print(localizacao["region"])
            print(localizacao["country"])
            print(localizacao["loc"])
            print(localizacao["postal"])
            print(localizacao["timezone"])
    else:
        print("Error - Status code {}".format(req.status_code))


