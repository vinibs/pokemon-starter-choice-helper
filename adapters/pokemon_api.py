from typing import Tuple
from http import HTTPStatus
import requests

_base_url = 'https://pokeapi.co/api/v2'

def get_types(pokemon_name: str) -> Tuple[str]:
    url = f'{_base_url}/pokemon/{pokemon_name}'
    response = requests.get(url)

    if response.status_code != HTTPStatus.OK:
        return ()
    
    try:
        data = response.json()
        types_data = data.get("types")
        return tuple(type_data['type']['name'] for type_data in types_data)
    
    except Exception:
        return ()
