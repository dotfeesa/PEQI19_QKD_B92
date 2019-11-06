# Created by: Sarajevo team (L.Lemeš, M.Šetić, A.Kerla, E.Ibragic, H.Tarahija, B.Džanko, E.Dervišević, M.Mehić)
# PEQI Hachaton 2019
# University of Sarajevo, Sarajevo, Bosnia and Herzegovina
# Department of Telecommunications
# www.tk.etf.unsa.ba

import sys
from math import ceil, log, sqrt
from random import randint, random, sample
from multiprocessing import pool
from cqc.pythonLib import CQCConnection, qubit

bits_alice = []
mesurments_bob = []

def preperation_Alice():
    with CQCConnection("Alice") as Alice:
        for i in range(100):
            random_bits_alice = randint(0,1)
            bits_alice.append(random_bits_alice)

            q = qubit(Alice)

            if random_bits_alice == 1:
                q.X()   

            if random_bits_alice == 1:
                q.H()

            Alice.sendQubit(q, "Bob")
            
        Alice.flush()
        r = Alice.recvClassical()
        mesurments_bob[:] = list(r)
        print ("bits of alice:", bits_alice)
        print ("mem bob:", mesurments_bob)
        error = 0;
        for i in range(len(mesurments_bob)):
            if (mesurments_bob[i] == 0):
                error = error + 1
        print("error", len(mesurments_bob))
        error_percentage = error/len(mesurments_bob) # maximum value is 1
        print("error_percentage", error_percentage)

if __name__ == "__main__":
    preperation_Alice()
