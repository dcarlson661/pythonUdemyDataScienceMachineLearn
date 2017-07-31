
""" multi-line comment three dblquotes
20170728 
"""

import numpy as np
incomes=np.random.normal(27000,15000,10000)
themean=np.mean(incomes)
#print(themean)


import matplotlib.pyplot as plt 
plt.hist(incomes,50);
plt.show()

#print("median="+str(np.median(incomes)))
#print("mean  ="+str(np.mean(incomes)))

incomes=np.append(incomes,1000000000)

#print("medianAfter="+str(np.median(incomes)))
#print("mean  After="+str(np.mean(incomes)))

ages = np.random.randint(10,high=90, size=500)
#print("ages="+str(ages))

from scipy import stats
m = stats.mode(ages);
print (m)


