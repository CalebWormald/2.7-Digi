#################################
##  aMAZEing -- Caleb Wormald  ##
#################################

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

WIDTH = 4
pos = 8
##N = pos-WIDTH
##E = pos+1
##S = pos+WIDTH
##W = pos-1

#starting blurb
print("Welcome to" + logo +"You are stuck in a maze.")

#movment
def move(pos, dir):
    """takes pos and dir then works out new pos"""
    newpos = pos
    if dir == "N":
        newpos = pos - WIDTH
    elif dir == "E":
        newpos = pos + 1
    elif dir == "W":
        newpos = pos - 1
    elif dir == "S":
        newpos = pos + WIDTH
    else:
        print("not working")
    print(newpos)

def canmove(pos,dir):
    """Checks to see which dir you can go using pos and then compares that dir you have cosen
        if you have chosen a dir that is listed it allows you to go in that dir otherwise you
        don't move and are told to choose a new dir"""
    if move(dir) in smap:
        if move(dir) == smap[dir]:
            print("done")

##if move(dir) == smap(dir)
##use pos for same location


smap=[
{"pos":"0", "dir":"E"},{"pos":"1", "dir":"EWS"},{"pos":"2", "dir":"EW"},{"pos":"3", "dir":"WS"},
{"pos":"4", "dir":"S"},{"pos":"5", "dir":"NS"},{"pos":"6", "dir":"S"},{"pos":"7", "dir":"N"},
{"pos":"8", "dir":"ES"},{"pos":"9", "dir":"NW"},{"pos":"10", "dir":"NE"},{"pos":"11", "dir":"WS"},
{"pos":"12", "dir":"NE"},{"pos":"13", "dir":"EW"},{"pos":"14", "dir":"EW"},{"pos":"15", "dir":"NW"}
]


