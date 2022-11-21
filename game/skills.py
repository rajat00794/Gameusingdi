class Skills:
    def __init__(self, config: object) -> None:
        self.type = "skill"
        self.config = config.get_config(type_=self.type)

    def get_skill(self):
        skilla = []
        skilld = []
        for i in self.config[0]["data"]:
            if i["type"] == "Offensive":
                skilla.append(i["skillname"])
            else:
                skilld.append(i["skillname"])
        return skilla, skilld

    def luckstrike(self, player, player2):
        if player.strike == "LuckyStrike":
            player2.strangth = 0
        else:
            if player2.strike == "LuckyStrike":
                player.strangth = 0
        return player2, player

    def rapidfire(self, player, player2):
        if player.strike == "RapidFire":
            player.strike = "LuckyStrike"
            self.luckstrike(player, player2)
            self.luckstrike(player, player2)
            player.strike = "RapidFire"
        else:
            if player2.strike == "RapidFire":
                player2.strike = "LuckyStrike"
                self.luckstrike(player, player2)
                self.luckstrike(player, player2)
                player2.strike = "RapidFire"
        return player2, player

    def lifetap(self, player, player2):
        if player.strike == "LifeTap":
            player.helthpoints += player2.damage % 50
        else:
            if player2.strike == "LifeTap":
                player2.helthpoints += player.damage % 50
        return player2, player

    def honeybadger(self, player, player2):
        if player.strike == "HoneyBadger":
            player.strangth = player.strangth
        else:
            if player2.strike == "HoneyBadger":
                player2.strangth = player2.strangth
        return player2, player

    def refuseresist(self, player, player2):
        if player.strike == "RefuseResist":
            player.damage += player.damage % 50
        else:
            if player2.strike == "RefuseResist":
                player2.damage += player2.damage % 50
        return player2, player

    def antifragile(self, player, player2):
        if player.strike == "Antifragile":
            player.healthpoints += player.damage % 50
        else:
            if player2.strike == "Antifragile":
                player2.healthpoints += player.damage % 50

        return player2, player
