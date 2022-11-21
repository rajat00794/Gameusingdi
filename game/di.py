import pinject
from .player import Player
from .skills import Skills
from .gconfig import Config


class Player2(Player):
    pass


class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind("player", to_class=Player)
        bind("player2", to_class=Player2)
        bind("skill", to_class=Skills)
        bind("config", to_class=Config)


obj_graph = pinject.new_object_graph(binding_specs=[MyBindingSpec()])
