import random

slayer = ["Tanjiro", "Rion", "Zenitsu", "Inosuke", "Kanao"]

upper_rank = ["Akaza", "Doma", "Nakime", "Kokushibo", "Kaigaku"]

for fight in range(len(slayer)):
    s = random.choice(slayer)
    ur = random.choice(upper_rank)
    
    slayer.remove(s)
    upper_rank.remove(ur)
    
    print(f"{s} fights {ur}")
    print()