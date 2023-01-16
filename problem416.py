
import numpy as np
from copy import deepcopy
import time
import typing


start = time.time()
m = 10
n = 10**12


# The state is made up of four components
# 1) trips using this square
# 2) other tirps using the previous square
# 3) other trips using the square before that
# 4) number of past or present squares that are not used on any trip
init = (2*m,0,0,0)  # initial state

def binom(n:int,k:int):
    """Compute the binomial coefficient"""
    res = 1
    for j in range(n-k+1,n+1):
        res *= j
    for j in range(2,k+1):
        res //= j
    return res

def next_state(state):
    """Returns a dictionary in which all states that can be reached in one
    turn from state are keys.  The value associated with each key is the
    number of ways that the transition can be made."""
    res = {}
    if (state[-1] == 0) and (state[2] == 0):
        # No trip uses the current square
        res[(0,)+state[0:2]+(1,)] = 1

    for ones in range(state[0]+1):  # frogs landing after a jump of 1
        mult0 = binom(state[0],ones)
        for twos in range(state[1]+1): # frogs landing after a jump of 2
            mult1 = mult0*binom(state[1],twos)
            if ones+twos == 2*m:
                continue
            res[(sum(state[:3])-ones-twos,
                 ones,
                 twos,
                 state[3])] = mult1
    return res

# assign IDs to each state
state_ids = {init:0}   # given a state returns the ID
states = [init]        # states[k] is the state with ID k


old = [init]  # states for which next_state needs to be considered
while old:
    curr = []
    for s in old:
        for ns in next_state(s):
            if ns not in state_ids:
                state_ids[ns] = len(states)
                states.append(ns)
                curr.append(ns)
    old = curr

N = len(states)  # number of states

# Build the transition matrix
dtype = np.uint64  # numpy integer type
M = np.zeros((N,N),dtype)

for s in states:
    id = state_ids[s]
    ns_dict = next_state(s)
    for ns in ns_dict:
        n_id = state_ids[ns]
        M[n_id,id] += ns_dict[ns]

# Initial state
vinit = np.zeros((N,),dtype)
vinit[state_ids[init]] = 1

# Final states
vend = np.zeros((N,),dtype)
vend[state_ids[init]] = 1
vend[state_ids[2*m,0,0,1]] = 1

def mult(M1,M2,modulus=10**9):
    """Multiplies two matrices in mod modulus"""
    M2_big   = M2 // 10**5
    M2_small = M2 %  10**5
    res_big = np.einsum('ik,kj->ij', M1,M2_big) % modulus
    res_small = np.einsum('ik,kj->ij', M1,M2_small)
    return ((res_big*10**5)+res_small) % modulus

def matrix_exp(M,q,modulus=10**9):
    """Returns the q-th power of M mod modulus"""
    # uses the binary method
    assert q > 0
    res = deepcopy(M)   # resulting matrix
    power = deepcopy(M) # M up to a power of two
    q -= 1
    while q > 0:
        print("q = "+str(q)+" time = "+str(time.time()-start))
        if q & 1:
            res = mult(power,res,modulus)
        power = mult(power,power,modulus)
        q //= 2
    return res

print(int(vend.dot(matrix_exp(M,n-1).dot(vinit))) % 10**9)
print("it took "+str(time.time()-start)+" seconds")