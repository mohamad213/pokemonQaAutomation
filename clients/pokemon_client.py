import requests
import logging as log


BASE_POKEMON_ENDPOINT = "https://pokeapi.co/api/v2"


def get_pokemon_type_list():
    log.info("start calling get pokemon type api")
    response = get_api_request(f"{BASE_POKEMON_ENDPOINT}/type")
    log.info("finish calling pokemon type api")

    return response


def get_api_request(endpoint):
    log.debug(f"start calling api {endpoint}")
    response = requests.get(endpoint)
    log.debug(f"finish calling api {endpoint}")

    return response
