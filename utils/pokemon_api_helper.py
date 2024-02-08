from clients.pokemon_client import get_pokemon_type_list, get_api_request
from enums.pokemon_type import PokemonType
from errors.failedExtractPokemonNameUrlDictError import FailedExtractPokemonNameUrlDictError
from errors.failedExtractUniquePokemonTypesError import FailedExtractUniquePokemonTypesError
from errors.failedGetPokemonTypeUrlError import FailedGetPokemonTypeUrlError
from errors.unsupportedPokemonTypeError import UnsupportedPokemonTypeError


def retrieve_pokemon_type_data(type_name):
    type_url = get_pokemon_type_url(type_name)
    return get_api_request(type_url)


def get_pokemon_type_url(pokemon_type):
    if not isinstance(pokemon_type, PokemonType):
        raise UnsupportedPokemonTypeError(pokemon_type)

    response_body = get_pokemon_type_list().json()
    try:
        pokemon_url = next((entry["url"] for entry in response_body["results"] if entry["name"] == pokemon_type.value), None)
    except Exception as e:
        raise FailedGetPokemonTypeUrlError(e)
    return pokemon_url


def extract_pokemon_name_url_dict(type_response_body, pokemon_names):
    pokemons_name_url_dict = {}
    try:
        for entry in type_response_body["pokemon"]:
            if entry["pokemon"]["name"] in pokemon_names:
                pokemons_name_url_dict[entry["pokemon"]["name"]] = entry["pokemon"]["url"]
            # If the dictionary contains all specified Pokemon names, exit the loop
            if len(pokemons_name_url_dict) == len(pokemon_names) \
                    and set(pokemons_name_url_dict.keys()) == set(pokemon_names):
                break
    except Exception as e:
        raise FailedExtractPokemonNameUrlDictError(e)
    return pokemons_name_url_dict



def is_pokemon_present(type_response_body, pokemon_name):
    # Check if any entry in the type response has the specified Pokemon name
    return any(entry["pokemon"]["name"] == pokemon_name for entry in type_response_body["pokemon"])


# Function to assert the weight of a specific Pokemon
def assert_pokemon_weight(pokemon_url, expected_weight):
    # Make a GET request to retrieve the details of the specific Pokemon
    response_body = get_api_request(pokemon_url).json()
    # Assert that the Pokemon's weight matches the expected weight
    assert response_body["weight"] == expected_weight


def extract_unique_pokemon_types_from_response(response_body):
    pokemon_different_types = set()
    try:
        for entry in response_body["results"]:
            pokemon_different_types.add(entry["name"])
    except Exception as e:
        raise FailedExtractUniquePokemonTypesError(e)
    return pokemon_different_types
