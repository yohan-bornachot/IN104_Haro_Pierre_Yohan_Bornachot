import IN104_simulateur as simu

def evaluate(state):
    Cell = simu.Cell
    boardState = state.boardState
    score = 0
    cell = boardState.cells
    for k in range(0,32):
        [r,c] = boardState.indexToRC(k)
        if cell[k] is Cell.w:
            score =+ r
        elif cell[k] is Cell.b:
            score -= r
        elif cell[k] is Cell.B:
            score -= 10
        elif cell[k] is Cell.W:
            score += 10
    return score