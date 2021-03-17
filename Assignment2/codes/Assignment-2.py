import numpy as np

from scipy.stats import bernoulli


sim_len=int(1e7)
sample_size=216
event_size=6
#prob for X=1, i.e., probability for 3 dice showing same number
prob=event_size/sample_size
#creating random variables
data_bern = bernoulli.rvs(size=sim_len,p=prob)
#checking for X=1
err_ind = np.nonzero(data_bern == 1)
#finding the size of err_ind,i.e., number of cases where X=1 and dividing it by sample size 
err_n = np.size(err_ind)/sim_len

#Theory vs Simulation
print("The theroretical result is {} while the result obtained through simulation is {}".format(prob,err_n))



#Alternate solution
import random

count=0
for i in range(sim_len):
    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    roll3=random.randint(1,6)
    
    if roll1==roll2==roll3:
        count=count+1
probability=count/sim_len

print("With the help of another simulation, the result obatined is {}".format(probability))

