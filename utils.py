import random

from poke_env.environment.battle import Battle
from poke_env.environment.double_battle import DoubleBattle
from poke_env.environment.field import Field
from poke_env.environment.move import Move
from poke_env.environment.pokemon import Pokemon
from poke_env.environment.side_condition import SideCondition
from poke_env.environment.status import Status
from poke_env.exceptions import ShowdownException
from poke_env.player.battle_order import (BattleOrder, DefaultBattleOrder,
                                          DoubleBattleOrder)
from poke_env.player.player import Player
from poke_env.player.random_player import RandomPlayer


def choose_metronome_move(self, battle: DoubleBattle) -> BattleOrder:
    active_orders = [[], []]
    tera_used = False
    for (
        idx,
        (
            orders,
            mon,
            moves,
            can_tera,
        ),
    ) in enumerate(
        zip(
            active_orders,
            battle.active_pokemon,
            battle.available_moves,
            battle.can_tera,
        )
    ):
        if mon:
            if can_tera and not tera_used:
                tera_used = True
                orders.extend(
                    [
                        BattleOrder(move,
                                    terastallize=True)
                        for move in moves
                    ]
                )
            elif not tera_used:
                return DefaultBattleOrder()
            else:
                orders.extend(
                    [
                        BattleOrder(move)
                        for move in moves
                    ]
                )

    orders = DoubleBattleOrder.join_orders(*active_orders)

    return orders[int(random.random() * len(orders))]
