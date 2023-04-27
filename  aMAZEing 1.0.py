################################################
####  aMAZEing -- Caleb Wormald -- 4/6/2023 ####
################################################

logo = ("""
 Welcome to
          __  __              ______  ______   _                    :::::::::::::::::::::::::::::::::::::::::::::::::::     
         |  \/  |     /\     |___  / |  ____| (_)                ™  ::     :                                         ::  N
   __ _  | \  / |    /  \       / /  | |__     _   _ __     __ _    ::     :......      ......     .......           ::  ∆
  / _` | | |\/| |   / /\ \     / /   |  __|   | | | '_ \   / _` |   ::           :           :     :           :     ::  |
 | (_| | | |  | |  / ____ \   / /__  | |____  | | | | | | | (_| |   ::           :           :     :           :  S  ::
  \__,_| |_|  |_| /_/    \_\ /_____| |______| |_| |_| |_|  \__, |   ::     ......:.....      :.....:     ......:.....::
                                                            __/ |   ::                       :           :     :     ::
 You are stuck in a maze.                                  |___/    ::                       :           :     :     ::
                                                                    ::     .......     ......:     ......:     :     ::
 To play this game you told "You can go" then the directions        ::           :     :     :     :                 ::
 you can go N=North, E=East, W=West and S=South.                    ::.....      :.....:     :.....:     .....       ::
 To go the direction just enter the first letter of the direction   ::                                   :           ::
 you wish to go.                                                    ::                                   :           ::
 So if you wanted to go North you could enter ethier N or n.        ::     .......     .......      .....:      .....::
 The Map is above use it how you want S is where you Start and      ::     :     :     :     :           :           ::
 F is where you Finish but don't forget to find the key!            ::     :     :     :     :           :           ::
                                                                    ::           :.....:     :.......    :......     ::
                                                                    ::           :                  :    :           ::
                                                                    ::...........:     ......       :....:      .....::
                                                                    ::                 :                             ::
                                                                    ::  F              :                             ::
                                                                    :::::::::::::::::::::::::::::::::::::::::::::::::::
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
{"pos":"24", "direction":"NE"},{"pos":"25", "direction":"WS"},{"pos":"26", "direction":"N"},{"pos":"27", "direction":"S"},{"pos":"28", "direction":"N", "item":"key card"},{"pos":"29", "direction":"ES"},{"pos":"30", "direction":"NEW"},{"pos":"31", "direction":"NWS"},
{"pos":"32", "direction":"NE"},{"pos":"33", "direction":"NEW"},{"pos":"34", "direction":"EWS"},{"pos":"35", "direction":"NEW"},{"pos":"36", "direction":"EWS"},{"pos":"37", "direction":"NW"},{"pos":"38", "direction":"ES"},{"pos":"39","direction":"NW"},
{"pos":"40", "direction":"NS"},{"pos":"41", "direction":"S"},{"pos":"42", "direction":"N"},{"pos":"43", "direction":"S", "item":"crowbar"},{"pos":"44", "direction":"NE"},{"pos":"45", "direction":"WS"},{"pos":"46", "direction":"NE"},{"pos":"47", "direction":"WS"},
{"pos":"48", "direction":"NE"},{"pos":"49", "direction":"NW"},{"pos":"50", "direction":"ES"},{"pos":"51", "direction":"NEW"},{"pos":"52", "direction":"WS"},{"pos":"53", "direction":"N"},{"pos":"54", "direction":"ES"},{"pos":"55", "direction":"NW"},
{"pos":"56", "direction":"E"},{"pos":"57", "direction":"EW"},{"pos":"58", "direction":"NW"},{"pos":"59", "direction":"E"},{"pos":"60", "direction":"NEW"},{"pos":"61", "direction":"EW"},{"pos":"62", "direction":"NEW"},{"pos":"63", "direction":"W"}
]

WIDTH = 8
inventory = ["key" , 'key']

#game start here
def start():
    """runs and calls to other defs to run game"""
    #starting blurb
    print(logo)
    game = True
    pos = 15
    while game == True:
        print(pos)
        print(inventory)
        print(game)
        direction = input("You can go {}. \nWhich direction would you like to go? ".format(bmap[pos]["direction"])).upper()
        if canmove(pos, direction):
            pos = move(pos, direction)
            item(pos)
            ifitem(inventory, pos)
        if game == False:
            print("Game Over. You escaped the maze!")
    
#movment checker
def canmove(pos, direction):
    """Checks to see which direction you can go using pos and then compares that direction you have chosen.
    If you have chosen a direction that is listed it allows you to go in that direction, otherwise you
    don't move and are told to choose a new direction."""
    if direction in bmap[pos]["direction"]:
        return True
    else:
        print("Choose a different direction.")
        return False

#movment
def move(pos, direction):
    """takes pos and direction then works out new pos"""
    global WIDTH
    if direction == "N":
        pos = pos - WIDTH
    elif direction == "E":
        pos = pos + 1
    elif direction == "W":
        pos = pos - 1
    elif direction == "S":
        pos = pos + WIDTH
    else:
        print("Please enter a direction")
    return pos

#is there an item in your square?
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

#item checker
def ifitem(inventory, pos):
    """checks if you have an item in your inventory and if you are at the final position to end the game"""
    global game
    if 'key' in inventory and pos == 7 or "key" in inventory and pos == 7 or ["key"] in inventory and pos == 7 or ['key'] in inventory and pos == 7:
        game = False
