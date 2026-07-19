# William Littlefield
# July 18 2026
# Final Project    
# Text based game



"""
A Simple Text-Based RPG
------------------------
Create your character, then face off against a series of random monsters!
"""

import random
import time
import sys


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def slow_print(text, delay=0.015):
    """Prints text with a small delay per character for a bit of drama."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def divider():
    print("-" * 50)


# ---------------------------------------------------------------------------
# Character / Monster classes
# ---------------------------------------------------------------------------

class Character:
    def __init__(self, name, health, armor, weapon):
        self.name = name
        self.max_health = health
        self.health = health
        self.armor = armor
        self.weapon = weapon

    @property
    def is_alive(self):
        return self.health > 0

    def take_damage(self, raw_damage):
        # Armor absorbs part of the damage; always take at least 1
        mitigated = max(1, raw_damage - (self.armor // 2))
        self.health = max(0, self.health - mitigated)
        return mitigated

    def health_bar(self):
        pct = self.health / self.max_health if self.max_health else 0
        filled = int(pct * 20)
        return f"[{'#' * filled}{'-' * (20 - filled)}] {self.health}/{self.max_health} HP"


class Monster(Character):
    def __init__(self, name, health, weapon, damage_range, flavor=""):
        super().__init__(name, health, armor=0, weapon=weapon)
        self.damage_range = damage_range
        self.flavor = flavor

    def attack_damage(self):
        return random.randint(*self.damage_range)


WEAPON_DAMAGE = {
    "Sword": (8, 14),
    "Bow and Arrow": (6, 12),
    "Staff": (5, 10),
}
# changed the weapon dmg to make it more balanced when going against larry

# ---------------------------------------------------------------------------
# Character creation
# ---------------------------------------------------------------------------

def create_character():
    divider()
    slow_print("CHARACTER CREATION")
    divider()

    name = input("Enter your character's name: ").strip()
    if not name:
        name = "Hero"

    base_health = 50
    base_armor = 10
    weapon = random.choice(["Sword", "Bow and Arrow", "Staff"])

    player = Character(name, base_health, base_armor, weapon)

    print()
    slow_print(f"Welcome, {player.name}!")
    print(f"  Health: {player.health}")
    print(f"  Armor:  {player.armor}")
    print(f"  Weapon: {player.weapon}")
    divider()
    return player


# ---------------------------------------------------------------------------
# Monster generation
# ---------------------------------------------------------------------------
    # I went back and changed the chances of each monster spawning to make the game more balanced.
    # I also added a new monster, Larry the Lich, to add more variety and comedy
def spawn_monster():
    roll = random.random()  # 0.0 - 1.0
    
    if roll < 0.30:
        return Monster(
            name="Goblin",
            health=10,
            weapon="Dagger",
            damage_range=(0, 6),
            flavor="A small, snarling goblin clutches a rusty dagger.",
        )
    elif roll < 0.60:
        return Monster(
            name="Bandit",
            health=15,
            weapon="Sword",
            damage_range=(2, 9),
            flavor="A rough-looking bandit draws a worn sword.",
        )
    elif roll < 0.80:
        return Monster(
            name = "Larry the Lich",
            health = 70,
            weapon="Arcane spatula",
            damage_range=(5, 18),
            flavor="A suburban dad wielding an ancient arcane spatula.",
        )
    else:
        spell = random.choice(["Ice", "Fire", "Poison"])
        return Monster(
            name="Beholder",
            health=50,
            weapon=f"{spell} Spell",
            damage_range=(3, 15),
            flavor=f"A floating beholder's central eye glows with {spell.lower()} energy!",
        )


def generate_encounters(count=3):
    return [spawn_monster() for _ in range(count)]


# ---------------------------------------------------------------------------
# Combat
# ---------------------------------------------------------------------------

def combat(player, monster):
    divider()
    slow_print(f"A wild {monster.name} appears!")
    print(monster.flavor)
    print(f"{monster.name} is armed with: {monster.weapon}")
    divider()

    while player.is_alive and monster.is_alive:
        print()
        print(f"{player.name}: {player.health_bar()}")
        print(f"{monster.name}: {monster.health_bar()}")
        print()
        print("What will you do?")
        print("  1. Attack")
        print("  2. Flee")
        print("  3. Heal (restore 10 HP, can only be used once per encounter)")
        choice = input("> ").strip()

        if choice == "2":
            slow_print(f"{player.name} flees from the {monster.name}!")
            return "fled"
        # I felt that the game needed a way to heal, so I added this option. It can only be used once per encounter.
        elif choice == "3":
            if hasattr(player, 'healed') and player.healed:
                slow_print("You have already healed once in this encounter!")
            else:
                player.health = min(player.max_health, player.health + 10)
                player.healed = True
                slow_print(f"{player.name} heals for 10 HP! Current health: {player.health}/{player.max_health}")
            continue

        # Player attacks
        min_dmg, max_dmg = WEAPON_DAMAGE[player.weapon]
        dmg = random.randint(min_dmg, max_dmg)
        monster.health = max(0, monster.health - dmg)
        slow_print(f"{player.name} strikes with their {player.weapon} for {dmg} damage!")

        if not monster.is_alive:
            slow_print(f"The {monster.name} has been defeated!")
            return "won"

        # Monster attacks back
        raw_dmg = monster.attack_damage()
        taken = player.take_damage(raw_dmg)
        slow_print(f"The {monster.name} hits {player.name} for {taken} damage (after armor)!")

        if not player.is_alive:
            slow_print(f"{player.name} has fallen in battle...")
            return "lost"

    return "won" if player.is_alive else "lost"


# ---------------------------------------------------------------------------
# Main game loop
# ---------------------------------------------------------------------------

def main():
    slow_print("=== TEXT ADVENTURE ===")
    player = create_character()
    monsters = generate_encounters(3)
    

    for i, monster in enumerate(monsters, start=1):
        if not player.is_alive:
            break
        print()
        slow_print(f"--- Encounter {i} of {len(monsters)} ---")
        result = combat(player, monster)

        if result == "lost":
            divider()
            slow_print("GAME OVER")
            try_again = input("Would you like to try again? (y/n): ").strip().lower()
            if try_again == "y":
                main()  # added a restart game option if the player loses
            divider()
            return
        elif result == "fled":
            divider()
            slow_print("You chose to flee. Your adventure ends here.")
            divider()
            return

    if player.is_alive:

        divider()
        slow_print(f"Congratulations, {player.name}! You survived all {len(monsters)} encounters!")
        
        divider()
 
 
if __name__ == "__main__":
    main()

   # I attempted to make a second level basically with better loot and stronger monsters that you'll see in my AI submission
   # but ultimatley it was proof that AI is not perfect and it caused more issues than I expected and due to time restraints
   # I wasnt able to figure out where the issue was so I reverted back to the original