from game.game_play import GamePlay
from game.di import obj_graph
from pprint import pprint

obj = obj_graph.provide(GamePlay)

game_stats = obj.start()


pprint([x.__dict__ for x in game_stats])
