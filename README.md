<!-- ABOUT THE PROJECT -->

## About The Project

Hi there! I've been enjoying metronome battles on [Pokémon Showdown](https://play.pokemonshowdown.com/), but found it a bit tedious to have to manually play through each game.
I created this simple bot to play for you, so you can spend your time building a better team!

I used this and was able to hit rank 1 on the `gen9metronomebattle` ladder!

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

This project uses [Poke-env](https://poke-env.readthedocs.io/en/latest/), which requires python >= 3.8 to be installed. Their documentation is great so please do check it out!

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install poke-env
   ```sh
   pip install poke-env
   ```

<!-- USAGE EXAMPLES -->

## Usage

You'll need a couple things before you start laddering:

1. Account information. Feel free to edit `authentication.txt` with your account information:

2. A winning team! Take your team in showdown and copy-paste it into `pokemon_team.txt` (You're welcome to use my team as well!).

3. Currently the bot is set to play 10 games, with up to 5 games at a time. Feel free to edit these as you wish, but do note that Showdown may (understandably) limit you to a certain number of concurrent games.

4. Run the bot with:
   ```sh
   python bot.py
   ```
