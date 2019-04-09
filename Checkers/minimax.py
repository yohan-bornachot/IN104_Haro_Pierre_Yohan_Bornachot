def minimax(state, depth, maximize,dico_state):
    if(depth==0 or state.get_children()==[]):
        return state.evaluate()  
    value=float("-inf")
    if str(state) in dico_state:
        return(dico_state[str(state)])
    if maximize==True:
        for i in state.get_children():
            value=max(value,minimax(i,depth-1,False,dico_state))
            dico_state[str(i)] = value
    else:
        for i in state.get_children():
            value=min(-value,minimax(i,depth-1,True,dico_state))
            dico_state[str(i)] = value
    return value

