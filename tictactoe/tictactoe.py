import random

def game():
    print("\nTic ~ Tac ~ Toe Board")
    print ("", data["a"], "||", data["b"], "||", data["c"]) 
    print ("======================")
    print ("", data["d"], "||", data["e"], "||", data["f"])
    print ("======================")
    print ("", data["g"], "||", data["h"], "||", data["i"])

data = {"a":None, "b":None, "c":None, "d":None, "e":None, "f":None, "g":None, "h":None, "i":None}
count = 0

game()

print("\nType 'exit' to exit the game.\n" )

while True:
    random_key = random.choice(list(data.keys()))
    if random_key in data and data[random_key] == None:
        data[random_key] = "  X "
        count = count + 1
    else:
        continue
    game()
    if count == 9:
            quit()   

    while True:
        human_key = input ("\nSelect square: \n")
        if human_key == "exit":
            quit()
        if human_key in data and data[human_key] == None:
            data[human_key] = "  O "
            count = count +1
            game() 
            break
        else:
            print("\nPlease select an existing empty square!\n")    

