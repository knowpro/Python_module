
def calculation(nano1, nano2):
    """
    

    Parameters
    ----------
    nano1 : float
        it is no 1.
    nano2 : float
        it is no 2.

    Returns
    -------
    None.

    """
    
    return (nano1+nano2), (nano1-nano2), (nano1/nano2), (nano1*nano2)
    
res = calculation(10, 15)

print(res)