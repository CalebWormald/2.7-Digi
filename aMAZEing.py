#####################################
####  aMAZEing -- Caleb Wormald  ####
#####################################

logo = ("""
          __  __              ______  ______   _                 
         |  \/  |     /\     |___  / |  ____| (_)                ™
   __ _  | \  / |    /  \       / /  | |__     _   _ __     __ _ 
  / _` | | |\/| |   / /\ \     / /   |  __|   | | | '_ \   / _` |
 | (_| | | |  | |  / ____ \   / /__  | |____  | | | | | | | (_| |
  \__,_| |_|  |_| /_/    \_\ /_____| |______| |_| |_| |_|  \__, |
                                                            __/ |
                                                           |___/ 
""")
ending = ("""
 __     ______  _    _  __          ______  _   _
 \ \   / / __ \| |  | | \ \        / / __ \| \ | | 
  \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` |
    | | | |__| | |__| |    \  /\  / | |__| | |\  |
    |_|  \____/ \____/      \/  \/   \____/|_| \_|                                                       
""")
bmap=[
{"pos":"0", "direction":"S", "item":"key"},{"pos":"1", "direction":"E"},{"pos":"2", "direction":"EWS"},{"pos":"3", "direction":"EW"},{"pos":"4", "direction":"EWS"},{"pos":"5", "direction":"EW"},{"pos":"6", "direction":"EWS"},{"pos":"7", "direction":"WS"},
{"pos":"8", "direction":"NES"},{"pos":"9", "direction":"W"},{"pos":"10", "direction":"NE"},{"pos":"11", "direction":"WS"}, {"pos":"12", "direction":"N"},{"pos":"13", "direction":"ES"},{"pos":"14", "direction":"NW"},{"pos":"15", "direction":"N"},
{"pos":"16", "direction":"NES"},{"pos":"17", "direction":"EW"},{"pos":"18", "direction":"EWS"},{"pos":"19", "direction":"NW"},{"pos":"20", "direction":"ES"},{"pos":"21", "direction":"NW"},{"pos":"22", "direction":"S"},{"pos":"23", "direction":"S"},
{"pos":"24", "direction":"NE"},{"pos":"25", "direction":"WS"},{"pos":"26", "direction":"N"},{"pos":"27", "direction":"S"},{"pos":"28", "direction":"N"},{"pos":"29", "direction":"ES"},{"pos":"30", "direction":"NEW"},{"pos":"31", "direction":"NWS"},
{"pos":"32", "direction":"NE"},{"pos":"33", "direction":"NEW"},{"pos":"34", "direction":"EWS"},{"pos":"35", "direction":"NEW"},{"pos":"36", "direction":"EWS"},{"pos":"37", "direction":"NW"},{"pos":"38", "direction":"ES"},{"pos":"39","direction":"NW"},
{"pos":"40", "direction":"NS"},{"pos":"41", "direction":"S"},{"pos":"42", "direction":"N"},{"pos":"43", "direction":"S", "item":"crowbar"},{"pos":"44", "direction":"NE"},{"pos":"45", "direction":"WS"},{"pos":"46", "direction":"NE"},{"pos":"47", "direction":"WS"},
{"pos":"48", "direction":"NE"},{"pos":"49", "direction":"NW"},{"pos":"50", "direction":"ES"},{"pos":"51", "direction":"NEW"},{"pos":"52", "direction":"WS"},{"pos":"53", "direction":"N"},{"pos":"54", "direction":"ES"},{"pos":"55", "direction":"NW"},
{"pos":"56", "direction":"E"},{"pos":"57", "direction":"EW"},{"pos":"58", "direction":"NW"},{"pos":"59", "direction":"E"},{"pos":"60", "direction":"NEW"},{"pos":"61", "direction":"EW"},{"pos":"62", "direction":"NEW"},{"pos":"63", "direction":"W"}
]

WIDTH = 8
inventory = []
##N = pos-WIDTH
##E = pos+1
##S = pos+WIDTH
##W = pos-1


#game start here
def main():
    """runs and calls to other defs to run game"""
    #starting blurb
    print("Welcome to " + logo + "You are stuck in a maze.")
    game = True
    pos = 15
    while game:
        direction = input("You can go {}. \nWhich direction would you like to go? ".format(bmap[pos]["direction"])).upper()
        if canmove(pos, direction):
            pos = move(pos, direction)
            item(pos)
            ifitem(pos)
        else:
            print("Choose a different direction.")
            
    
#movment
def canmove(pos, direction):
    """Checks to see which direction you can go using pos and then compares that direction you have chosen.
    If you have chosen a direction that is listed it allows you to go in that direction, otherwise you
    don't move and are told to choose a new direction."""
    if direction in bmap[pos]["direction"]:
        return True
    else:
        print("You cannot go that direction.")
        return False

def move(pos, direction):
    """takes pos and direction then works out new pos"""
    global WIDTH
    if direction == "N" or direction == "n":
        pos = pos - WIDTH
    elif direction == "E" or direction == "e":
        pos = pos + 1
    elif direction == "W" or direction == "w":
        pos = pos - 1
    elif direction == "S" or direction == "s":
        pos = pos + WIDTH
    else:
        print("not working")
    return pos

def item(pos):
    """check if you have an item in your inventory and pick up, use item when asked"""
    global inventory
    if "item" in bmap[pos] and bmap[pos]["item"]:
        if "key" in bmap[pos]["item"] or "crowbar" in bmap[pos]["item"] or "key_card" in bmap[pos]["item"]:
            print("You have found the {}.".format(bmap[pos]["item"]))
            pick_up = input("Would you like to pick up the {}? ".format(bmap[pos]["item"])).upper()
            if pick_up == "Y":
                inventory.append(bmap[pos]["item"])
                print(inventory)

def ifitem(pos):
    """checks if you have an item in your inventory and if you are at the final position to end the game"""
    global inventory
    global game
    if 'key' in inventory and pos == 12:
        game = False
        print("Game Over. You escaped the maze!")
