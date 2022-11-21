import random


class GamePlay:
    def __init__(self, player: object, player2: object, skill: object) -> None:
        self.player = player
        self.player2 = player2
        self.skill = skill

    def start(self):
        if self.ready():
            self.player.player_name = input("enter player1 name:") or "test"
            self.player2.player_name = input("enter player2 name:") or "testm"
            self.player.strike = random.choice(self.player.skills)
            self.player2.strike = random.choice(self.player2.skills)
            if hasattr(self.skill, self.player.strike.lower()):
                getattr(self.skill, self.player.strike.lower())(
                    self.player, self.player2
                )
            if hasattr(self.skill, self.player2.strike.lower()):
                getattr(self.skill, self.player2.strike.lower())(
                    self.player, self.player2
                )
            return self.player, self.player2

    def assign(self):
        self.player.healthpoints = random.randint(30, 90)
        self.player2.healthpoints = random.randint(30, 90)
        skills = self.skill.get_skill()
        self.player.skills = [random.choice(skills[0]), random.choice(skills[1])]
        self.player2.skills = [random.choice(skills[0]), random.choice(skills[1])]
        self.player2.luck = random.randint(15, 90)
        self.player.luck = random.randint(15, 90)
        self.player.strangth = 100
        self.player2.strangth = 100
        return True

    def ready(self):
        return self.assign()
