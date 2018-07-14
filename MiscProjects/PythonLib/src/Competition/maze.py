import random

def find(mat, elem):
    for row, i in enumerate(mat):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

def next_move(board):    
    possibleActions = []
    if board[0][1]!='#':
        possibleActions.append('UP')
    if board[2][1]!='#':
        possibleActions.append('DOWN')
    if board[1][0]!='#':
        possibleActions.append('LEFT')
    if board[1][2]!='#':
        possibleActions.append('RIGHT')
        
    ePos = find(board,'e')
    if ePos == -1:
        probe = random.random()
        if probe < 0.75:
            if "UP" in possibleActions:
                print "UP"
            elif "RIGHT" in possibleActions:
                print "RIGHT"
            elif "DOWN" in possibleActions:
                print "DOWN"
            else:
                print "LEFT"                
        else:
            print random.choice(possibleActions)
    else:
        y_diff = ePos[0] - 1
        x_diff = ePos[1] - 1
        if x_diff < 0:
            if "LEFT" in possibleActions:
                print "LEFT"
            else:
                if y_diff < 0:
                    if "UP" in possibleActions:
                        print "UP"
                    else:
                        print random.choice(possibleActions)
                else:
                    if "DOWN" in possibleActions:
                        print "DOWN"
                    else:
                        print random.choice(possibleActions)
        elif x_diff > 0:
            if "RIGHT" in possibleActions:
                print "RIGHT"
            else:
                if y_diff < 0:
                    if "UP" in possibleActions:
                        print "UP"
                    else:
                        print random.choice(possibleActions)
                else:
                    if "DOWN" in possibleActions:
                        print "DOWN"
                    else:
                        print random.choice(possibleActions)
        else:
            if y_diff < 0:
                print "UP"
            else:
                print "DOWN"
    return

if __name__ == "__main__":
    playerId = int(raw_input())
    board = [[j for j in raw_input().strip()] for i in range(3)]
    next_move(board)