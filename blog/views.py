from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def index(request):
    r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false')
    data = []
    if r.status_code == 200:
        json = r.json()
        for j in json:
            data.append(j)

    contenido = {'nombre_sitio': 'BTCInfo', 'page_name': 'Home', 'data': data}
    return render(request, 'index.html', contenido)


def block(request):
    r = requests.get('https://api.bitaps.com/btc/v1/blockchain/blocks/last/10')
    data = []
    if r.status_code == 200:
        json = r.json()
        for j in json['data']:
            data.append(j)
    contenido = {'nombre_sitio': 'BTCInfo', 'page_name': 'Block', 'data': data}
    return render(request, 'block.html', contenido)