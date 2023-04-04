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
{"Pos":"0", "direction":"S", "item":"key"},{"Pos":"1", "direction":"E"},{"Pos":"2", "direction":"EWS"},{"Pos":"3", "direction":"EW"},{"Pos":"4", "direction":"EWS"},{"Pos":"5", "direction":"EW"},{"Pos":"6", "direction":"EWS"},{"Pos":"7", "direction":"WS"},
{"Pos":"8", "direction":"NES"},{"Pos":"9", "direction":"W"},{"Pos":"10", "direction":"NE"},{"Pos":"11", "direction":"WS"}, {"Pos":"12", "direction":"N"},{"Pos":"13", "direction":"ES"},{"Pos":"14", "direction":"NW"},{"Pos":"15", "direction":"N"},
{"Pos":"16", "direction":"NES"},{"Pos":"17", "direction":"EW"},{"Pos":"18", "direction":"EW"},{"Pos":"19", "direction":"NW"},{"Pos":"20", "direction":"ES"},{"Pos":"21", "direction":"NW"},{"Pos":"22", "direction":"S"},{"Pos":"23", "direction":"S"},
{"Pos":"24", "direction":"NE"},{"Pos":"25", "direction":"WS"},{"Pos":"26", "direction":"N"},{"Pos":"27", "direction":"S"},{"Pos":"28", "direction":"N", "item":"key_card"},{"Pos":"29", "direction":"ES"},{"Pos":"30", "direction":"NW"},{"Pos":"31", "direction":"NWS"},
{"Pos":"32", "direction":"NE"},{"Pos":"33", "direction":"NEW"},{"Pos":"34", "direction":"EWS"},{"Pos":"35", "direction":"NEW"},{"Pos":"36", "direction":"EWS"},{"Pos":"37", "direction":"NW"},{"Pos":"38", "direction":"ES"},{"Pos":"39","direction":"NW"},
{"Pos":"40", "direction":"NS"},{"Pos":"41", "direction":"S"},{"Pos":"42", "direction":"N"},{"Pos":"43", "direction":"S", "item":"crowbar"},{"Pos":"44", "direction":"NE"},{"Pos":"45", "direction":"WS"},{"Pos":"46", "direction":"NE"},{"Pos":"47", "direction":"WS"},
{"Pos":"48", "direction":"NE"},{"Pos":"49", "direction":"NW"},{"Pos":"50", "direction":"ES"},{"Pos":"51", "direction":"NEW"},{"Pos":"52", "direction":"WS"},{"Pos":"53", "direction":"N"},{"Pos":"54", "direction":"ES"},{"Pos":"55", "direction":"NW"},
{"Pos":"56", "direction":"E"},{"Pos":"57", "direction":"EW"},{"Pos":"58", "direction":"NW"},{"Pos":"59", "direction":"E"},{"Pos":"60", "direction":"NEW"},{"Pos":"61", "direction":"EW"},{"Pos":"62", "direction":"NEW"},{"Pos":"63", "direction":"W"}
]


WIDTH = 4

inventory = ['key']
##N = pos-WIDTH
##E = pos+1
##S = pos+WIDTH
##W = pos-1

#game start here
def main():
    """runs and calls to other defs to run game"""
    #starting blurb
    print("Welcome to" + logo +"You are stuck in a maze.")
    game = True
    pos = 8
    while game == True:
        direction = input("You can go {}\nWhich direction would you like to go?" .format(bmap[pos]["direction"])).upper()
        canmove(pos,direction)
        if canmove == True:
            move(pos,direction)
        else:
            direction = input("You can go {}\nWhich direction would you like to go?" .format(bmap[pos]["direction"])).upper()
        if ifitem == True:
            print(ending)
    
#movment
def canmove(pos,direction):
    """Checks to see which direction you can go using pos and then compares that direction you have cosen
        if you have chosen a direction that is listed it allows you to go in that direction otherwise you
        don't move and are told to choose a new direction"""
##    print(direction,pos,smap[pos]["direction"])
    if direction in bmap[pos]["direction"]:
        return True
    else:
        return False

def move(pos, direction):
    """takes pos and direction then works out new pos"""
    if canmove(pos, direction)== True:
        if direction == "N":
            pos = pos - WIDTH
        elif direction == "E":
            pos = pos + 1
        elif direction == "W":
            pos = pos - 1
        elif direction == "S":
            pos = pos + WIDTH
        else:
            print("not working")
        print(pos)


def item(pos):
    """check if you have an item in your inventory and pick up, use item when asked"""
    print(pos)
    if "item" in bmap[pos] and bmap[pos]["item"]:
        if "key" in bmap[pos]["item"] or "crowbar" in bmap[pos]["item"] or "key_card" in bmap[pos]["item"]:
            print("you have found the {}." .format(bmap[pos]["item"]))
            pick_up = input("Would you like to pick up the {}" .format(bmap[pos]["item"])).upper()
            if pick_up == "Y":
                inventory.append(bmap[pos]["item"])
                print(inventory)

def ifitem(pos):
    if 'key' in inventory and pos == 12:
        gameend = True
        print("Game Over")

##item check
##item pick up

##print(smap[pos])
##if move(direction) == smap(direction)
##use pos for same location:

direction = input("You can go {}\nWhich direction would you like to go?" .format(bmap[pos]["direction"])).upper()
canmove(pos,direction)
if canmove == True:
    move(pos, direction)
    pos = newpos
if canmove == False:
    print("False")
    print("You can go {}" .format(bmap[pos]["direction"]))
if pos == 12 and "key" in inventory:
    print(ending)
    game = False
