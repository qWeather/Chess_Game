# Avoid jumping pieces
# Killing conditions 
# Checkmate


# width for the spaces
width = 2
#  dictionary containing all the pieces
pieces = {
    'checker': u'\u25A0',
    'pawn': u'\u2659',
    'rook': u'\u2656',
    'knight': u'\u2658',
    'bishop': u'\u2657',
    'king': u'\u2654',
    'queen': u'\u2655'
}

positions = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
}
#  dictionary of player_1 moves
dict_move_p1 = {
    "rook_l": (1, 1),
    "rook_r": (1, 8),
    "knight_l": (1, 2),
    "knight_r": (1, 7),
    "bishop_l": (1, 3),
    "bishop_r": (1, 6),
    "king": (1, 5),
    "queen": (1, 4),
    "pawn_1": (2, 1),
    "pawn_2": (2, 2),
    "pawn_3": (2, 3),
    "pawn_4": (2, 4),
    "pawn_5": (2, 5),
    "pawn_6": (2, 6),
    "pawn_7": (2, 7),
    "pawn_8": (2, 8),
}
#  dictionary of player_2 moves
dict_move_p2 = {
    "rook_l": (8, 1),
    "rook_r": (8, 8),
    "knight_l": (8, 2),
    "knight_r": (8, 7),
    "bishop_l": (8, 3),
    "bishop_r": (8, 6),
    "king": (8, 5),
    "queen": (8, 4),
    "pawn_1": (7, 1),
    "pawn_2": (7, 2),
    "pawn_3": (7, 3),
    "pawn_4": (7, 4),
    "pawn_5": (7, 5),
    "pawn_6": (7, 6),
    "pawn_7": (7, 7),
    "pawn_8": (7, 8)
}


# rook = (1,8) 1,8 --> 8,8  pawn = (6,8)  1,8 --> 5,8 7,8 is empty curr position 6,8 is occcupied curr_pos(rook) < curr_pos(pawn)


# (1,8) -> (8,8) -----> (2,8) , (3,8) , (4,8) ... (8,8)  ----> input these tuples into is_occupied()


# rook at (1,8); we want to move to (4,8) and there is pawn at (2,8)
#  curr_pos[0] - next_pos[0] > 0 (in this case diff of rows 4 - 1 = 3)  
# diff_rows = 3

# for i in range(diff_rows):
# curr_pos[0] = curr_pos[0] + 1 
# if is_occupied(curr_pos[0]):
#     ...

# curr_pos[1] - next_pos[1] > 0 (in this case diff of columns = 0 coz 8 - 8 = 0)

#  function to display and update the board
def display_and_update(pos_values_1, pos_values_2):
    #  search for row and column
    #  if tuple of row and column exists in the dictionary values then the key will be equal to
    #  print all pieces based on the key in their initial positions
    #  print the rest of the board as checkers (one white, one black)
    #  if column is 8, print next row
    for r in range(1, 9):
        for c in range(1, 9):

            if (r, c) in pos_values_1:
                key = {i for i in dict_move_p1 if dict_move_p1[i] == (r, c)}

                if key == {"rook_l"} or key == {"rook_r"}:
                    print("\033[95m", pieces['rook'], "\033[0m", end='\t')
                elif key == {"knight_l"} or key == {"knight_r"}:
                    print("\033[95m", pieces['knight'], "\033[0m", end='\t')
                elif key == {"bishop_l"} or key == {"bishop_r"}:
                    print("\033[95m", pieces['bishop'], "\033[0m", end='\t')
                elif key == {"king"}:
                    print("\033[95m", pieces['king'], "\033[0m", end='\t')
                elif key == {"queen"}:
                    print("\033[95m", pieces['queen'], "\033[0m", end='\t')
                elif key == {"pawn_1"} or key == {"pawn_2"} or key == {"pawn_3"} or key == {"pawn_4"} or key == {
                    "pawn_5"} or key == {"pawn_6"} or key == {"pawn_7"} or key == {"pawn_8"}:
                    print("\033[95m", pieces['pawn'], "\033[0m", end='\t')
                if c % 8 == 0:
                    print("\n")

            elif (r, c) in pos_values_2:
                key = {i for i in dict_move_p2 if dict_move_p2[i] == (r, c)}

                if key == {"rook_l"} or key == {"rook_r"}:
                    print("\033[93m", pieces['rook'], "\033[0m", end='\t')
                elif key == {"knight_l"} or key == {"knight_r"}:
                    print("\033[93m", pieces['knight'], "\033[0m", end='\t')
                elif key == {"bishop_l"} or key == {"bishop_r"}:
                    print("\033[93m", pieces['bishop'], "\033[0m", end='\t')
                elif key == {"king"}:
                    print("\033[93m", pieces['king'], "\033[0m", end='\t')
                elif key == {"queen"}:
                    print("\033[93m", pieces['queen'], "\033[0m", end='\t')
                elif key == {"pawn_1"} or key == {"pawn_2"} or key == {"pawn_3"} or key == {"pawn_4"} or key == {
                    "pawn_5"} or key == {"pawn_6"} or key == {"pawn_7"} or key == {"pawn_8"}:
                    print("\033[93m", pieces['pawn'], "\033[0m", end='\t')
                if c % 8 == 0:
                    print("\n")

            elif c % 8 == 0:
                if r % 2 == 1:
                    if c % 2 == 1:
                        print("\033[95m", pieces['checker'], "\033[0m", end='\n' * width)
                    else:
                        print("\033[93m", pieces['checker'], "\033[0m", end='\n' * width)
                else:
                    if c % width == 0:
                        print("\033[95m", pieces['checker'], "\033[0m", end='\n' * width)
                    else:
                        print("\033[93m", pieces['checker'], "\033[0m", end='\n' * width)

            else:
                if r % width == 1:
                    if c % 2 == 1:
                        print("\033[93m", pieces['checker'], "\033[0m", end='\t' * width)
                    else:
                        print("\033[95m", pieces['checker'], "\033[0m", end='\t' * width)
                else:
                    if c % width == 0:
                        print("\033[93m", pieces['checker'], "\033[0m", end='\t' * width)
                    else:
                        print("\033[95m", pieces['checker'], "\033[0m", end='\t' * width)
    for letter in positions.keys():
        print("\033[92m", letter, "\033[0m", end='\t' * width)
    print()


def player_input():
    pass


# function to check if the next position the player wants to move to is occupied or not
def is_occupied(pos):
    # search the player_1 dictionary of pieces for the key
    # check if key has same value as the next position and don't let it move if True
    # checking for both players
    for key in dict_move_p1.keys():
        if pos == dict_move_p1[key]:
            print("\033[93m\nThe position you want to move to is already occupied!\033[0m\n")
            return False
    for key in dict_move_p2.keys():
        if pos == dict_move_p2[key]:
            print("\033[93m\nThe position you want to move to is already occupied!\033[0m\n")
            return False
    return True



# function to set the rules of the chess game
def rules(piece_name, current_piece_pos, next_piece_pos):
    # if the piece is any of the 8 pawns
    # check if the next position is occupied
    # move only one space forward
    if piece_name.startswith('pawn'):
        if abs(next_piece_pos[0] - current_piece_pos[0]) == 1 and is_occupied(next_piece_pos):
            return True
        else:
            return False
    # if the piece is any of the 2 rooks
    # check if the next position is occupied
    # move forward/backward/left/right if not outside boundaries
    if piece_name.startswith('rook'):
        if (next_piece_pos[0] == current_piece_pos[0] or \
            next_piece_pos[1] == current_piece_pos[1]) and is_occupied(next_piece_pos):
            return True
        else:
            return False
    # if the piece is any of the 2 bishops
    # check if the next position is occupied
    # move on the diagonal if not outside boundaries
    if piece_name.startswith('bishop'):
        if (next_piece_pos[0] != current_piece_pos[0] and \
            next_piece_pos[1] != current_piece_pos[1]) and is_occupied(next_piece_pos):
            return True
        else:
            return False
    # if the piece is any of the 2 knights
    # check if the next position is occupied
    # move in the shape of L up/down/left/right
    if piece_name.startswith('knight'):
        if ((abs(next_piece_pos[0] - current_piece_pos[0]) == 1 and abs(
                next_piece_pos[1] - current_piece_pos[1])) == 2) or \
                ((abs(next_piece_pos[0] - current_piece_pos[0]) == 2 and abs(
                    next_piece_pos[1] - current_piece_pos[1])) == 1) and \
                is_occupied(next_piece_pos):
            return True
        else:
            return False
    # if the piece is the king
    # check if the next position is occupied
    # move forward/backward/left/right/diagonal only one space
    if piece_name.startswith('king'):
        if ((next_piece_pos[0] - current_piece_pos[0] == 1) or \
            (next_piece_pos[1] - current_piece_pos[1] == 1)) and is_occupied(next_piece_pos):
            return True
        else:
            return False
    # if the piece is the queen
    # check if the next position is occupied
    # move forward/backward/left/right/diagonal if not outside boundaries
    if piece_name.startswith('queen'):
        if ((next_piece_pos[0] != current_piece_pos[0] and next_piece_pos[1] != current_piece_pos[1]) or \
            (next_piece_pos[0] == current_piece_pos[0] or next_piece_pos[1] == current_piece_pos[1])) and is_occupied(
            next_piece_pos):
            return True
        else:
            return False


values_1 = list(dict_move_p1.values())  # update values_1 for player_1
values_2 = list(dict_move_p2.values())  # update values_2 for player_2
display_and_update(values_1, values_2)  # update the board with the new values for both players

game = True  # bool to start the game
next_turn = True  # bool to check whose turn is it

# main loop to run the game
while game:
    #  white starts the game, at the end of the move next_turn = False and black starts turn
    #  getting input for the piece that the player wants to move
    #  current position of the piece will be returned from the dictionary
    #  getting input for the position the player wants to move the piece
    #  check that the rules are met by calling the function and update dictionary with new position
    #  update the values_1, values_2, and board at end of each turn
    if next_turn:
        print("\033[95m\nWhite's Turn\033[0m")
        piece = input("\033[95m\nWhat piece would you like to move: \033[0m")
        if piece == "pawn":
            pawn = input("\033[95m\nWhich pawn (1 to 8) would you like to move: \033[0m")
            piece += "_" + pawn
        elif piece == "rook":
            rook = input("\033[95m\nWhich rook (l or r) would you like to move: \033[0m")
            piece += "_" + rook
        elif piece == "bishop":
            bishop = input("\033[95m\nWhich bishop (l or r) would you like to move: \033[0m")
            piece += "_" + bishop
        elif piece == "knight":
            knight = input("\033[95m\nWhich knight (l or r) would you like to move: \033[0m")
            piece += "_" + knight
        curr_pos = dict_move_p1[piece]
        print(f"\033[95m\nCurrent position is {curr_pos}.\033[0m")

        poses = input("\033[95m\nWhere would you like to move: \033[0m").capitalize()
        poses = poses.strip(' ')
        pos1 = poses[-1]
        pos2 = poses[0]
        print()

        for key, value in positions.items():
            if pos2 == key:
                pos2 = value

        next_pos = (int(pos1), int(pos2))
    else:
        print("\033[93m\nBlack's Turn\033[0m")
        piece = input("\033[93m\nWhat piece would you like to move: \033[0m")
        if piece == "pawn":
            pawn = input("\033[95m\nWhich pawn (1 to 8) would you like to move: \033[0m")
            piece += "_" + pawn
        elif piece == "rook":
            rook = input("\033[95m\nWhich rook (l or r) would you like to move: \033[0m")
            piece += "_" + rook
        elif piece == "bishop":
            bishop = input("\033[95m\nWhich bishop (l or r) would you like to move: \033[0m")
            piece += "_" + bishop
        elif piece == "knight":
            knight = input("\033[95m\nWhich knight (l or r) would you like to move: \033[0m")
            piece += "_" + knight
        curr_pos = dict_move_p2[piece]
        print(f"\033[93m\nCurrent position is {curr_pos}.\033[0m")

        poses = input("\033[93m\nWhere would you like to move: \033[0m").capitalize()
        poses = poses.strip(' ')
        pos1 = poses[-1]
        pos2 = poses[0]
        print()

        for key, value in positions.items():
            if pos2 == key:
                pos2 = value

        next_pos = (int(pos1), int(pos2))

    if rules(piece, curr_pos, next_pos):
        if next_turn:
            dict_move_p1[piece] = next_pos
            next_turn = False
        else:
            dict_move_p2[piece] = next_pos
            next_turn = True
    else:
        print("\033[93m\nPiece doesn't exist or the position you tried to move to is invalid!\033[0m\n")

    values_1 = list(dict_move_p1.values())
    values_2 = list(dict_move_p2.values())
    display_and_update(values_1, values_2)
