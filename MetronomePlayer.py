import asyncio

from poke_env.environment import DoubleBattle
from poke_env.player import DoubleBattleOrder, Player
from poke_env.player.battle_order import (BattleOrder, DefaultBattleOrder,
                                          DoubleBattleOrder)

from utils import *


class MetronomePlayer(Player):
    def choose_move(self, battle:  DoubleBattle):

        doubles_move = choose_metronome_move(self, battle)

        return doubles_move