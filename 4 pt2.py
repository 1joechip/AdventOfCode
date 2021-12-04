inp = """puzzle input here"""
parts = inp.split()
nums = [num for num in parts[0].split(",")]
boards = [[parts[i-4:i+1] for i in range(j+5, j+30, 5)] for j in range(0, 2500, 25)]

def check_bingo(board):
    for row in board:
        if len(set(row)) <= 1: return True
    cols = list(zip(*board[::-1]))
    for column in cols:
        if len(set(column)) <= 1: return True

def update_board(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = "#"
    return board

def go(boards):
    total = 0
    solved = []
    for num in nums:
        boards = [update_board(board, num) for board in boards]
        for board in boards:
            if board not in solved and check_bingo(board):
                solved.append(board)
                total += 1
                if total == len(boards):
                    nontags = 0
                    for row in board:
                        for el in row:
                            if el != "#":
                                nontags += int(el)
                    return nontags*int(num)
print(go(boards))
            
            
    
        
    
    
