import random

def martingale_roulette(spins: int, bankroll: int, initial_stake: int):
    stake = initial_stake
    for i in range(spins):
        if bankroll < stake:
            #handle scenario where punter runs out of money
            print("Not enough money to continue!")
            break
        if random.random()*(37) > 18:
            #outcome where punter loses
            bankroll = bankroll - stake
            stake = stake*2
        else:
            #outcome where they win, return to intial stake
            bankroll = bankroll + (stake*2)
            stake = initial_stake
    return (bankroll)

