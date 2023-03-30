import os
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play? 'y' or 'n': ")
if play == 'y':
    clear = lambda: os.system('clear')
    clear()
else:
    exit()

print(logo)

def deal_card():
    randoTrader = random.randint(0, len(cards)-1)
    num = cards[randoTrader]
    cards.pop(randoTrader)
    return num

def calculate_score(arr):
    sums = sum(arr)
    if sums > 21:
        for index, num in enumerate(arr):
            if num == 11:
                arr.pop(index)
                arr.append(1)

    return sum(arr)


condi = True
trader = []
player = []
for i in range(0,2):
    numPlayer = deal_card()
    player.append(numPlayer)

scorePlayer = calculate_score(player)
print(f"Your card: {player}, current score is: {scorePlayer}")
trader.append(deal_card())
print(f"Computer card is {trader}")
# while condi == True:
