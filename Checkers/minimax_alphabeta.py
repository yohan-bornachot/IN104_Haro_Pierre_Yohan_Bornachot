def minimax(state, depth, maximize,dico_state={},maxi=float("-inf"),mini=float("+inf")):
    children=state.get_children()
    if(depth==0 or children==[]):
        return state.evaluate()
    if str(state) in dico_state:
        return(dico_state[str(state)])
    if maximize==True:
        value=float("-inf")
        for i in children:
            new_value=minimax(i,depth-1,False,dico_state)
            value=max(value,new_value)
            dico_state[str(i)] = new_value
            if value>=mini:
                return value
            maxi=max(value,maxi)
    else:
        value=float("+inf")
        for i in children:
            new_value=minimax(i,depth-1,True,dico_state)
            value=min(value,new_value)
            dico_state[str(i)] = new_value
            if value<=maxi:
                return value
            mini=min(value,mini)
    return value