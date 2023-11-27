import json
import os

import requests
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}"
OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=metric"

EXPIRE_CACHE_TIME = 60 * 60 * 1  # 1 hour


@csrf_exempt
def obter_cidade(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is None or longitude is None:
            return JsonResponse(
                {"status": "erro", "mensagem": "Corpo de requisição inválido"}
            )

        cached_cidade = cache.get(f"cidade_{latitude},{longitude}")
        if cached_cidade:
            return JsonResponse({"status": "ok", "cidade": cached_cidade})

        cidade_url = NOMINATIM_URL.format(latitude, longitude)
        response_cidade = requests.get(cidade_url)

        if response_cidade.status_code != 200:
            return JsonResponse({"status": "erro", "mensagem": "Erro ao obter cidade"})

        cidade = (
            response_cidade.json().get("address", {}).get("town", "Cidade desconhecida")
        )
        cache.set(f"cidade_{latitude},{longitude}", cidade, EXPIRE_CACHE_TIME)
        return JsonResponse({"status": "ok", "cidade": cidade})
    else:
        return JsonResponse({"status": "erro", "mensagem": "Método inválido"})


@csrf_exempt
def obter_temperatura(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is None or longitude is None:
            return JsonResponse({"status": "erro", "mensagem": "Parâmetros inválidos"})

        cached_temperatura = cache.get(f"temperatura_{latitude},{longitude}")
        if cached_temperatura:
            return JsonResponse({"status": "ok", "temperatura": cached_temperatura})

        temperatura_url = OPEN_WEATHER_URL.format(
            latitude, longitude, os.environ.get("OPEN_WEATHER_API_KEY")
        )
        response_temperatura = requests.get(temperatura_url)

        if response_temperatura.status_code != 200:
            return JsonResponse(
                {"status": "erro", "mensagem": "Erro ao obter temperatura"}
            )

        temperatura_em_celsius = response_temperatura.json()["current"]["temp"]
        cache.set(
            f"temperatura_{latitude},{longitude}",
            temperatura_em_celsius,
            EXPIRE_CACHE_TIME,
        )
        return JsonResponse({"status": "ok", "temperatura": temperatura_em_celsius})
    else:
        return JsonResponse({"status": "erro", "mensagem": "Método inválido"})
