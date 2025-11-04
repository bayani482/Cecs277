import check_input
from beg_factory import BegFactory
from enemy_factory import EnemyFactory
from exp_factory import ExpFactory
from hero import Hero


def main():
    print("Monster Trials")
    name = input("What is your name? ")
    print(f"\nYou will face a series of 3 monsters, {name}.\nDefeat them all to win.")
    hero = Hero(name)
    
    beg_factory = BegFactory()
    exp_factory = ExpFactory()
    monsters = [beg_factory.create_random_enemy(),
                beg_factory.create_random_enemy(),
                exp_factory.create_random_enemy()]
    while hero._hp > 0 and len(monsters) > 0:
        print("Choose an enemy to attack:")
        for i, enemy in enumerate(monsters):
            print(f"{i + 1}. {str(enemy)}")
        choice = check_input.get_int_range(f"Enter choice (1-{len(monsters)}): ", 1, len(monsters))
        enemy = monsters[choice - 1]
        print("\nChoose your attack:\n1. Melee Attack\n2. Ranged Attack")
        attack_choice = check_input.get_int_range("Enter choice (1-2): ", 1, 2)
        match attack_choice:
            case 1:
                print(hero.melee_attack(enemy))
            case 2:
                print(hero.ranged_attack(enemy))
        if enemy._hp > 0:
            print(enemy.attack(hero))
            print(hero)
            print(enemy)
        elif enemy._hp <= 0:
            print(f"{enemy._name} has been slain!\n")
            monsters.pop(choice - 1)
            print(hero)

    if hero._hp <= 0:
        print("You have been slain. Game over.")
    else:
        print("Congratulations! You defeated all three monsters!\nGame Over")

if __name__ == "__main__":
    main()