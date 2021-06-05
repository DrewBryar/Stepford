import random
import numpy as np



def StatsRoller():
    results = [0, 0, 0 , 0]
    for i in range(0, 4):
        results[i] = random.randint(1,6)
    min = 6
    for x in results:
        if x < min:
            min = x
    statTotal = np.sum(results)-min

    print(results)
    if statTotal > 15:
        print(statTotal)
        print("Excellent roll!")
    else:
        print(statTotal)

    return(statTotal)

def StatSpread():
    stats = []
    for i in range(0, 7):
        stat = StatsRoller()
        stats.append(stat)
    print(stats)
    
    min = 18
    
    for stat in stats:
        if stat < min:
            min = stat
    
    statsTotal = np.sum(stats)-min
    if statsTotal <= 72:
        print("My condolences, but your stats seem low. Might I suggest taking the standard array of [15,14,13,12,10,8]?")
    else:
        print(stats)
        print(f"Your lowest stat is {min}. For optimal builds, I suggest dropping this, but consider the opportunity for roleplay with a weak stat.")


StatSpread()