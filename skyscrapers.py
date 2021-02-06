"""
Skscrapers from final
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    result = list()
    with open(path) as file:
        for line in file:
            result.append(line.replace("\n", ""))
    return result


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    counter = 1
    lenth = len(input_line) - 1
    first_building = input_line[1]
    for i in range(2, lenth):
        if first_building < input_line[i]:
            first_building = input_line[i]
            counter += 1
    if counter == pivot:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present
     on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
 '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
 '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
 '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for element in board:
        for symbol in element:
            if symbol == "?":
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
 '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215',\
 '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215',\
 '*35214*', '*41532*', '*2*1***'])
    False
    """
    del board[0]
    del board[-1]
    for element in board:
        element = element[1:-1]
        for symbol in element:
            if element.count(symbol) != 1 and symbol not in " *":
                return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
 '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
 '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
 '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1, len(board) - 2):
        if board[i][0].isdigit():
            result = left_to_right_check(board[i], int(board[i][0]))
            if not result:
                return result
        if board[i][-1].isdigit():
            result = left_to_right_check(board[i][::-1], int(board[i][-1]))
            if not result:
                return result
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique
     height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    list_of_columns = list()
    lenth = len(board) - 1
    for symbol in range(1, lenth):
        part = ""
        for element in board:
            part += element[symbol]
        list_of_columns.append(part)
        for element in list_of_columns:
            element = element[1:-1]
            for symbol in element:
                if element.count(symbol) != 1 and symbol not in " *":
                    return False
    lenth = len(list_of_columns) - 1
    for i in range(lenth):
        if list_of_columns[i][0].isdigit():
            result = left_to_right_check(
                list_of_columns[i], int(list_of_columns[i][0]))
            if not result:
                return result
        if list_of_columns[i][-1].isdigit():
            result = left_to_right_check(
                list_of_columns[i][::-1], int(list_of_columns[i][-1]))
            if not result:
                return result
    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    if check_horizontal_visibility(board):
        if check_columns(board):
            if check_not_finished_board(board):
                return True
    return False
