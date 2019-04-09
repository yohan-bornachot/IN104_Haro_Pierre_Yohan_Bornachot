def minimax(state, depth, maximize):
    if(depth==0 or state.get_children()==[]):
        return state.evaluate()    

    if maximize==True:
        value=float("-inf")
        for i in state.get_children():
            value=max(value,minimax(i,depth-1,False))
        return value
    else:
        value=float("+inf")
        for i in state.get_children():
            value=min(value,minimax(i,depth-1,True))
        return value

