from numpy.random import binomial
fs=frozenset
def LancerSimultane(n):
    """on répète n fois le lancer simultané de deux pièces,
le programme renvoie la fréquence d'apparition des
 événéments 
on a obtenu que des piles , symbolisé par 0
on a obtenu 1 pile, 1 face, symbolisé par 1
on a obtenu que des faces , symbolisé par 2
"""
    Result=[0,0,0]
    for i in range(n):
        a= binomial(2,.5)
        Result[a]+=1
    return [x/n for x in Result]
    

    
