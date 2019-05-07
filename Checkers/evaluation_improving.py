import IN104_simulateur as simu

def evaluate(state):
    Cell = simu.Cell
    boardState = state.boardState
    score = 0
    cell = boardState.cells
    nRow = boardState.nRows
    boardSize = len(cell)
    for k in range(0,boardSize):
        [r,c] = boardState.indexToRC(k)
        if cell[k] is Cell.w:
            score += r
        elif cell[k] is Cell.b:
            score -= r
        elif cell[k] is Cell.B:
            score -= nRow+3
        elif cell[k] is Cell.W:
            score += nRow+3
    return score