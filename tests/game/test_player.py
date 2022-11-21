from game.player import Player


def test_player_object():
    pl = Player()
    fix = {
        "healthpoints": 53,
        "luck": 86,
        "player_name": "mishra",
        "skills": ["RapidFire", "HoneyBadger"],
        "strangth": 100,
        "strike": "HoneyBadger",
    }
    res = map(lambda x: x if hasattr(pl, x) else False, list(fix.keys()))
    assert list(res) == list(fix.keys())
