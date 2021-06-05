import random
import numpy as np



def StatsRoller():
    results = [0, 0, 0 , 0]
    for i in range(0, 4):
        results[i] = random.randint(1,6)
    
    return(results)

def StatSpread():
    #Make a place to store the rolls.
    statList =[]
    # Roll the Dice 7 times
    for i in range(0,7):
        # Make a list of 4 Rolled d6
        diceRolls = StatsRoller()
        # Find the minimum
        lowestRoll = min(diceRolls)
        # Remove the lowest roll from the dice rolls.
        diceRolls.remove(lowestRoll)
        # I want as much transparency passed to the bot as possible. Maybe there is something cleaner, but for now we need this ugly data structure.
        diceRollsAndTotal = [diceRolls, sum(diceRolls), lowestRoll]
        # Add it to the Stat List
        statList.append(diceRollsAndTotal)
    
    return statList


