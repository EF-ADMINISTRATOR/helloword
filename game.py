def is_win(game):
    """Return whether either player has three marks in a line."""
    lines = list(game)
    lines += [[game[r][c] for r in range(3)] for c in range(3)]
    lines += [[game[i][i] for i in range(3)],
              [game[i][2 - i] for i in range(3)]]
    return any(line[0] in ('X', 'O') and line[0] == line[1] == line[2]
               for line in lines)


def main():
    game = [['*' for _ in range(3)] for _ in range(3)]
    print('X = Player 1')
    print('O = Player 2')

    for turn in range(9):
        player = 'X' if turn % 2 == 0 else 'O'
        while True:
            try:
                row, col = map(int, input(
                    f'Player {1 if player == "X" else 2}: '
                    'Which cell to mark? i:[1..3], j:[1..3]: '
                ).split())
                if not (1 <= row <= 3 and 1 <= col <= 3):
                    print('Please enter two numbers from 1 to 3.')
                    continue
                row -= 1
                col -= 1
                if game[row][col] != '*':
                    print('That cell is occupied. Try again.')
                    continue
                break
            except ValueError:
                print('Please enter two numbers from 1 to 3.')

        game[row][col] = player
        for board_row in game:
            print(' '.join(board_row))
        if is_win(game):
            print(f'Player {1 if player == "X" else 2} wins!')
            break
    else:
        print('Tie!')


if __name__ == '__main__':
    main()
