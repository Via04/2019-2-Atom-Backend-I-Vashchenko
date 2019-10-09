class Field:
    __curState = []

    def __init__(self):
        self.__curState = [[" "] * 3 for _ in range(3)]
        self.__winner = -1
        self.__isCross = True
        print("The classic game Tic Tac Toe. Player 1 goes with crosses and player 2 with zeroes\n")
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print("{}:{}|".format(i, j), end="")
                else:
                    print("{}:{}".format(i, j), end="")
                    print("\n-----------")

    def draw(self):
        for i in range(3):
            for j in range(3):
                if j != 2:
                    if self.__curState[i][j] == " ":
                        print("{}:{}|".format(i, j), end="")
                    else:
                        print(" {} |".format(self.__curState[i][j]), end="")
                else:
                    if self.__curState[i][j] == " ":
                        print("{}:{}".format(i, j), end="")
                        print("\n-----------")
                    else:
                        print(" {} ".format(self.__curState[i][j]), end="")
                        print("\n-----------")

    def __check_diagonal(self, sign):
        toright = True
        toleft = True
        for i in range(3):
            toright = toright and (self.__curState[i][i] == sign)
            toleft = toleft and (self.__curState[2-i][i] == sign)
        if (toright or toleft) and sign == "o":
            self.__winner = 2
            return True
        if (toright or toleft) and sign == "x":
            self.__winner = 1
            return True
        return False

    def __check_lines(self, sign):
        for i in range(3):
            cols = True
            rows = True
            for j in range(3):
                cols = cols and (self.__curState[j][i] == sign)
                rows = rows and (self.__curState[i][j] == sign)
            if (cols or rows) and sign == "o":
                self.__winner = 2
                return True
            if (cols or rows) and sign == "x":
                self.__winner = 1
                return True
        return False

    def is_end(self):
        if self.__check_diagonal("o") or self.__check_diagonal("x") or \
                self.__check_lines("o") or self.__check_lines("x"):
            return True

    def show_winner(self):
        print("Player {} won the game!".format(self.__winner))
        return self.__winner

    def make_turn(self, i, j):
        if self.__isCross:
            if self.__curState != "x" or self.__curState != "o":
                self.__curState[i][j] = "x"
                self.__isCross = False
            else:
                print("There is something already in this cell. Make your turn again")
        else:
            if self.__curState != "x" or self.__curState != "o":
                self.__curState[i][j] = "o"
                self.__isCross = True
            else:
                print("There is something already in this cell. Make your turn again")


game = Field()
print("\nInput coordinates using \":\" separator")
try:
    while not game.is_end():
        nexti, nextj = map(int, input().split(":"))
        game.make_turn(nexti, nextj)
        game.draw()
    game.show_winner()

except (TypeError, ValueError):
    print("Incorrect data type. Expected number of cell for next turn")
except IndexError:
    print("There no such coordinates. Error")
except KeyboardInterrupt:
    print("The game was closed")
