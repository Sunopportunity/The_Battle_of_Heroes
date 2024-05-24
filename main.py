import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Здоровье: {self.health})"

class Game:
    def __init__(self):
        self.player = None
        self.computer = None

    def create_player(self):
        name = input("Введите имя своего героя: ")
        self.player = Hero(name)

    def create_computer(self):
        names = ["Draco", "Fenrir", "Balrog", "Sauron", "Smaug"]
        name = random.choice(names)
        attack_power = random.randint(15, 25)
        self.computer = Hero(name, attack_power=attack_power)

    def start(self):
        self.create_player()
        self.create_computer()
        print(f"Ваш герой: {self.player}")
        print(f"Противник: {self.computer}")

        player_turn = True  # Определяет, кто начинает первым

        while self.player.is_alive() and self.computer.is_alive():
            if player_turn:
                self.player.attack(self.computer)
                print(self.computer)
            else:
                self.computer.attack(self.player)
                print(self.player)

            player_turn = not player_turn

            input("Нажмите Enter для следующего раунда...")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

if __name__ == "__main__":
    game = Game()
    game.start()
