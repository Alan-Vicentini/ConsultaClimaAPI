import requests
import pprint

apikey = "3f05d3b1f9964b8eacc22306253008"
link_api =  "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": apikey,
    "q": "Rio de Janeiro",
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]
    print(temp)
    print(descricao)