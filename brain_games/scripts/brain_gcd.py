#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.engine_game import start_game


def main():
    """Start game GCD"""
    start_game(gcd)


if __name__ == '__main__':
    main()
