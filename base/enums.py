from enum import Enum

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
    NEUTRAL = 'neutral'
    PARTIALLY_IMMUNE = 'partially_immune'
    IMMUNE = 'immune'
