import random

def flip1(N):
    coin = [0]*5 + [1]*2
    
    record = []
    for i in range(N):
        record.append(random.choice(coin))

    return record

def flip2(N):
    coin = [0]*5 + [1]*5
    
    record = []
    for i in range(N):
        record.append(random.choice(coin))

    return record

def flip3(N):
    coin = [0]*50 + [1]*51
    
    record = []
    for i in range(N):
        record.append(random.choice(coin))

    return record
