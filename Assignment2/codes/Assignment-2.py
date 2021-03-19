import math

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#function to calculate probability that none of the digits in the k digit number are 0,5 or 9
def theoreticalprob(m):

    return pow(0.7,m)


k=int(input("Enter the number k- the number of digits upto which you want to analyse"))

#function to calculate binomial coefficient
#Generating k cases to verify our result with the simulation
probab_theo=[]
probab_sim=[]
for i in range(1,k+1):
    probab_theo.append(theoreticalprob(i))

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


for i in range(1,k+1):
        probab_sim.append(simprob(i))                   
        
        
#plotting

cases = []
for i in range(1,k+1):
    cases.append(i)

#probab_theo = [case_1, case_2, case_3, case_4, case_5 , case_6, case_7, case_8, case_9, case_10]
#probab_sim = [case_1_sim,case_2_sim,case_3_sim,case_4_sim, case_5_sim , case_6_sim, case_7_sim, case_8_sim, case_9_sim, case_10_sim]

x = np.arange(len(cases))

plt.stem(cases,probab_sim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(cases,probab_theo, markerfmt='x',use_line_collection=True, label='Theory')
plt.xlabel('number of digits')
plt.ylabel('Probabilty')
plt.title("")
plt.legend()
plt.grid()