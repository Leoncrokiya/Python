import random

slayer = ["Tanjiro", "Rion", "Zenitsu", "Inosuke"]

upper_rank = ["Akaza", "Doma", "Kokushibo", "Kaigaku"]

for fight in range(len(slayer)):
    s = random.choice(slayer)
    ur = random.choice(upper_rank)
    
    slayer.remove(s)
    upper_rank.remove(ur)
    
    print(f"{s} fights {ur}")
    print()
