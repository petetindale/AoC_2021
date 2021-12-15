import functools as fn

test_input = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n",
    "\n",
    "22 13 17 11  0\n",
    " 8  2 23  4 24\n",
    "21  9 14 16  7\n",
    " 6 10  3 18  5\n",
    " 1 12 20 15 19\n",
    "\n",
    " 3 15  0  2 22\n",
    " 9 18 13 17  5\n",
    "19  8  7 25 23\n",
    "20 11 10 24  4\n",
    "14 21 16 12  6\n",
    "\n",
    "14 21 17 24  4\n",
    "10 16 15  9 19\n",
    "18  8 23 26 20\n",
    "22 11 13  6  5\n",
    " 2  0 12  3  7\n"]

test_sum_result = 188
test_last_number = 24
test_total = 4512

#Build the Bingo Board
class BingoBoard:
    NOT_FOUND = 0
    FOUND = 1
    BINGO = 2
    ALREADY_COMPLETE = 3

    def __init__(self) :
        self.board_lines = list()
        self.found_number = list()
        self.found_x = list()
        self.found_y = list()
        self.complete = False
    def add_line(self, board_line):
        self.board_lines.append(list(map(int, filter(lambda x : x != '', list(map(str,board_line.strip().split(" ")))))))
    def __str__(self) -> str:
        return self.board_lines
    def find(self, drawn_number):
        if self.complete :
            return BingoBoard.ALREADY_COMPLETE
        y = 0
        y_len = len(self.board_lines)
        x = 0 
        x_len = len(self.board_lines[0])
        for board_line in self.board_lines :
            for board_number in board_line :
                if board_number == drawn_number :
                    #print(f"found {board_number} at x={x}, y={y}")
                    self.found_number.append(drawn_number)
                    self.found_x.append(x)
                    self.found_y.append(y)
                    if self.found_y.count(y) >= y_len:
                        self.complete = True
                        return BingoBoard.BINGO
                    if self.found_x.count(x) >= x_len :
                        self.complete = True
                        return BingoBoard.BINGO
                    return BingoBoard.FOUND
                x += 1 
            x = 0
            y += 1
        return BingoBoard.NOT_FOUND
    
    def sum_uncalled_numbers(self) :
        print(f"Winning Board : {self.board_lines}")
        sum_of_numbers = fn.reduce(lambda x,y: x + sum(y), self.board_lines, 0)
        sum_of_found_numbers = sum(self.found_number)
        return sum_of_numbers - sum_of_found_numbers


def play_squid_bingo(list_of_strings, win_game) :
    if len(list_of_strings) > 0 :
        drawn_numbers = list(map(int, list_of_strings[0].split(",")))
        list_of_bingo_boards = list()
        winning_boards_numbers = list()
        temp_bingo_board = None
        for x in list_of_strings :
            if x.find(",") == -1 :
                if x.strip() != "" :
                    if temp_bingo_board == None :
                        temp_bingo_board = BingoBoard()
                    temp_bingo_board.add_line(x)
                else :
                    if temp_bingo_board != None :
                        list_of_bingo_boards.append(temp_bingo_board)
                    temp_bingo_board = BingoBoard()
        if temp_bingo_board != None :
            list_of_bingo_boards.append(temp_bingo_board)
        for drawn_number in drawn_numbers :
            for bingo_board in list_of_bingo_boards :
                if bingo_board.find(drawn_number) == BingoBoard.BINGO :
                    print(f"Winning Last Draw {drawn_number}")
                    if win_game :
                        return(bingo_board.sum_uncalled_numbers() * drawn_number)
                    else :
                        winning_boards_numbers.append(bingo_board.sum_uncalled_numbers() * drawn_number)
    return winning_boards_numbers.pop()

def test_squid_bingo() :
    print(play_squid_bingo(test_input, False))

test_squid_bingo()