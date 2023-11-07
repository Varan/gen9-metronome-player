import asyncio

from poke_env.player_configuration import PlayerConfiguration
from poke_env.server_configuration import ShowdownServerConfiguration

from MetronomePlayer import MetronomePlayer


async def main():
    print("Starting up bot!")

    # Import Pokemon team and Pokemon Showdown account information
    with open('pokemon_team.txt', 'r') as f:
        team_paste = f.read()

    with open('authentication.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]
        username, password = lines

    # Create a player with the online server configuration
    player = MetronomePlayer(
        player_configuration=PlayerConfiguration(username, password),
        server_configuration=ShowdownServerConfiguration,
        battle_format="gen9metronomebattle",
        team=team_paste,
        max_concurrent_battles=5,
    )

    # Play 10 games on the ladder
    await player.ladder(10)

    # Print the rating of the player and its opponent after each battle
    for battle in player.battles.values():
        print(battle.rating, battle.opponent_rating)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())