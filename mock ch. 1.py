from intro import get_player_name

def scene_one(name):
    print(f"Welcome to the forest, {name}!")

def scene_two(name):
    print(f"It's getting dark, {name}. We should leave.")

if __name__ == "__main__":
    # 1. Ask ONCE at the start
    player_name = get_player_name() 
    
    # 2. Pass that name into any scene that needs it
    scene_one(player_name)
    scene_two(player_name)