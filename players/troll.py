#coding: utf-8
from things import Player


class Troll(Player):
    def next_step(self, things):
        self.status = 'healing myself'
        return 'heal', self

# (trolls have regenerative capabilities)


def create():
    return Troll('troll', 'blue')
