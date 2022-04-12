import random

game_on = True
trynumber = 4
random_game = random.randint(101,110)
def gameison(input_szam):
    global in_game
    global trynumber

    if input_szam == random_game:
        print("WIN")
        game_on = False
    elif input_szam > random_game:
        print("The random number is smaller")
        trynumber -=2
    elif input_szam < random_game:
        print("The random number is bigger")
        trynumber -=2	
while game_on:
    if trynumber > 0:
        input_num = input("what is the number(101-110):")
        if input_num.isnumeric():
            input_to_num = int(input_num)
            if input_to_num > 100 and input_to_num < 111:
                gameison(input_to_num)
            else:
                print("The number is not in the range!")
                trynumber -=2
        else:
            print("Give me the number!")
            trynumber -= 2
    else:
        print(f"LOSE {random_game}")
        game_on = False