from bankroll import random_bankroll
from roulette import martingale_roulette

def main():
    print("Running simulation for punters of varying bankrolls.")
    #hardcoded values
    for i in range(100):
        initial_bankroll = random_bankroll(1, 2000)
        final_bankroll = martingale_roulette(100, initial_bankroll, 1)
        print("Initial bankroll: " + str(initial_bankroll) + ". " "Final bankroll: " + str(final_bankroll) + ".")

main()
