from PokemonBattles.constants import *


class Pokemon:
    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = []  # attacks vector
        self.stats = {}
        self.baseStats = {}
        self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0
        self.nature = None

    def compute_stats(self):
        self.stats = {
            HP: self.compute_hp_stat(),
            ATTACK: self.compute_standard_stat(ATTACK),
            DEFENSE: self.compute_standard_stat(DEFENSE),
            SPATTACK: self.compute_standard_stat(SPATTACK),
            SPDEFENSE: self.compute_standard_stat(SPDEFENSE),
            SPEED: self.compute_standard_stat(SPEED)
        }

    def compute_hp_stat(self):
        hp = int((2 * self.baseStats[HP] + self.iv[HP] + int(self.ev[HP] / 4)) * self.level / 100)
        return hp + self.level + 10

    def compute_standard_stat(self, stat):
        value_stat = int((2 * self.baseStats[stat] + self.iv[stat] + int(self.ev[stat] / 4)) * self.level / 100)
        return int((value_stat + 5) * NATURE_MATRIX[self.nature][stat])


class Attack:
    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
