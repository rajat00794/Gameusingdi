from game.di import obj_graph
from game.skills import Skills
from game.player import Player


def test_skills():
    obj = obj_graph.provide(Skills)
    config = obj.get_skill()
    assert type(config) == tuple
    fix = {
        "healthpoints": 53,
        "luck": 86,
        "player_name": "mishra",
        "skills": ["LuckyStrike", "HoneyBadger"],
        "strangth": 100,
        "strike": "HoneyBadger",
    }
    player = Player()
    player2 = Player()
    map(lambda x: setattr(player, x, fix[x]), list(fix.keys()))
    map(lambda x: setattr(player2, x, fix[x]), list(fix.keys()))
    luckystrike = obj.luckstrike(player, player2)
    assert type(luckystrike) == tuple
    rapidfire = obj.rapidfire(player, player2)
    assert isinstance(rapidfire, tuple) == True
    lifetap = obj.lifetap(player, player2)
    assert isinstance(lifetap, tuple) == True
    honeybadger = obj.honeybadger(player, player2)
    assert isinstance(honeybadger, tuple) == True
    refuseresist = obj.refuseresist(player, player2)
    assert isinstance(refuseresist, tuple) == True
    antifragile = obj.antifragile(player, player2)
    assert isinstance(antifragile, tuple) == True
