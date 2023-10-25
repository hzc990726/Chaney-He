def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
        return input_board

    # Modify the current cell
    input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]

    # Recursive calls to neighboring cells
    flood_fill(input_board, old, new, x+1, y)
    flood_fill(input_board, old, new, x-1, y)
    flood_fill(input_board, old, new, x, y+1)
    flood_fill(input_board, old, new, x, y-1)

    return input_board
