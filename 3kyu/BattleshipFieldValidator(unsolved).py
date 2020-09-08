#https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

def validate_battlefield(field):
    current_ships = [0, 0, 0, 0]
    standard_ships = [4, 3, 2, 1]
    for row in range(10):
        for col in range(10):

            if field[row][col] == 1 :
                field[row][col] = 2 
                cnt = 0

                for check in range(1, 4):
                    if col+1 < 10 and field[row][col+1] == 1:
                        if col + check > 9 or field[row][col+check] != 1:
                            break
                        elif field[row][col+check] == 1:
                            field[row][col+check] = 2
                            cnt += 1
                            if field[row+1][col+check] == 1 :
                                return False
                    elif row+1 < 10 and field[row+1][col] == 1:
                        if row + check > 9 or field[row+check][col] != 1:
                            break
                        elif field[row+check][col] == 1:
                            field[row+check][col] = 2
                            cnt += 1
                            if field[row + check][col+1] == 1:
                                return False
                    else:
                current_ships [cnt] += 1
    if current_ships == standard_ships and (1 not in field):
        return True
    else:
        return False

battleField =      [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))