from typing import Any, Tuple
from http import HTTPStatus
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
