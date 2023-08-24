class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self, enemy):
        enemy.take_damage(self.damage)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, damage=30)

    def special_ability(self, enemy):
        enemy.take_damage(self.damage*2)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=60, damage=45)

    def special_ability(self, enemy):
        self.health += 15
        for i in range(3):
            enemy.take_damage(10)


class StoryGame:
    def __init__(self):
        self.player = None
        self.current_enemy = None
        self.story_progress = 0
        self.choices = [
            "1.Explore the forest",
            "2.Enter the cave",
            "3.Return to village",
            "4.Exit"
        ]

    def start(self):
        print("Welcome to the game!")
        player_name = input("What is your name?")
        player_class = input("Are you a Warrior or Mage?").lower()
        if player_class == "warrior":
            self.player = Warrior(player_name)
        elif player_class == "mage":
            self.player = Mage(player_name)
        else:
            print("Invalid class")
            self.player = Warrior(player_name)
        self.play()

    def play(self):
        print(
            f"Welcome {self.player.name} the amazing {type(self.player).__name__}!")
        print("You at a crossroad. What do you do?\n")
        while self.player.is_alive():
            print("\n".join(self.choices))
            choice = input("Enter your choice: ")
            if choice == "1":
                self.explore_forest()
            elif choice == "2":
                self.enter_cave()
            elif choice == "3":
                self.return_to_village()
            elif choice == "4":
                break
            else:
                print("Invalid choice")
        print("Game Over")

    def explore_forest(self):
        print("You are in a forest. You see a Troll.")
        self.current_enemy = Character(name="Troll", health=100, damage=30)
        self.battle()

    def enter_cave(self):
        print("You are in a cave. You see  Harry Potter.")
        self.current_enemy = Character(
            name="Harry Potter", health=60, damage=45)
        self.battle()

    def return_to_village(self):
        print("You are in a village.")
        self.player.health += 10
        self.story_progress += 1
        if self.story_progress > 4:
            self.player.damage += 20
        print(f"Your current progress is {self.story_progress} .")

    def battle(self):
        i = 1
        while self.current_enemy.is_alive() and self.player.is_alive():
            print(f"{self.player.name} (Health: {self.player.health}) vs {self.current_enemy.name} (Health: {self.current_enemy.health})")
            action = input(
                "Enter 'a' to attack, 's' to special attack, 'r' to run: ").lower()
            if action == "a":
                self.player.attack_enemy(self.current_enemy)
                i += 1
                if self.current_enemy.is_alive():
                    self.current_enemy.attack_enemy(self.player)
            elif action == "s" and i % 3 == 0:
                self.player.special_ability(self.current_enemy)
                if self.current_enemy.is_alive():
                    self.current_enemy.attack_enemy(self.player)
            elif action == "r":
                print("You run away.")
                break
            else:
                print("Invalid action")
        if not self.current_enemy.is_alive():
            print(f"{self.current_enemy.name} is dead.")
            self.story_progress += 1


game = StoryGame()
game.start()
