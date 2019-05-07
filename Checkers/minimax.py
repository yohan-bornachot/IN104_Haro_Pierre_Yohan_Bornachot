def minimax(state, depth, maximize,get_children,evaluate,dico_state={}):
    if(depth==0 or get_children(state)==[]):
        return evaluate(state)  
   
    if str(state) in dico_state:
        return(dico_state[str(state)])
    if maximize==True:
        value=float("-inf")
        for i in get_children(state):
            new_value=minimax(i,depth-1,False,get_children,evaluate,dico_state)
            value=max(value,new_value)
            dico_state[str(i)] = new_value
    else:
        value=float("+inf")
        for i in get_children(state):
            new_value=minimax(i,depth-1,True,get_children,evaluate,dico_state)
            value=min(value,new_value)
            dico_state[str(i)] = new_value
    return value

