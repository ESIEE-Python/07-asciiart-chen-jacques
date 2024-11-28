"""exercice ascii"""


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c = [s[0]]
    o = [1]
    for i in s[1:]:
        if i == c[-1]:
            o[-1]+=1
        else:
            c.append(i)
            o.append(1)
    return [(c[i], o[i]) for i in range (len(c))]



def artcode_r(s):
    """retourne la liste de tuples encodant une 
    chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:
        return []
    c = s[0]
    n = 1
    while n<len(s) and s[n]==c:
        n+=1
    return [(c, n)] + artcode_r(s[n:])

def main():
    """main"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
