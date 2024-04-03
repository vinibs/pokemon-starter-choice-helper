from enum import Enum
from typing import Any, Dict, Tuple


class Types(Enum):
    NORMAL = 'normal'
    FIRE = 'fire'
    WATER = 'water'
    ELECTRIC = 'electric'
    GRASS = 'grass'
    ICE = 'ice'
    FIGHTING = 'fighting'
    POISON = 'poison'
    GROUND = 'ground'
    FLYING = 'flying'
    PSYCHIC = 'psychic'
    BUG = 'bug'
    ROCK = 'rock'
    GHOST = 'ghost'
    DRAGON = 'dragon'
    DARK = 'dark'
    STEEL = 'steel'
    FAIRY = 'fairy'

    @staticmethod
    def list():
        return list(map(lambda t: t.value, Types))
    
class AdvantageCondition(Enum):
    ADVANTAGE = 'advantage'
    DISADVANTAGE = 'disadvantage'
    PARTIALLY_IMMUNE = 'partially_immune'
    IMMUNE = 'immune'

_types_damage_multiplier_relation = {
    Types.NORMAL.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 0.5,
        Types.GHOST.value: 0,
        Types.DRAGON.value: 1,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
    Types.FIRE.value: {     
        Types.NORMAL.value: 1,
        Types.FIRE.value: 0.5,
        Types.WATER.value: 0.5,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 2,
        Types.ICE.value: 2,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 2,
        Types.ROCK.value: 0.5,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 0.5,
        Types.DARK.value: 1,
        Types.STEEL.value: 2,
        Types.FAIRY.value: 1,
    },
    Types.WATER.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 2,
        Types.WATER.value: 0.5,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 0.5,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 2,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 2,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 0.5,
        Types.DARK.value: 1,
        Types.STEEL.value: 1,
        Types.FAIRY.value: 1,
    },
    Types.ELECTRIC.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 2,
        Types.ELECTRIC.value: 0.5,
        Types.GRASS.value: 0.5,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 0,
        Types.FLYING.value: 2,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 0.5,
        Types.DARK.value: 1,
        Types.STEEL.value: 1,
        Types.FAIRY.value: 1,
    },
    Types.GRASS.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 0.5,
        Types.WATER.value: 2,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 0.5,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 0.5,
        Types.GROUND.value: 2,
        Types.FLYING.value: 0.5,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 0.5,
        Types.ROCK.value: 2,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 0.5,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
    Types.ICE.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 0.5,
        Types.WATER.value: 0.5,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 2,
        Types.ICE.value: 0.5,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 2,
        Types.FLYING.value: 2,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 2,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
    Types.FIGHTING.value: {
        Types.NORMAL.value: 2,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 2,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 0.5,
        Types.GROUND.value: 1,
        Types.FLYING.value: 0.5,
        Types.PSYCHIC.value: 0.5,
        Types.BUG.value: 0.5,
        Types.ROCK.value: 2,
        Types.GHOST.value: 0,
        Types.DRAGON.value: 1,
        Types.DARK.value: 2,
        Types.STEEL.value: 2,
        Types.FAIRY.value: 0.5,
    },
    Types.POISON.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 2,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 0.5,
        Types.GROUND.value: 0.5,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 0.5,
        Types.GHOST.value: 0.5,
        Types.DRAGON.value: 1,
        Types.DARK.value: 1,
        Types.STEEL.value: 0,
        Types.FAIRY.value: 2,
    },
    Types.GROUND.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 2,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 2,
        Types.GRASS.value: 0.5,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 2,
        Types.GROUND.value: 1,
        Types.FLYING.value: 0,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 0.5,
        Types.ROCK.value: 2,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 1,
        Types.DARK.value: 1,
        Types.STEEL.value: 2,
        Types.FAIRY.value: 1,
    },
    Types.FLYING.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 0.5,
        Types.GRASS.value: 2,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 2,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 2,
        Types.ROCK.value: 0.5,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 1,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
    Types.PSYCHIC.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 2,
        Types.POISON.value: 2,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 0.5,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 1,
        Types.DARK.value: 0,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
    Types.BUG.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 0.5,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 2,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 0.5,
        Types.POISON.value: 0.5,
        Types.GROUND.value: 1,
        Types.FLYING.value: 0.5,
        Types.PSYCHIC.value: 2,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 0.5,
        Types.DRAGON.value: 1,
        Types.DARK.value: 2,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 0.5,
    },
    Types.ROCK.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 2,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 2,
        Types.FIGHTING.value: 0.5,
        Types.POISON.value: 1,
        Types.GROUND.value: 0.5,
        Types.FLYING.value: 2,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 2,
        Types.ROCK.value: 1,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 1,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
    Types.GHOST.value: {
        Types.NORMAL.value: 0,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 2,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 2,
        Types.DRAGON.value: 1,
        Types.DARK.value: 0.5,
        Types.STEEL.value: 1,
        Types.FAIRY.value: 1,
    },
    Types.DRAGON.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 2,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 0,
    },
    Types.DARK.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 1,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 0.5,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 2,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 2,
        Types.DRAGON.value: 1,
        Types.DARK.value: 0.5,
        Types.STEEL.value: 1,
        Types.FAIRY.value: 0.5,
    },
    Types.STEEL.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 0.5,
        Types.WATER.value: 0.5,
        Types.ELECTRIC.value: 0.5,
        Types.GRASS.value: 1,
        Types.ICE.value: 2,
        Types.FIGHTING.value: 1,
        Types.POISON.value: 1,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 2,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 1,
        Types.DARK.value: 1,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 2,
    },
    Types.FAIRY.value: {
        Types.NORMAL.value: 1,
        Types.FIRE.value: 0.5,
        Types.WATER.value: 1,
        Types.ELECTRIC.value: 1,
        Types.GRASS.value: 1,
        Types.ICE.value: 1,
        Types.FIGHTING.value: 2,
        Types.POISON.value: 0.5,
        Types.GROUND.value: 1,
        Types.FLYING.value: 1,
        Types.PSYCHIC.value: 1,
        Types.BUG.value: 1,
        Types.ROCK.value: 1,
        Types.GHOST.value: 1,
        Types.DRAGON.value: 2,
        Types.DARK.value: 2,
        Types.STEEL.value: 0.5,
        Types.FAIRY.value: 1,
    },
}


def _calculate_types_damage_points(attacker_types: Tuple[str], defender_types: Tuple[str]) -> int:
    damage_points = 1

    for attack_type in attacker_types:
        if attack_type not in Types.list():
            raise Exception('invalid_attacker_type', attack_type)

        for defense_type in defender_types:
            if defense_type not in Types.list():
                raise Exception('invalid_defense_type', defense_type)
            
            types_damage = _types_damage_multiplier_relation[attack_type][defense_type]
            damage_points = damage_points * types_damage

    return damage_points


def _calculate_types_immunity(defender_types: Tuple[str], attacker_types: Tuple[str]) -> AdvantageCondition:
    damage_multipliers = []

    for attack_type in attacker_types:
        if attack_type not in Types.list():
            raise Exception('invalid_attacker_type', attack_type)

        for defense_type in defender_types:
            if defense_type not in Types.list():
                raise Exception('invalid_defense_type', defense_type)
            
            types_damage = _types_damage_multiplier_relation[attack_type][defense_type]
            damage_multipliers.append(types_damage)

    if 0 not in damage_multipliers:
        immunity_condition = None

    else:
        full_immunity = set(damage_multipliers) == {0} 
        immunity_condition = AdvantageCondition.IMMUNE if full_immunity else AdvantageCondition.PARTIALLY_IMMUNE

    return immunity_condition
