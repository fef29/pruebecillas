from PokemonBattles.constants import *


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0

    def is_finished(self):
        finished = self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0
        if finished:
            self.print_winner()
        return finished

    def print_winner(self):
        if self.pokemon1.current_hp <= 0 < self.pokemon2.current_hp:
            print(self.pokemon2 + ' won in ' + str(self.actual_turn) + ' turns!!')

        elif self.pokemon2.current_hp <= 0 < self.pokemon1.current_hp:
            print(self.pokemon1.name + ' won in ' + str(self.actual_turn) + ' turns!!')

        else:
            print('Double KO!!!')

    def execute_turn(self, turn):
        command1 = turn.command1
        command2 = turn.command2

        attack1 = None
        attack2 = None

        if DO_ATTACK in command1.action.keys():
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]
        if DO_ATTACK in command2.action.keys():
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]

        # Execute Attacks
        self.pokemon2.current_hp -= self.compute_damage(attack1)
        self.pokemon1.current_hp -= self.compute_damage(attack2, from1to2=False)

        self.actual_turn += 1

    def print_current_status(self):
        print(self.pokemon1.name + ' has ' + str(self.pokemon1.current_hp) + ' left!')
        print(self.pokemon2.name + ' has ' + str(self.pokemon2.current_hp) + ' left!')

    def compute_damage(self, attack, from1to2=True):
        if from1to2:
            if attack.type == PHYSICAL:
                powerFactor = self.pokemon1.stats[ATTACK] / self.pokemon2.stats[DEFENSE]
            elif attack.type == SPECIAL:
                powerFactor = self.pokemon1.stats[SPATTACK] / self.pokemon2.stats[SPDEFENSE]
        else:
            if attack.type == PHYSICAL:
                powerFactor = self.pokemon2.stats[ATTACK] / self.pokemon1.stats[DEFENSE]
            elif attack.type == SPECIAL:
                powerFactor = self.pokemon2.stats[SPATTACK] / self.pokemon1.stats[SPDEFENSE]

        damage_without_modifier = powerFactor * 50 + 2

        return 0

    def compute_damage_modifier(self, attack):
        pass


class Turn:
    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1 is not None and self.command2 is not None


class Command:
    def __init__(self, action):
        self.action = action
