from typing import Any, Dict, Tuple
from http import HTTPStatus
import re
import requests

_base_url = 'https://pokeapi.co/api/v2'

def _handle_request(url: str, extract_data: callable) -> Any:
    response = requests.get(url)

    if response.status_code != HTTPStatus.OK:
        return ()
    
    try:
        json_data = response.json()
        return extract_data(json_data)
    
    except Exception:
        return ()

def get_types(pokemon_name: str) -> Tuple[str]:
    url = f'{_base_url}/pokemon/{pokemon_name}'

    def extract_types(json_data: Any) -> Tuple[str]:
        types_data = json_data.get('types')
        return tuple(type_data['type']['name'] for type_data in types_data)
    
    return _handle_request(url, extract_types)

def get_species_from_generation(generation_number: int) -> Dict[int, str]:
    url = f'{_base_url}/generation/{generation_number}'

    def extract_number_from_url(species_url: str) -> str:
        pattern = r'https:\/\/pokeapi\.co\/api\/v2\/pokemon-species\/(\d+)\/'

        if search_result := re.search(pattern, species_url):
            return search_result.group(1)
        
        return None

    def extract_species(json_data: Any) -> Dict[int, str]:
        species_data = json_data.get('pokemon_species')

        data = {int(extract_number_from_url(poke_data['url'])): poke_data['name'] for poke_data in species_data}
        return dict(sorted(data.items()))
    
    return _handle_request(url, extract_species)
