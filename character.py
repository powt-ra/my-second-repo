import random


class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        multiplier = random.uniform(0.3, 0.9)
        damage = round(multiplier * self.attack_power, 1)
        other.hp = max(0, round(other.hp - damage, 1))
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
