import random
import keyboard
import time

def wait_for_key(key, success_message):
    """Wait for a specific key"""
    while True:
        if keyboard.is_pressed(key):
            print(success_message)
            time.sleep(0.5)
            break
        #time.sleep(1)
        #dungeon= ("Trap", "Ogre", "Chest", "Door", "Pit", "key")

def handle_trap_pit (game_state):
    print("Press Space to jump over the trap/pit \n Waiting for Space...")
    wait_for_key('space', "Jumped!\nSuccessfully jumped over it!")

def handle_chest(game_state):
    game_state["items"].append("chest")
    print(" You picked up a treasure chest! Now you can fight ogres!")
    wait_for_key('enter', "Treasure saved! Successfully added 10 clicks!")

def handle_key(game_state):
    game_state["items"].append("key")
    print(" You found a key!")

def handle_ogre(game_state):
    print("an ogre appeared in front of you!")
    if "chest" in game_state["items"]:
        print("You have a treasure chest, you can fight it!\nYou must press Enter 10 times to kill the ogre...")
        for hit in range(1, 11):
            input(f"Hit {hit}/10: Press Enter!")
            print(f" Hit {hit} landed!")
        print("You killed the ogre! Well done!")
        game_state["items"].remove("chest")
    else:
        print("You don't have a treasure chest! You can't fight...\n The ogre dealt 30 damage!")
        game_state["health"] -= 30
    time.sleep(1)

def handle_door(game_state):
    if "key" in game_state["items"]:
        print("You opened the door with the key!")
        game_state["items"].remove("key")
        jump= random.choice([1, 2, -1, -2])
        game_state["current_room"] += jump
        print(f"The door took you {abs(jump)} room(s) {'forward' if jump > 0 else 'backward'}")
        time.sleep(1)
        return "continue"
    
    else:
        print("The door is locked! You go back.")
        game_state["current_room"] -= 1
        time.slepp(1)
        return "continue"
    

def start_adventure():
    game = {
        "health": 100,
        "current_room": 1,
        "last_room": 5,
        "items": []
    }
    dungeon = ("Trap", "Ogre", "Chest", "Door", "Pit", "Key")

    scenario_map= {
        "Trap": handle_trap_pit,
        "Pit": handle_trap_pit,
        "Chest": handle_chest,
        "Ogre": handle_ogre,
        "Door": handle_door,
        "Key": handle_key

    }

    while game["health"] > 0 and game["current_room"]<= game["last_room"]:
        if game["current_room"] <1:
            game["current_room"] =1
        scenario= random.choice(dungeon)

        print(f"\n current room: {game['current_room']}")
        print(f"\n health: {game['health']}")
        print(f"items: {game['items']}")
        print(f"scenario: {scenario}")
        print("-" *20)
        time.sleep(1)

        result= scenario_map[scenario] (game)
        if result =="continue":
            continue

        game["current_room"] += 1
        time.sleep(1)

    if game["health"] <= 0:
        print("You died and game over!")
    else:
        print(f"\n You Won!")
        print(f"\n Health: {game['health']}, Items: {game['items']}")


if __name__ == "__main__":
    start_adventure()