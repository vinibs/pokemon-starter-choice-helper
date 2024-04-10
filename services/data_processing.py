from typing import Dict, List, Tuple
from adapters import pokemon_api
from base.enums import AdvantageCondition
from services import advantage_calculation

def get_typed_pokemon_list(generation_number: int) -> Dict[str, Tuple[str]]:
    species_from_gen = pokemon_api.get_species_from_generation(generation_number)

    return {
        name: pokemon_api.get_types(number) for (number, name) in species_from_gen.items()
    }

def get_pokemon_advantage_relations(
    species_data: Tuple[str, Tuple[str]], other_pokemon_list: Dict[str, Tuple[str]]
) -> Dict[AdvantageCondition, List[Tuple[str, Tuple[str]]]]:
    advantage_relation = {
        AdvantageCondition.ADVANTAGE: [],
        AdvantageCondition.DISADVANTAGE: [],
        AdvantageCondition.NEUTRAL: [],
        AdvantageCondition.PARTIALLY_IMMUNE: [],
        AdvantageCondition.IMMUNE: [],
    }

    species_types = species_data[1]

    for listed_pokemon_name, listed_pokemon_types in other_pokemon_list.items():
        condition = advantage_calculation.calculate_species_types_advantage(species_types, listed_pokemon_types)

        advantage_relation[condition].append((listed_pokemon_name, listed_pokemon_types))
    
    return advantage_relation

def get_typed_starters_list(generation_number: int) -> Dict[str, Tuple[str]]:
    starters_names_list = pokemon_api.get_starters_names_from_generation(generation_number)

    if not starters_names_list:
        return {}
    
    return {
        starter_name: pokemon_api.get_types(pokemon_name=starter_name) for starter_name in starters_names_list
    }

def process_starters_advantages(generation_number: int) -> Dict[str, Dict[str, int]]:
    starters = get_typed_starters_list(generation_number)
    generation_pokemon_list = get_typed_pokemon_list(generation_number)

    return {
        starter_name: get_pokemon_advantage_relations((starter_name, starter_types), generation_pokemon_list)
        for starter_name, starter_types in starters.items()
    }
