'''
Created on Jun 4, 2014

@author: Anirudh
'''
#!/bin/python
TOTAL_AMT = 100
POS = 11

def calculate_bid(player,pos,first_moves,second_moves):
    """your logic here"""
    firstAmt = 100
    secondAmt = 100
    tieCount=0
    for i in range(len(first_moves)):
        if first_moves[i] < second_moves[i]:
            secondAmt = secondAmt -  second_moves[i]
        elif first_moves[i] > second_moves[i]:
            firstAmt = firstAmt - first_moves[i]
        else:
            if tieCount%2==0:
                firstAmt = firstAmt - first_moves[i]
            else:
                secondAmt = secondAmt -  second_moves[i]
            tieCount = tieCount + 1
    
    print firstAmt
    print secondAmt
    print pos
    
    return 5
#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
