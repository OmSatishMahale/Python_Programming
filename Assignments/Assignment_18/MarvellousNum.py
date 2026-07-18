def ChkPrime(Data):

    Sum = 0
    for no in Data:
        for i in range(2,no):
            if(no % i == 0):
                break
        else:
            Sum = Sum + no

    return Sum
            
