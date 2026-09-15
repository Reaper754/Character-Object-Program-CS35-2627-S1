class Character:
    def __init__(self, health, weapon, name, ammo):
        self.health = health
        self.weapon = weapon
        self.name = name
        self.ammo = ammo
        self.rank = "Private"

    def shoot(self):
        if self.health == 0:
            print(f"{self.rank} {self.name} is downed and cannot shoot.")
        else:
            if self.ammo == 0:
                print (f"Click. {self.rank} {self.name} needs to reload.")
            elif self.weapon == "M249 SAW":
                self.ammo -= 10
                print(f"Brrrr! {self.rank} {self.name} fired ten rounds.")
            else:
                self.ammo -= 1
                print(f"Bang! {self.rank} {self.name} fired a round.")

    def damage(self):
        if self.health == 0:
            print(f"{self.rank} {self.name} is already downed.")
        else:
            amount = int(input(f"How much damage should {self.rank} {self.name} take?"))
            self.health -= amount
            print(f"{self.rank} {self.name} took {amount} points of damage.")
            if self.health == 0:
                print(f"{self.rank} {self.name} is now downed")
            elif self.health < 0:
                self.health = 0
                print(f"{self.rank} {self.name} is now downed")

    def reload(self):
        if self.health == 0:
            print(f"{self.rank} {self.name} is downed and cannot reload.")
        else:
            if self.ammo != 0:
                if self.weapon == "M249 SAW":
                    self.ammo = 200
                    print(f"{self.rank} {self.name} reloaded to 201")
                else:
                    self.ammo = 31
                    print(f"{self.rank} {self.name} reloaded to 31")
            else:
                if self.weapon == "M249 SAW":
                    self.ammo = 200
                    print(f"{self.rank} {self.name} reloaded to 200")
                else:
                    self.ammo = 30
                    print(f"{self.rank} {self.name} reloaded to 30")

    def heal(self):
        if self.name == "Johnson":
            if self.health == 150:
                print(f"{self.rank} {self.name} are already at max health.")
            else:
                self.health += 50
                print(f"{self.rank} {self.name} has healed 50 health points.")
                if self.health > 150:
                    self.health = 150
                self.stats()
        else:
            if self.health == 100:
                print(f"{self.rank} {self.name} are already at max health.")
            else:
                self.health += 50
                print(f"{self.rank} {self.name} has healed 50 health points.")
                if self.health > 100:
                    self.health = 100
                self.stats()

    def stats(self):
        print(f"health: {self.health}, Weapon: {self.weapon}, Name: {self.name}, Ammo: {self.ammo}, Rank: {self.rank}")