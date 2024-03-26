from typing import Dict, Tuple
from adapters import pokemon_api

def get_typed_pokemon_list(generation_number: int) -> Dict[str, Tuple[str]]:
    species_from_gen = pokemon_api.get_species_from_generation(generation_number)

    return {
        name: pokemon_api.get_types(number) for (number, name) in species_from_gen.items()
    }
