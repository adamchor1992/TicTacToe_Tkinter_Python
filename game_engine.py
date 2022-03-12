import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

import game_logic as logic
from common import *
import PIL.Image
import PIL.ImageTk
from functools import partial
import itertools

import tkinter.simpledialog


class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._master = master

        self.gameboard_size = None

        values = ["3x3", "5x5"]

        self.selected_month = tk.StringVar()

        self.combobox = ttk.Combobox(self._master,
                                     justify="center",
                                     textvariable=self.selected_month,
                                     state="readonly")
        self.combobox["values"] = values
        self.combobox.current(0)

        self.ok_button = tk.Button(self._master,
                                   text="OK",
                                   command=self.ok)

        self.close_button = tk.Button(self._master,
                                      text="CLOSE",
                                      command=exit)

        self.combobox.grid(row=0, column=0)
        self.ok_button.grid(row=1, column=0)
        self.close_button.grid(row=2, column=0)

    def ok(self):
        self.gameboard_size = self.combobox.get()

        self.combobox.destroy()
        self.ok_button.destroy()
        self.close_button.destroy()
        self._master.quit()

    def get_gameboard_size(self):
        return int(self.gameboard_size[0]), int(self.gameboard_size[2])


class TicTacToeGameGui(tk.Frame):
    def __init__(self, master, gameboard_size):
        super().__init__(master)
        self._master = master
        self.pack()

        self.gameboard_size = gameboard_size

        self.row_count = self.gameboard_size[0]
        self.column_count = self.gameboard_size[1]

        gameboard_size = self.row_count * self.column_count

        if gameboard_size == 9:
            self.check_win = logic.check_win_3x3
        elif gameboard_size == 25:
            self.check_win = logic.check_win_5x5
        else:
            raise Exception("Invalid game board")

        self._game_board = logic.create_game_board(self.row_count, self.column_count)

        self._create_widgets()

        self._players = itertools.cycle(["Player", "Computer"])

        self._empty_cell_click_flag = tk.BooleanVar(value=False)

    def _cell_clicked(self, cell_coordinates):
        """Cell buttons callback

        Args:
            cell_coordinates: Coordinates related to which button/cell was clicked

        Returns:
            None
        """

        if cell_coordinates in logic.get_empty_cells_coordinates(self._game_board):
            self._empty_cell_click_flag.set(True)
            logic.mark_cell(self._game_board, X_TOKEN, cell_coordinates)

    def _create_widgets(self):
        """Builds game graphical user interface

        Args:
            self

        Returns:
            None
        """

        button_width = 100
        button_height = 100

        path_empty_cell_image = "images/empty_cell.jpg"
        path_x_cell_image = "images/x_cell.jpg"
        path_o_cell_image = "images/o_cell.jpg"

        self.empty_cell_image = PIL.ImageTk.PhotoImage(PIL.Image.open(path_empty_cell_image))
        self.x_cell_image = PIL.ImageTk.PhotoImage(PIL.Image.open(path_x_cell_image))
        self.o_cell_image = PIL.ImageTk.PhotoImage(PIL.Image.open(path_o_cell_image))

        self.cell_buttons = {}

        for cell_coordinates in self._game_board:
            self.cell_buttons[cell_coordinates] = tk.Button(self,
                                                            width=button_width,
                                                            height=button_height,
                                                            image=self.empty_cell_image,
                                                            borderwidth=0,
                                                            command=partial(self._cell_clicked, cell_coordinates))

            self.cell_buttons[cell_coordinates].grid(row=cell_coordinates[0] - 1, column=cell_coordinates[1] - 1)

        self.restart_button = tk.Button(self,
                                        text="Restart",
                                        fg="black",
                                        command=self.restart_game)

        self.restart_button.grid(row=self.row_count, column=0, columnspan=self.column_count)

        self.quit_button = tk.Button(self,
                                     text="Quit",
                                     fg="red",
                                     command=self._master.destroy)

        self.quit_button.grid(row=self.row_count + 1, column=0, columnspan=self.column_count)

    def _refresh_gui(self):
        """Refreshes graphical interface by setting each button text according to game board state

        Returns:
            None
        """

        for cell_coordinates in self.cell_buttons:
            if self._game_board[cell_coordinates] == NULL_CELL:
                self.cell_buttons[cell_coordinates].configure(image=self.empty_cell_image)
            elif self._game_board[cell_coordinates] == X_TOKEN:
                self.cell_buttons[cell_coordinates].configure(image=self.x_cell_image)
            elif self._game_board[cell_coordinates] == O_TOKEN:
                self.cell_buttons[cell_coordinates].configure(image=self.o_cell_image)

    def restart_game(self):
        """Restarts game which effectively means resetting game board and activating again all cells

        Returns:
            None
        """
        logic.reset_game_board(self._game_board)

        for cell_button in self.cell_buttons.values():
            cell_button.configure(state="normal")

        self._refresh_gui()

    @staticmethod
    def _congratulate_winner(token):
        """Prints congratulations pointing out victorious token

        Args:
            token: String representing winning token

        Returns:
            None
        """

        tkinter.messagebox.showinfo("Information", "TOKEN {} WINS".format(token))

    def game_round(self):
        """Method managing whole round consisting of multiple game turns. Returns when round is over

        Returns:
            None
        """
        while logic.get_empty_cells_coordinates(self._game_board):
            if self._game_turn() is not None:
                return
        else:
            tkinter.messagebox.showinfo("TIE", "No more valid moves")

    def _game_turn(self):
        """Method managing whole round consisting of multiple game turns. Returns when turn is over

        Returns:
            None
        """
        if next(self._players) == "Player":
            self._master.wait_variable(self._empty_cell_click_flag)
        else:
            logic.computer_move(self._game_board)

        self._refresh_gui()

        winning_token = self.check_win(self._game_board)

        if winning_token:
            self._congratulate_winner(winning_token)
            return winning_token
        else:
            return None


def main():
    app = tk.Tk()
    app.title("Tic Tac Toe")

    app.eval('tk::PlaceWindow . center')

    menu = Menu(app)
    menu.mainloop()

    game = TicTacToeGameGui(app, menu.get_gameboard_size())

    while True:
        game.game_round()
        game.restart_game()


if __name__ == "__main__":
    main()
