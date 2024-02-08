from enums.pokemon_type import PokemonType
from clients import pokemon_client
import logging as log
from utils import pokemon_api_helper


def test_get_pokemon_api_response_type():
    response = pokemon_client.get_pokemon_type_list()

    log.info("verify get pokemon type list API status code")
    assert response.status_code == 200, f"get pokemon type list API failed on status code: {response.status_code}"
    log.info("verify get pokemon type list API response type")
    assert "application/json" in response.headers.get("Content-Type", "").lower(), "get pokemon type list API " \
                                                                                   "response type is not JSON"


def test_get_pokemon_api_has_20_different_pokemon_types():
    response = pokemon_client.get_pokemon_type_list()

    log.info("verify get pokemon type list API status code")
    assert response.status_code == 200, f"get pokemon type list API failed on status code: {response.status_code}"
    log.info("verify unique pokemon types")
    number_of_unique_pokemon_types = len(pokemon_api_helper.extract_unique_pokemon_types_from_response(response.json()))
    assert number_of_unique_pokemon_types == 20, f"number of unique pokemon types actual:" \
                                                 f" {number_of_unique_pokemon_types} - expected: 20"


def test_is_charmander_exist_in_fire_pokemon_list():
    pokemon_type_data_response = pokemon_api_helper.retrieve_pokemon_type_data(PokemonType.FIRE)
    log.info("verify retrieve pokemon type data status code")
    assert pokemon_type_data_response.status_code == 200, f"retrieve pokemon type data API failed on status code" \
                                                          f": {pokemon_type_data_response.status_code}"

    pokemon_type_data_response_body = pokemon_type_data_response.json()
    log.info("verify charmander exist in fire pokemon list")
    assert pokemon_api_helper.is_pokemon_present(pokemon_type_data_response_body, "charmander"), \
        "Actual: charmander does not exist in fire pokemon list, expected: charmander exist in fire pokemon list"


def test_is_bulbasaur_not_exist_in_fire_pokemon_list():
    pokemon_type_data_response = pokemon_api_helper.retrieve_pokemon_type_data(PokemonType.FIRE)
    log.info("verify retrieve pokemon type data status code")
    assert pokemon_type_data_response.status_code == 200, f"retrieve pokemon type data API failed on status code" \
                                                          f": {pokemon_type_data_response.status_code}"

    pokemon_type_data_response_body = pokemon_type_data_response.json()
    log.info("verify charmander exist in fire pokemon list")
    assert not pokemon_api_helper.is_pokemon_present(pokemon_type_data_response_body, "bulbasaur"),\
        "Actual: bulbasaur exist in fire pokemon list, expected: bulbasaur does not exist in fire pokemon list"


def test_heaviest_pokemons_weight_on_fire_type():
    expected_pokemons_name_weight_dict = {"charizard-gmax": 10000,
                                          "cinderace-gmax": 10000,
                                          "coalossal-gmax": 10000,
                                          "centiskorch-gmax": 10000,
                                          "groudon-primal": 9997}

    pokemon_type_data_response = pokemon_api_helper.retrieve_pokemon_type_data(PokemonType.FIRE)
    log.info("Get a dictionary of Pokemon names and URLs for the heaviest Pokemon in the fire type")
    pokemons_name_url_dict = pokemon_api_helper.extract_pokemon_name_url_dict(pokemon_type_data_response.json(),
                                                                              expected_pokemons_name_weight_dict.keys())

    log.info("Iterate through the dictionary and assert the weights of each Pokemon")
    for pokemon_name, pokemon_url in pokemons_name_url_dict.items():
        pokemon_api_helper.assert_pokemon_weight(pokemon_url, expected_pokemons_name_weight_dict[pokemon_name])
