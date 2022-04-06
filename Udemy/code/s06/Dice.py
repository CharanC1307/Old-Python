import random
keep_going = True
while keep_going:
    # 'Roll' five random dice
    dice = [0,0,0,0,0]
    for i in range(5): # "Roll"
        dice[i] = random.randint(1,6)
    print("You rolled:", dice)
    answer = input("Keep going?")
    keep_going = (answer == "")
        
