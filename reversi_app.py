from reversi import *
from tkinter import messagebox
import tkinter as tk
import threading
import queue

class ReversiGUI:
    CELL_SIZE = 64
    MARGIN = 32
    BOARD_PIXELS = CELL_SIZE * BOARD_SIZE

    def __init__(self, root):
        self.root = root
        self.root.title("リバーシ")

        self.board = Board()
        self.human_color = BLACK
        self.ai_type = "RandomPlayer"

        self.ai_thinking = False
        self.game_over = False
        self.result_queue = queue.Queue()

        # メニューバー
        self._create_menu()

        # 盤面
        canvas_size = self.BOARD_PIXELS + self.MARGIN * 2
        self.canvas = tk.Canvas(
            root,
            width = canvas_size,
            height = canvas_size,
            bg = "#176b3a",
            highlightthickness = 0
        )
        self.canvas.pack(padx = 10, pady = 10)
        self.canvas.bind("<Button-1>", self.on_click)

        # 状態表示
        self.status_label = tk.Label(
            root, text = "", font=("Meiryo", 12)
        )
        self.status_label.pack(pady = (0, 4))

        self.score_label = tk.Label(
            root, text = "", font = ("Meiryo", 11)
        )
        self.score_label.pack(pady = (0, 10))

        self.draw_board()
        self.process_turn()

        # AIの計算結果を定期的に確認
        self.root.after(50, self.check_ai_result)

    def _create_menu(self):
        menubar = tk.Menu(self.root)

        # 対局メニュー
        game_menu = tk.Menu(menubar, tearoff = False)
        game_menu.add_command(
            label = "新しい対局",
            command = self.reset_game
        )
        game_menu.add_separator()
        game_menu.add_command(
            label = "終了",
            command = self.root.destroy
        )
        menubar.add_cascade(label = "対局", menu = game_menu)

        # プレイヤー設定
        player_menu = tk.Menu(menubar, tearoff = False)
        self.color_var = tk.StringVar(value = "黒")
        player_menu.add_radiobutton(
            label = "人間が黒番",
            variable = self.color_var,
            value = "黒",
            command = self.change_settings
        )
        player_menu.add_radiobutton(
            label = "人間が白番",
            variable = self.color_var,
            value = "白",
            command = self.change_settings
        )
        menubar.add_cascade(
            label = "プレイヤー", menu = player_menu
        )

        # AI設定
        ai_menu = tk.Menu(menubar, tearoff = False)
        self.ai_var = tk.StringVar(value = "Random")

        ai_menu.add_radiobutton(
            label = "Random",
            variable = self.ai_var,
            value = "Random",
            command = self.change_settings
        )
        ai_menu.add_radiobutton(
            label = "MonteCarlo",
            variable = self.ai_var,
            value = "MonteCarlo",
            command = self.change_settings
        )
        ai_menu.add_radiobutton(
            label = "Jev",
            variable = self.ai_var,
            value = "Jev",
            command = self.change_settings
        )
        ai_menu.add_radiobutton(
            label = "JevClone",
            variable = self.ai_var,
            value = "JevClone",
            command = self.change_settings
        )
        menubar.add_cascade(label = "AI", menu = ai_menu)

        self.root.config(menu = menubar)

    def change_settings(self):
        self.human_color = (
            BLACK if self.color_var.get() == "黒" else WHITE
        )

        self.ai_type = {
            "Random" : "RandomPlayer",
            "MonteCarlo" : "MonteCarloPlayer",
            "Jev" : "JevPlayer",
            "JevClone" : "JevClonePlayer"
        }[self.ai_var.get()]

        # 設定を変更したら新しい対局を開始
        self.reset_game()

    def reset_game(self):
        self.board = Board()
        self.ai_thinking = False
        self.game_over = False

        # 古いAIの計算結果を破棄
        while not self.result_queue.empty():
            try:
                self.result_queue.get_nowait()
            
            except queue.Empty:
                break

        self.draw_board()
        self.process_turn()

    def draw_board(self):
        self.canvas.delete("all")

        m = self.MARGIN
        cell = self.CELL_SIZE

        # 盤面の背景
        self.canvas.create_rectangle(
            m,
            m,
            m + self.BOARD_PIXELS,
            m + self.BOARD_PIXELS,
            fill = "#218c4b",
            outline = "#103d25",
            width = 2
        )

        # マス目
        for i in range(BOARD_SIZE + 1):
            p = m + i * cell
            self.canvas.create_line(
                m, p, m + self.BOARD_PIXELS, p, fill = "#103d25"
            )
            self.canvas.create_line(
                p, m, p, m + self.BOARD_PIXELS, fill = "#103d25"
            )

        # 座標ラベル
        for i, label in enumerate(X_STR):
            x = m + i * cell + cell / 2
            self.canvas.create_text(
                x, m / 2, text = label, fill = "white", font = ("Arial", 11)
            )

        for i, label in enumerate(Y_STR):
            y = m + i * cell + cell / 2
            self.canvas.create_text(
                m / 2, y, text = label, fill = "white", font = ("Arial", 11)
            )

        # 合法手を小さな点で表示
        if not self.game_over and not self.ai_thinking:
            movable = self.board.check_movable_pos(
                self.board.current_color
            )

            is_human_turn = (
                self.board.current_color == self.human_color
            )

            if is_human_turn:
                for x, y in movable:
                    cx = m + (x - 0.5) * cell
                    cy = m + (y - 0.5) * cell
                    r = 4
                    self.canvas.create_oval(
                        cx - r, cy - r, cx + r, cy + r, fill = "#b9e8c8", outline = ""
                    )

        # 石を描画
        for y in range(1, BOARD_SIZE + 1):
            for x in range(1, BOARD_SIZE + 1):
                color = self.board.board[y][x]

                if color == EMPTY:
                    continue

                cx = m + (x - 0.5) * cell
                cy = m + (y - 0.5) * cell
                r = cell * 0.40

                fill = "black" if color == BLACK else "white"
                outline = "#333333" if color == BLACK else "#aaaaaa"

                self.canvas.create_oval(
                    cx - r, cy - r, cx + r, cy + r, fill = fill, outline = outline, width = 2
                )

        # 手番と石数
        current = "黒" if self.board.current_color == BLACK else "白"
        black_count = self.board.count(BLACK)
        white_count = self.board.count(WHITE)

        if self.game_over:
            self.status_label.config(text = "対局終了")

        elif self.ai_thinking:
            self.status_label.config(text = "AIが思考中です...")

        elif self.board.current_color == self.human_color:
            self.status_label.config(text = f"あなたの番（{current}）")

        else:
            self.status_label.config(text = f"AIの番（{current}）")

        self.score_label.config(
            text = f"黒：{black_count}, 白：{white_count}"
        )

    def on_click(self, event):
        if self.game_over or self.ai_thinking:
            return

        # 人間の手番以外はクリックできない
        if self.board.current_color != self.human_color:
            return

        # クリック座標を盤面座標に変換
        x = int((event.x - self.MARGIN) // self.CELL_SIZE) + 1
        y = int((event.y - self.MARGIN) // self.CELL_SIZE) + 1

        if not (1 <= x <= BOARD_SIZE and 1 <= y <= BOARD_SIZE):
            return

        # 合法手でなければ何もしない
        movable = self.board.check_movable_pos(
            self.board.current_color
        )

        if (x, y) not in movable:
            return

        self.board = self.board.move(x, y)
        self.process_turn()

    def process_turn(self):
        if self.board.is_done():
            self.finish_game()
            return

        movable = self.board.check_movable_pos(
            self.board.current_color
        )

        # 合法手がない場合はパス
        if not movable:
            skipped_color = self.board.current_color
            self.board = self.board.skip()

            name = "黒" if skipped_color == BLACK else "白"
            self.status_label.config(text = f"{name}はパスです")
            self.draw_board()

            # パス後の手番を続けて判定
            self.root.after(500, self.process_turn)
            return

        # AIの手番
        if self.board.current_color != self.human_color:
            self.start_ai()

        else:
            self.draw_board()

    def start_ai(self):
        self.ai_thinking = True
        self.draw_board()

        # スレッド内では盤面のコピーを使う
        board_snapshot = self.board.copy()
        player_type = self.ai_type

        def worker():
            try:
                players = {
                    "RandomPlayer" : RandomPlayer(),
                    "MonteCarloPlayer" : MonteCarloPlayer(),
                    "JevPlayer" : JevPlayer(),
                    "JevClonePlayer" : JevClonePlayer()
                }

                player = players[player_type]

                result = player.move(board_snapshot)
                self.result_queue.put(("move", result))

            except Exception as exc:
                self.result_queue.put(("error", str(exc)))

        threading.Thread(
            target = worker,
            daemon = True
        ).start()

    def check_ai_result(self):
        try:
            result_type, result = self.result_queue.get_nowait()

        except queue.Empty:
            self.root.after(50, self.check_ai_result)
            return

        self.ai_thinking = False

        if result_type == "error":
            messagebox.showerror(
                "AIエラー", f"AIの計算中にエラーが発生しました。\n{result}"
            )
            self.draw_board()

        else:
            x, y = result

            # 計算中に対局がリセットされた場合などを考慮
            if not self.game_over:
                movable = self.board.check_movable_pos(
                    self.board.current_color
                )

                if (x, y) in movable:
                    self.board = self.board.move(x, y)

                self.draw_board()
                self.process_turn()

        self.root.after(50, self.check_ai_result)

    def finish_game(self):
        self.game_over = True
        self.draw_board()

        black = self.board.count(BLACK)
        white = self.board.count(WHITE)

        if black > white:
            winner = "黒の勝ちです！"

        elif white > black:
            winner = "白の勝ちです！"

        else:
            winner = "引き分けです！"

        messagebox.showinfo(
            "対局終了", f"{winner}\n\n黒：{black}, 白：{white}"
        )

        with open("output.txt", "a", encoding = "utf-8") as file:
            color = "White" if self.human_color == BLACK else "Black"
            file.write(f"{self.ai_type}({color}),{black},{white},{self.board.history}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReversiGUI(root)
    root.mainloop()
