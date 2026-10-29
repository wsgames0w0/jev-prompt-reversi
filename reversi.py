import random
from typesafe_sdk import Choice, TypeSafeClient

JEV_MODEL = "jev-1.14.0"

BLACK =  1
WHITE = -1
EMPTY =  0
WALL  =  2
BOARD_SIZE = 8
MAX_TURNS = 60

DXY = (
    (-1, -1), ( 0, -1), ( 1, -1),
    (-1,  0),           ( 1,  0),
    (-1,  1), ( 0,  1), ( 1,  1)
)

X_STR = ("A", "B", "C", "D", "E", "F", "G", "H")
Y_STR = ("1", "2", "3", "4", "5", "6", "7", "8")

BOARD_STR = [[x + y for x in X_STR] for y in Y_STR]

class Board:
    def __init__(self):
        self.init()

    def init(self):
        self.board = [[EMPTY for x in range(BOARD_SIZE + 2)] for y in range(BOARD_SIZE + 2)]

        for y in range(BOARD_SIZE + 2):
            self.board[y][0] = WALL
            self.board[y][BOARD_SIZE + 1] = WALL

        for x in range(BOARD_SIZE + 2):
            self.board[0][x] = WALL
            self.board[BOARD_SIZE + 1][x] = WALL

        self.board[4][5] = BLACK
        self.board[5][4] = BLACK
        self.board[4][4] = WHITE
        self.board[5][5] = WHITE

        self.current_color = BLACK
        self.turn = 0
        self.history = ""

        self.reversed_pos = [] # 直前に置いた石と裏返した石を保存

    def show(self):
        print("   A B C D E F G H")
        print("------------------")

        for y in range(1, BOARD_SIZE + 1):
            print(f"{y}|", end = "")

            for x in range(1, BOARD_SIZE + 1):
                if self.board[y][x] == BLACK:
                    print("●", end = "")
                
                elif self.board[y][x] == WHITE:
                    print("○", end = "")
                
                else:
                    print("□", end = "")
            
            print()

        movable_pos = self.check_movable_pos(self.current_color)
        movable_pos_str = [BOARD_STR[y - 1][x - 1] for x, y in movable_pos]
        print(f"Next Moves: {movable_pos_str}")

    def check_movable_dir(self, x, y, color):
        direction = []

        if self.board[y][x] != EMPTY:
            return direction

        for (dx, dy) in DXY:
            s = x + dx
            t = y + dy

            if self.board[t][s] == -color:
                s += dx
                t += dy

                while self.board[t][s] == -color:
                    s += dx
                    t += dy

                if self.board[t][s] == color:
                    direction.append((dx, dy))

        return direction

    def check_movable_pos(self, color):
        movable_pos = []

        for y in range(1, BOARD_SIZE + 1):
            for x in range(1, BOARD_SIZE + 1):
                direction = self.check_movable_dir(x, y, color)

                if len(direction) > 0:
                    movable_pos.append((x, y))

        return movable_pos

    def is_done(self):
        if len(self.check_movable_pos(BLACK)) > 0:
            return False

        if len(self.check_movable_pos(WHITE)) > 0:
            return False
        
        return True

    def copy(self):
        board_copy = Board()

        for y in range(1, BOARD_SIZE + 1):
            for x in range(1, BOARD_SIZE + 1):
                board_copy.board[y][x] = self.board[y][x]
        
        board_copy.current_color = self.current_color
        board_copy.turn = self.turn
        board_copy.history = self.history

        board_copy.reversed_pos = self.reversed_pos.copy()

        return board_copy

    def move(self, x, y):
        board_copy = self.copy()

        board_copy.reversed_pos.clear()

        color = self.current_color

        direction = self.check_movable_dir(x, y, self.current_color)
        
        board_copy.board[y][x] = color
        board_copy.reversed_pos.append((x, y))

        for (dx, dy) in direction:
            s = x + dx
            t = y + dy

            while board_copy.board[t][s] == -color:
                board_copy.board[t][s] = color
                board_copy.reversed_pos.append((s, t))
                s += dx
                t += dy
        
        board_copy.current_color = -color
        board_copy.turn += 1
        board_copy.history += BOARD_STR[y - 1][x - 1]

        return board_copy

    def skip(self):
        board_copy = self.copy()

        board_copy.reversed_pos.clear()

        board_copy.current_color = -self.current_color

        return board_copy

    def count(self, color):
        total = 0

        for y in range(1, BOARD_SIZE + 1):
            for x in range(1, BOARD_SIZE + 1):
                if self.board[y][x] == color:
                    total += 1

        return total

    def count_liberty(self):
        total = 0

        for x, y in self.reversed_pos:
            for dx, dy in DXY:
                if self.board[y + dy][x + dx] == EMPTY:
                    total += 1

        return total

    def count_stable(self, color):
        corner = {
            "A1" : (( 1, 0), ( 0,  1)),
            "A8" : (( 1, 0), ( 0, -1)),
            "H1" : ((-1, 0), ( 0,  1)),
            "H8" : ((-1, 0), ( 0, -1))
        }

        total = 0
        checked = []

        for key in corner.keys():
            x, y = self.str_to_point(key)

            if self.board[y][x] == color:
                if not (x, y) in checked:
                    total += 1
                    checked.append((x, y))

                for dx, dy in corner[key]:
                    s = x + dx
                    t = y + dy

                    while self.board[t][s] == color:
                        if not (t, s) in checked:
                            total += 1
                            checked.append((s, t))
                        
                        s += dx
                        t += dy

        return total

    def count_c(self, color):
        corner_c = { # C_POINT : [CORNER_POINT, (ANOTHER_DXY), END_POINT]
            "A2" : ("A1", ( 0,  1), "A6"),
            "B1" : ("A1", ( 1,  0), "F1"),
            "A7" : ("A8", ( 0, -1), "A3"),
            "B8" : ("A8", ( 1,  0), "F8"),
            "G1" : ("H1", (-1,  0), "C1"),
            "H2" : ("H1", ( 0,  1), "H6"),
            "G8" : ("H8", (-1,  0), "C8"),
            "H7" : ("H8", ( 0, -1), "H3")
        }

        total = 0

        for key in corner_c.keys():
            x, y = self.str_to_point(key)

            if self.board[y][x] == color:
                pos, (dx, dy), pos_end = corner_c[key]
                s, t = self.str_to_point(pos)

                if self.board[t][s] == EMPTY:
                    px, py = x + dx, y + dy
                    ex, ey = self.str_to_point(pos_end)

                    for _ in range(3):
                        if self.board[py][px] != color:
                            break

                        px += dx
                        py += dy

                    if (px != ex or py != ey) or self.board[py][px] != color:
                        total += 1

        return total

    def count_x(self, color):
        corner_x = {
            "B2" : "A1",
            "B7" : "A8",
            "G2" : "H1",
            "G7" : "H8"
        }

        total = 0

        for key in corner_x.keys():
            x, y = self.str_to_point(key)

            if self.board[y][x] == color:
                s, t = self.str_to_point(corner_x[key])

                if self.board[t][s] != color:
                    total += 1

        return total

    def get_state_jev(self):
        state_jev = {}

        movable_pos = self.check_movable_pos(self.current_color)
        
        movable_pos_str = []

        for (x, y) in movable_pos:
            movable_pos_str.append(BOARD_STR[y - 1][x - 1])

        state_jev["MOVABLE_POS"] = movable_pos_str

        state_jev["INFO"] = {}

        for pos in movable_pos_str:
            new_board = self.move(*self.str_to_point(pos))

            state_jev["INFO"][pos] = {
                "X": new_board.count_x(self.current_color),
                "C": new_board.count_c(self.current_color),
                "STABLE": new_board.count_stable(self.current_color),
                "LIBERTY": new_board.count_liberty(),
                "MOVABLE": len(new_board.check_movable_pos(new_board.current_color)),
            }

        return state_jev

    def str_to_point(self, coord):
        return ord(coord[0]) - ord("A") + 1, ord(coord[1]) - ord("1") + 1

class BasePlayer:
    def __init__(self):
        self.name = "BasePlayer"

    def move(self, board : Board):
        raise NotImplementedError()

class RandomPlayer(BasePlayer):
    def __init__(self):
        super().__init__()

        self.name = "RandomPlayer"

    def move(self, board : Board):
        movable_pos = board.check_movable_pos(board.current_color)

        x, y = random.choice(movable_pos)

        return x, y

class MonteCarloPlayer(BasePlayer):
    def __init__(self):
        super().__init__()

        self.name = "MonteCarloPlayer"

        self.simulation_num = 50

    def move(self, board : Board):
        movable_pos = board.check_movable_pos(board.current_color)

        if len(movable_pos) == 1:
            return movable_pos[0]

        best_score = -float("inf")
        best_move = movable_pos[0]

        for x, y in movable_pos:
            score = 0

            for _ in range(self.simulation_num):
                score += -self.playout(board.move(x, y))

            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move

    def playout(self, board : Board):
        if board.is_done():
            black = board.count(BLACK)
            white = board.count(WHITE)

            if black > white:
                return 1

            elif white > black:
                return - 1

            else:
                return 0

        movable_pos = board.check_movable_pos(board.current_color)

        if len(movable_pos) == 0:
            return -self.playout(board.skip())

        else:
            return -self.playout(board.move(*random.choice(movable_pos)))

class JevPlayer(BasePlayer):
    def __init__(self):
        super().__init__()

        self.name = "JevPlayer"

    def move(self, board : Board):
        movable_pos = board.check_movable_pos(board.current_color)

        if len(movable_pos) == 1:
            return movable_pos[0]

        state = board.get_state_jev()

        state["POLICY"] = "\
次の処理を順に行い、候補を選択する。\
なお、数値を比較せずに候補を選択しないこと。\
(1)`INFO`内の全候補を対象とする。\
(2)その候補の内、Xの値が最小の候補だけを残す。\
(3)その候補の内、Cの値が最小の候補だけを残す。\
(4)その候補の内、STABLEの値が最大の候補だけを残す。\
(5)その候補の内、LIBERTYの値が最小の候補だけを残す。\
(6)その候補の内、MOVABLEの値が最小の候補だけを残す。\
(7)最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。\
"

        questions = {
            "best_move" : Choice(
                instructions = "\
`POLICY`に従って、選択肢`MOVABLE_POS`から1つの要素を選択してください。\
",
                criteria = {
                    move : move for move in state["MOVABLE_POS"]
                },
            ),
        }

        try:
            with TypeSafeClient() as client:
                response = client.system_one(
                    model = JEV_MODEL,
                    state = state,
                    questions = questions,
                )

            best_move_answer = response.choices["best_move"]
            best_move = best_move_answer.choice

            # print(f"次の手: {best_move}")
            # print(f"確信度: {best_move_answer.confidence}")

            return board.str_to_point(best_move)
        
        except Exception as e:
            print(e)
            raise

class JevClonePlayer(BasePlayer):
    def __init__(self):
        super().__init__()

        self.name = "JevClonePlayer"

    def move(self, board : Board):
        movable_pos = board.check_movable_pos(board.current_color)
        
        if len(movable_pos) == 1:
            return movable_pos[0]
        
        state = board.get_state_jev()

        # INFO内の全候補を対象とする。
        state_info = state["INFO"]

        # その候補の内、Xの値が最小の候補だけを残す。
        min_x = min(d["X"] for d in state_info.values())
        state_info = {k : d for k, d in state_info.items() if d["X"] == min_x}

        if len(state_info) == 1:
            return board.str_to_point(list(state_info.keys())[0])

        # その候補の内、Cの値が最小の候補だけを残す。
        min_c = min(d["C"] for d in state_info.values())
        state_info = {k : d for k, d in state_info.items() if d["C"] == min_c}

        if len(state_info) == 1:
            return board.str_to_point(list(state_info.keys())[0])

        # その候補の内、STABLEの値が最大の候補だけを残す。
        max_stable = max(d["STABLE"] for d in state_info.values())
        state_info = {k : d for k, d in state_info.items() if d["STABLE"] == max_stable}
        
        if len(state_info) == 1:
            return board.str_to_point(list(state_info.keys())[0])

        # その候補の内、LIBERTYの値が最小の候補だけを残す。
        min_liberty = min(d["LIBERTY"] for d in state_info.values())
        state_info = {k : d for k, d in state_info.items() if d["LIBERTY"] == min_liberty}

        if len(state_info) == 1:
            return board.str_to_point(list(state_info.keys())[0])

        # その候補の内、MOVABLEの値が最小の候補だけを残す。
        min_movable = min(d["MOVABLE"] for d in state_info.values())
        state_info = {k : d for k, d in state_info.items() if d["MOVABLE"] == min_movable}
        
        if len(state_info) == 1:
            return board.str_to_point(list(state_info.keys())[0])

        # 最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。
        return board.str_to_point(random.choice(list(state_info.keys())))

if __name__ == "__main__":
    import sys
    # import time

    players = {
        "Random" : RandomPlayer(),
        "MC" : MonteCarloPlayer(),
        "Jev" : JevPlayer(),
        "JevClone" : JevClonePlayer()
    }

    GAMES = 50

    player : dict[int, BasePlayer] = {BLACK : players[sys.argv[1]], WHITE : players[sys.argv[2]]}
    wins = {BLACK : 0, WHITE : 0}

    print(f"BLACK : {player[BLACK].name}, WHITE : {player[WHITE].name}")

    output = open("reversi_history.txt", "a", encoding = "utf-8")

    for i in range(GAMES):
        print(f"\rGame: {i + 1}/{GAMES}", end = "")
        output.write(f"{player[BLACK].name},{player[WHITE].name},")

        board = Board()
        
        while not board.is_done():
            movable_pos = board.check_movable_pos(board.current_color)

            if len(movable_pos) == 0:
                board = board.skip()
                
                continue

            # print(f"\rTurn: {board.turn}/{MAX_TURNS}", end = "")

            # time.sleep(0.5)

            x, y = player[board.current_color].move(board)

            board = board.move(x, y)

        # print()

        # board.show()

        black, white = board.count(BLACK), board.count(WHITE)

        # print(f"Black = {black}, WHITE = {white}")
        output.write(f"{black},{white},")

        if black > white:
            # print(f"{player[BLACK].name} Win")
            wins[BLACK] += 1

        elif black < white:
            # print(f"{player[WHITE].name} Win")
            wins[WHITE] += 1

        # else:
        #     print("Draw")

        # print("--")
        output.write(f"{board.history}\n")

    print(f"\n{player[BLACK].name} : ", end = "")
    print(f"Wins = {wins[BLACK]}, ", end = "")
    print(f"{player[WHITE].name} : ", end = "")
    print(f"Wins = {wins[WHITE]}")

    output.close()
