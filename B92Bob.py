# Created by: Sarajevo team (L.Lemeš, M.Šetić, A.Kerla, E.Ibragic, H.Tarahija, B.Džanko, E.Dervišević, M.Mehić)
# PEQI Hachaton 2019
# University of Sarajevo, Sarajevo, Bosnia and Herzegovina
# Department of Telecommunications
# www.tk.etf.unsa.ba

import sys
from math import ceil, log, sqrt
from random import randint, random, sample
from multiprocessing import Pool
from cqc.pythonLib import CQCConnection, qubit

correct_basis = []
correct_key = []
bits_alice = []
basis_alice = []
bits_bob = []
basis_bob = [] 
received = []
results = []

def preparation_Bob():
    with CQCConnection("Bob") as Bob:
        for i in range(100):
            
            q = Bob.recvQubit()
            random_basis_bob = randint(0,1)
            basis_bob.append(random_basis_bob)
            if random_basis_bob == 1:
               q.H()
            m = q.measure()
            if (random_basis_bob == 0 and m == 0):
               results.append(0);
            elif (random_basis_bob == 0 and m == 1):
               results.append(1);
            elif (random_basis_bob == 1 and m == 0):
               results.append(1);
            else:
               results.append(0);
            received.append(m)
            
        
    print ("basis of bob ", basis_bob)
    print ("measurement results of bob: ",received)
    print ("results ", results)

    Bob.sendClassical("Alice", results)

if __name__ == "__main__":
    preparation_Bob()

