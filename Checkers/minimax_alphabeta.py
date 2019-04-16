def minimax(state, depth, maximize,dico_state={},maxi=float("-inf"),mini=float("+inf")):
    children=state.get_children
    if(depth==0 or children==[]):
        return state.evaluate()  
    value=float("-inf")
    if str(state) in dico_state:
        return(dico_state[str(state)])
    if maximize==True:
        for i in children:
            value=max(value,minimax(i,depth-1,False,dico_state,maxi,mini))
            dico_state[str(i)] = value
            if value>=mini:
                return value
            maxi=max(value,maxi)
    else:
        for i in children:
            value=min(-value,minimax(i,depth-1,True,dico_state,maxi,mini)
            dico_state[str(i)] = value
            if value<=maxi:
                return value
            mini=min(value,mini)
    return value