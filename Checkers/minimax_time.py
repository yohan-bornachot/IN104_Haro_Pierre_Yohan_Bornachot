from time import clock

delta_children=1.6689300537109375e-6

def minimax(state, temps_imparti, maximize,get_children,evaluate,dico_state={}):
    time=clock()
    global delta_children
    if delta_children>temps_imparti: #PAS LE TEMPS D'EXPLORER LES ENFANTS   
        return evaluate(state)

    else:
        Children=get_children(state)
        if Children==[]: #PAS D'ENFANT DONC FEUILLE
            return evaluate(state)
   
        if str(state) in dico_state: #CONFIGURATION DU PLATEAU DEJA RENCONTREE
            return(dico_state[str(state)])

        if maximize==True:
            
            j=0 #INDICE INDIQUANT QUEL ENFANT ON EST EN TRAIN D'EXPLORER
            delta=0 
            value=float("-inf")
            
            for i in Children:
                t1=clock()
                delta= t1-time
                temps_imparti_suiv=(temps_imparti-delta)/(len(Children)-j) #TEMPS_IMPARTI_SUIV EVOLUE EN FONCTION DU TEMPS QUE PRENNENT LES ENFANTS POUR RECEVOIR UN SCORE
                new_value=minimax(i,temps_imparti_suiv,False,get_children,evaluate,dico_state)
                value=max(value,new_value)
                dico_state[str(i)] = new_value
                j+=1
        else :
            time=clock()
            j=0 #INDICE INDIQUANT QUEL ENFANT ON EST EN TRAIN D'EXPLORER
            delta=0
            value=float("+inf")

            for i in Children:
                t1=clock()
                delta= t1-time
                temps_imparti_suiv=(temps_imparti-delta)/(len(Children)-j)
                new_value=minimax(i,temps_imparti_suiv,True,get_children,evaluate,dico_state)
                value=min(value,new_value)
                dico_state[str(i)] = new_value
                j+=1
        return value
