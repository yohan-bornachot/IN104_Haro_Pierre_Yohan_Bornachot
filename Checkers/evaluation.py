def evaluate(state):
    boardState = state.boardState
    score = 0
    for cell in boardState.cells:
        if cell is Cell.w:
            score =+ 1
        elif cell is Cell.b:
            score -= 1
    return score