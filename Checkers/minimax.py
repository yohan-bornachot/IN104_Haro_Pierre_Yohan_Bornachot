def minimax(state, depth, maximize,dico_state={}):
    if(depth==0 or state.get_children()==[]):
        return state.evaluate()  
   
    if str(state) in dico_state:
        return(dico_state[str(state)])
    if maximize==True:
        value=float("-inf")
        for i in state.get_children():
            new_value=minimax(i,depth-1,False,dico_state)
            value=max(value,new_value)
            dico_state[str(i)] = new_value
    else:
        value=float("+inf")
        for i in state.get_children():
            new_value=minimax(i,depth-1,True,dico_state)
            value=min(value,new_value)
            dico_state[str(i)] = new_value
    return value

