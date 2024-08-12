#!/usr/bin/env python3
from brain_games.scripts.games.even import game
from brain_games.scripts.games.engine_game import greeting


def main():
    game(greeting())


if __name__ == '__main__':
    main()
