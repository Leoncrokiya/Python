from random import random
import random 

hashira = ["Giyu", "Shinobu", "Kyojuro", "Tengen", "Muichiro", "Mitsuri", "Sanemi", "Obanai", "Gyomei"]

upper_rank = ["Akaza", "Daki", "Gyutaro", "Doma", "Gyokko", "Hantengu", "Nakime", "Kokushibo", "Kaigaku"]

for fight in range(len(hashira)):
    h = random.choice(hashira)
    ur = random.choice(upper_rank)
    
    hashira.remove(h)
    upper_rank.remove(ur)
    
    print(f"{h} fights {ur}")
    print()