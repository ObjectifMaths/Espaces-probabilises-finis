from numpy.random import binomial

def LancerConsecutif(n):
    """on répète n fois le lancer consécutif de deux pièces,
 le programme renvoie la fréquence d'apparition des événéments
 (pile,pile), (pile, face), (face,pile), (face, face)"""
    Result={(0,0):0, (0,1):0, (1,0):0, (1,1):0}
    for i in range(n):
        a=binomial(1,.5)
        b=binomial(1,.5)
        Result[(a,b)]+=1
    return {x:Result[x]/n for x in Result}

    
