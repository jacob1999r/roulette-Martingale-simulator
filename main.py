from bankroll import random_bankroll
from roulette import martingale_roulette

import csv
from datetime import datetime
from pathlib import Path

def main():
    print("Running simulation for punters of varying bankrolls.")
    # hardcoded values
    spins = 250
    min_initial_bankroll = 1000
    max_initial_bankroll = 1000
    initial_stake = 5

    # initialise csv file
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    out_dir = Path("SIMULATIONS")
    out_dir.mkdir(exist_ok=True)
    filename = out_dir / f"{spins}_spins-simulation_{timestamp}-stake{initial_stake}.csv"

    # add information
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Jacob K.C. Russell"])
        writer.writerow([])
        writer.writerow(["Run Time:", timestamp])
        writer.writerow(["Number of Spins:", spins])
        writer.writerow(["Bankroll Range:", "£" + str(min_initial_bankroll) + " to " + "£" + str(max_initial_bankroll)])
        writer.writerow(["Starting Stake:", "£" + str(initial_stake)])
        writer.writerow([])

        # run simulation and save each outcome to csv
        writer.writerow(["Name", "Initial Bankroll", "Final Bankroll"])
        for i in range(100):
            initial_bankroll = random_bankroll(min_initial_bankroll, max_initial_bankroll)
            final_bankroll = martingale_roulette(spins, initial_bankroll, initial_stake)
            #print("Initial bankroll: " + str(initial_bankroll) + ". " "Final bankroll: " + str(final_bankroll) + ".")
            writer.writerow(["[unknown]","£" + str(initial_bankroll), "£" + str(final_bankroll)])

main()
