def minimax(state, depth, maximize,get_children,evaluate,dico_state={},maxi=float("-inf"),mini=float("+inf")):
    children=get_children(state)
    if(depth==0 or children==[]):
        return evaluate(state)
    if str(state) in dico_state:
        return(dico_state[str(state)])
    if maximize==True:
        value=float("-inf")
        for i in children:
            new_value=minimax(i,depth-1,False,get_children,evaluate,dico_state)
            value=max(value,new_value)
            dico_state[str(i)] = new_value
            if value>=mini:
                return value
            maxi=max(value,maxi)
    else:
        value=float("+inf")
        for i in children:
            new_value=minimax(i,depth-1,True,get_children,evaluate,dico_state)
            value=min(value,new_value)
            dico_state[str(i)] = new_value
            if value<=maxi:
                return value
            mini=min(value,mini)
    return value