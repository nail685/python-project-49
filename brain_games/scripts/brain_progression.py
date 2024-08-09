#!/usr/bin/env python3
from brain_games.games.progression import game
from brain_games.games.engine_game import greeting


def main():
    game(greeting())


if __name__ == '__main__':
    main()