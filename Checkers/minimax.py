def minimax(state, depth, maximize):
    Dico_state={}
    if(depth==0 or state.get_children()==[]):
        return state.evaluate()  
    value=float("-inf")  
    if maximize==True:
        for i in state.get_children():
            if str(i) not in Dico_state: 
                value=max(value,minimax(i,depth-1,False))
                Dico_state[str(i)] = value

    else:
        for i in state.get_children():
            if str(i) not in Dico_state: 
                value=min(-value,minimax(i,depth-1,True))
                Dico_state[str(i)] = value
    return value

