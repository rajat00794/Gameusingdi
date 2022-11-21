from game.game_play import GamePlay
from game.di import obj_graph


def test_game_play():
    obj = obj_graph.provide(GamePlay)
    assert obj.assign() == True
    assert obj.ready() == True
    assert isinstance(obj.start(), tuple) == True
