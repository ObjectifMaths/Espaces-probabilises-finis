def frequence(n,r,b,v):
    """n est le nombre de tirages effectués avec remise
dans une urne contenant r boule rouge, b boules bleues, 
v boules vertes. Le programme renvoie la fréquence 
d'apparition de chaque couleur dans l'ordre R,B,V""" 
    from random import shuffle
    Urne=['R']*r+['B']*b+['V']*v
    d={'R':0, 'B':1, 'V':2}
    ResTir=[0,0,0]
    for i in range(n):
        shuffle(Urne)
        ResTir[d[Urne[0]]]+=1
    Freq=[ResTir[j]/n for j in range(len(ResTir))]
    return Freq
