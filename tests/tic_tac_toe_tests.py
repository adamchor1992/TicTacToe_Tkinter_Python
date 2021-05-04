import unittest
from game import logic
from game.common import *

ROW_COUNT = 3
COLUMN_COUNT = 3


class GameBoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = logic.create_game_board(ROW_COUNT, COLUMN_COUNT)

    def test_function_create_game_board(self):
        self.assertEqual(len(self.game_board), 9)

        for cell_coordinates in self.game_board:
            self.assertEqual(self.game_board[cell_coordinates], NULL_TOKEN)

    def test_function_reset_game_board(self):
        self.game_board[(1,1)] = X_TOKEN
        self.game_board[(2,2)] = X_TOKEN
        self.game_board[(3,3)] = X_TOKEN

        logic.reset_game_board(self.game_board)

        self.assertEqual(self.game_board[(1, 1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1, 2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1, 3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2, 1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2, 2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2, 3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3, 1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3, 2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3, 3)], NULL_TOKEN)

    def test_function_get_empty_cells_coordinates_all_cells_empty(self):
        self.assertEqual(len(logic.get_empty_cells_coordinates(self.game_board)), 9)

        self.assertEqual(self.game_board[(1,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,3)], NULL_TOKEN)

    def test_function_get_empty_cells_coordinates_6_cells_empty(self):
        self.game_board[(1,1)] = X_TOKEN
        self.game_board[(2,2)] = X_TOKEN
        self.game_board[(3,3)] = X_TOKEN

        self.assertEqual(len(logic.get_empty_cells_coordinates(self.game_board)), 6)

        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)

    def test_function_logic_mark_cell(self):
        logic.mark_cell(self.game_board, X_TOKEN, (1,1))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))
        logic.mark_cell(self.game_board, X_TOKEN, (3,3))

        self.assertEqual(self.game_board[(1,1)], X_TOKEN)
        self.assertEqual(self.game_board[(2,2)], X_TOKEN)
        self.assertEqual(self.game_board[(3,3)], X_TOKEN)

        self.assertEqual(self.game_board[(1,2)], NULL_TOKEN)
        self.assertEqual(self.game_board[(1,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(2,3)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,1)], NULL_TOKEN)
        self.assertEqual(self.game_board[(3,2)], NULL_TOKEN)


class WinningPattern3x3Tests(unittest.TestCase):
    def setUp(self):
        ROW_COUNT = 3
        COLUMN_COUNT = 3
        self.game_board = logic.create_game_board(ROW_COUNT, COLUMN_COUNT)

    def test_function_logic_check_win_3x3_return_winning_X_token(self):
        logic.mark_cell(self.game_board, X_TOKEN, (1,1))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))
        logic.mark_cell(self.game_board, X_TOKEN, (3,3))

        self.assertEqual(logic.check_win_3x3(self.game_board), X_TOKEN)
 
    def test_function_logic_check_win_3x3_return_winning_O_token(self):
        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,1))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)
        
    def test_function_logic_check_win_3x3_all_cases(self):
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (1,2))
        logic.mark_cell(self.game_board, O_TOKEN, (1,3))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)
        
        logic.mark_cell(self.game_board, O_TOKEN, (2,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (3,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,1))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,2))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,1))

        self.assertEqual(logic.check_win_3x3(self.game_board), O_TOKEN)


class WinningPattern5x5Tests(unittest.TestCase):
    def setUp(self):
        ROW_COUNT = 5
        COLUMN_COUNT = 5
        self.game_board = logic.create_game_board(ROW_COUNT, COLUMN_COUNT)

    def test_function_logic_check_win_5x5_return_winning_X_token(self):
        logic.mark_cell(self.game_board, X_TOKEN, (1,1))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))
        logic.mark_cell(self.game_board, X_TOKEN, (3,3))
        logic.mark_cell(self.game_board, X_TOKEN, (4,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), X_TOKEN)
 

    def test_function_logic_check_win_5x5_return_winning_O_token(self):
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))
        logic.mark_cell(self.game_board, O_TOKEN, (5,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)
        

    def test_function_logic_check_win_5x5_horizontal_patterns(self):
        """Test all 10 horizontal winning cases"""
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (1,2))
        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (1,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)
        
        logic.mark_cell(self.game_board, O_TOKEN, (1,2))
        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (1,4))
        logic.mark_cell(self.game_board, O_TOKEN, (1,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,4))
        logic.mark_cell(self.game_board, O_TOKEN, (2,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (3,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,4))
        logic.mark_cell(self.game_board, O_TOKEN, (3,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (4,1))
        logic.mark_cell(self.game_board, O_TOKEN, (4,2))
        logic.mark_cell(self.game_board, O_TOKEN, (4,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (4,2))
        logic.mark_cell(self.game_board, O_TOKEN, (4,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))
        logic.mark_cell(self.game_board, O_TOKEN, (4,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (5,1))
        logic.mark_cell(self.game_board, O_TOKEN, (5,2))
        logic.mark_cell(self.game_board, O_TOKEN, (5,3))
        logic.mark_cell(self.game_board, O_TOKEN, (5,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (5,2))
        logic.mark_cell(self.game_board, O_TOKEN, (5,3))
        logic.mark_cell(self.game_board, O_TOKEN, (5,4))
        logic.mark_cell(self.game_board, O_TOKEN, (5,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)
        

    def test_function_logic_check_win_5x5_vertical_patterns(self):
        """Test all 10 vertical winning cases"""
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,1))
        logic.mark_cell(self.game_board, O_TOKEN, (4,1))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,1))
        logic.mark_cell(self.game_board, O_TOKEN, (4,1))
        logic.mark_cell(self.game_board, O_TOKEN, (5,1))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,2))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (4,2))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (4,2))
        logic.mark_cell(self.game_board, O_TOKEN, (5,2))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,3))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,3))
        logic.mark_cell(self.game_board, O_TOKEN, (5,3))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,4))
        logic.mark_cell(self.game_board, O_TOKEN, (2,4))
        logic.mark_cell(self.game_board, O_TOKEN, (3,4))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,4))
        logic.mark_cell(self.game_board, O_TOKEN, (3,4))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))
        logic.mark_cell(self.game_board, O_TOKEN, (5,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,5))
        logic.mark_cell(self.game_board, O_TOKEN, (2,5))
        logic.mark_cell(self.game_board, O_TOKEN, (3,5))
        logic.mark_cell(self.game_board, O_TOKEN, (4,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,5))
        logic.mark_cell(self.game_board, O_TOKEN, (3,5))
        logic.mark_cell(self.game_board, O_TOKEN, (4,5))
        logic.mark_cell(self.game_board, O_TOKEN, (5,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)


    def test_function_logic_check_win_5x5_diagonal_patterns(self):
        """Test all 8 diagonal winning cases"""
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,2))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,4))
        logic.mark_cell(self.game_board, O_TOKEN, (5,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,5))
        logic.mark_cell(self.game_board, O_TOKEN, (2,4))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,2))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,4))
        logic.mark_cell(self.game_board, O_TOKEN, (3,3))
        logic.mark_cell(self.game_board, O_TOKEN, (4,2))
        logic.mark_cell(self.game_board, O_TOKEN, (5,1))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (4,3))
        logic.mark_cell(self.game_board, O_TOKEN, (5,4))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,2))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,4))
        logic.mark_cell(self.game_board, O_TOKEN, (4,5))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (1,4))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, O_TOKEN, (3,2))
        logic.mark_cell(self.game_board, O_TOKEN, (4,1))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)

        logic.reset_game_board(self.game_board)

        logic.mark_cell(self.game_board, O_TOKEN, (2,5))
        logic.mark_cell(self.game_board, O_TOKEN, (3,4))
        logic.mark_cell(self.game_board, O_TOKEN, (4,3))
        logic.mark_cell(self.game_board, O_TOKEN, (5,2))

        self.assertEqual(logic.check_win_5x5(self.game_board), O_TOKEN)


class ComputerAiTests(unittest.TestCase):
    def setUp(self):
        self.game_board = logic.create_game_board(ROW_COUNT, COLUMN_COUNT)

    def test_function_computer_move_win_in_next_move_case1(self):
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,2))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)

    def test_function_computer_move_win_in_next_move_case2(self):
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (1,2))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(1,3)], O_TOKEN)

    def test_function_computer_move_win_in_next_move_case3(self):
        logic.mark_cell(self.game_board, O_TOKEN, (1,3))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)

    def test_function_computer_move_avoid_lose_in_next_move_case1(self):
        logic.mark_cell(self.game_board, X_TOKEN, (1,1))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)

    def test_function_computer_move_avoid_lose_in_next_move_case2(self):
        logic.mark_cell(self.game_board, X_TOKEN, (1,2))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,2)], O_TOKEN)

    def test_function_computer_move_avoid_lose_in_next_move_case3(self):
        logic.mark_cell(self.game_board, X_TOKEN, (1,3))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,1)], O_TOKEN)

    def test_function_computer_move_select_best_non_winning_non_losing_move_case1(self):
        """First move should always be middle cell"""
        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(2,2)], O_TOKEN)

    def test_function_computer_move_select_best_non_winning_non_losing_move_case2(self):
        """If middle cell is not empty the next move should be left upper corner cell"""
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))

        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(1,1)], O_TOKEN)

    def test_function_computer_move_select_best_non_winning_non_losing_move_case3(self):
        """If middle cell all left upper/lower and right upper corner is not empty the next move should be right lower corner"""
        logic.mark_cell(self.game_board, O_TOKEN, (1,1))
        logic.mark_cell(self.game_board, O_TOKEN, (3,1))
        logic.mark_cell(self.game_board, O_TOKEN, (2,3))
        logic.mark_cell(self.game_board, X_TOKEN, (2,1))
        logic.mark_cell(self.game_board, X_TOKEN, (2,2))
        logic.mark_cell(self.game_board, X_TOKEN, (1,3))
        
        logic.computer_move(self.game_board)

        self.assertEqual(self.game_board[(3,3)], O_TOKEN)


class UtilitesTests(unittest.TestCase):
    def test_function_search_for_duplicates_no_duplicates(self):
        test_list = [(5,3), (1,3), (2,1)]

        self.assertFalse(logic.search_for_duplicates(test_list))

    def test_function_search_for_duplicates_1_duplicate(self):
        test_list = [(2,4), (1,2), (2,1), (1,3), (2,4), (8,2)]

        self.assertTrue(logic.search_for_duplicates(test_list))

    def test_function_search_for_duplicates_2_duplicate(self):
        test_list = [(1,4), (3,4), (1,4), (8,2), (5,2), (3,4)]

        self.assertTrue(logic.search_for_duplicates(test_list))


if __name__ == "__main__":
    unittest.main()
