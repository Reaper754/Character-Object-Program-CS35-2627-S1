from character import Character

assault = Character(100, "M4A1 Carbine", "Green", 30)
heavy = Character(150, "M249 SAW", "Johnson", 200)

select = """Choose your class:
1 for assault | 2 for heavy | 3 for exit\n"""

message = """Enter an input: 
| Shoot | Damage | Reload | Heal | Stats |\n"""

commands = [
    "shoot",
    "damage",
    "reload",
    "heal",
    "stats",
]

actions = [
    assault.shoot,
    assault.damage,
    assault.reload,
    assault.heal,
    assault.stats,
]

actions2 = [
    heavy.shoot,
    heavy.damage,
    heavy.reload,
    heavy.heal,
    heavy.stats,
]

while True:
    try:
        soldier = int(input(select))
        if soldier == 1:
            user_input = input(message).strip().lower()
            for command, action in zip(commands, actions):
                if user_input == command:
                    action()
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        elif soldier == 2:
            user_input = input(message).strip().lower()
            for command, action2 in zip(commands, actions2):
                if user_input == command:
                    action2()
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        else:
            if soldier == 3:
                break
            print("Invalid command.")
    except ValueError:
        print("Invalid input")

