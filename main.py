from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy2 = Character("Slime", 20 ,5)
    enemies = [enemy, enemy2]

    print(hero)
    print(enemy)
    print(enemy2)
    print()

    while hero.is_alive() and enemy.is_alive():
        if enemy.is_alive():
            hero.attack(enemy)
        else:
            hero.attack(enemy2)
        for e in enemies:
            if hero.is_alive() and enemy.is_alive():
                e.attack(hero)                  
        print(hero)
        print(enemy)
        print(enemy2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

if __name__ == "__main__":
    main()
