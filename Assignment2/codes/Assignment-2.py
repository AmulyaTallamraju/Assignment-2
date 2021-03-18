import math

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#function to calculate probability that none of the digits in the k digit number are 0,5 or 9
def theoreticalprob(k):

    return pow(0.7,k)

#function to calculate binomial coefficient
#Generating 10 cases to verify our result with the simulation
case_1 = theoreticalprob(1)
case_2 = theoreticalprob(2)
case_3 = theoreticalprob(3)
case_4 = theoreticalprob(4)
case_5 = theoreticalprob(5)
case_6 = theoreticalprob(6)
case_7 = theoreticalprob(7)
case_8 = theoreticalprob(8)
case_9 = theoreticalprob(9)
case_10 = theoreticalprob(10)

def simprob(a):
    s=0
    count=0
    
    while s<1000000:
        liste=[]
        for i in range(0,a):
            liste.append(str(random.randint(0,9)))
        if '0' not in liste and '5' not in liste and '9' not in liste:
            count= count+1
        else:
            pass
        s=s+1
    return count/s
            
case_1_sim = simprob(1)
case_2_sim = simprob(2)
case_3_sim = simprob(3)
case_4_sim = simprob(4)
case_5_sim = simprob(5)
case_6_sim = simprob(6)
case_7_sim = simprob(7)
case_8_sim = simprob(8)
case_9_sim = simprob(9)
case_10_sim = simprob(10)            
        
        

#plotting

cases = ['1', '2', '3', '4','5','6','7','8','9','10']

probab_theo = [case_1, case_2, case_3, case_4, case_5 , case_6, case_7, case_8, case_9, case_10]
probab_sim = [case_1_sim,case_2_sim,case_3_sim,case_4_sim, case_5_sim , case_6_sim, case_7_sim, case_8_sim, case_9_sim, case_10_sim]

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.10, label = 'Theoretical')
plt.bar(x + 0.10, probab_sim, color = 'r', width = 0.10, label = 'Sim')
plt.xlabel('Number of digits')
plt.ylabel("Probability that the numbers don't contain the digits 0,5 or 9")
plt.xticks(x  + 0.10/2,['1', '2', '3', '4','5','6','7','8','9','10'])
plt.legend()
plt.show()