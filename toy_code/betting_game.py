import numpy as np
import math

multiply_factor = 2


def betting_game(bets):
    is_won = True if np.random.rand() > 0.5 else False

    return bets * multiply_factor if is_won else -bets * multiply_factor


def main():
    start_money = 10000000000
    min_bet = 1000

    print(f'Your start seed money is {start_money:,}')

    seed_money = start_money
    game_play_count = start_money // min_bet
    bets = min_bet
    max_m = 0
    min_m = start_money
    for i in range(game_play_count):
        if seed_money <= 0:
            print(f'You lose in {i}th game. End game')
            print(f'bets: {bets:,}, seed_money: {seed_money:,}, max_seed: {max_m:,}')
            exit(0)

        result = betting_game(bets=bets)
        seed_money += result

        if result <= 0:
            bets *= multiply_factor
        else:
            bets = min_bet

        if seed_money > max_m:
            max_m = seed_money
        if seed_money < min_m:
            min_m = seed_money

    print(f'You earned {(seed_money - start_money):,}, max_seed: {max_m:,}')


if __name__ == '__main__':
    main()
