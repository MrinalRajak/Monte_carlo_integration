
# Monte Carlo Integration

import numpy as np
import matplotlib.pyplot as plt
f=lambda x: np.sin(x)
'''

def MonteCarloInt(a,b,f):
    N=100000                 # No.of trials
    x=np.linspace(a,b,N)     # x-Domain
    y_min=0
    y_max=np.max((f(x)))+1
    A=(b-a)*(y_max-y_min)    # Area under the curve
    y=np.random.uniform(y_min,y_max,N)
    n=np.sum([abs(y)<abs(f(x))])   # points under the curve
    return float(A*n)/N

print (MonteCarloInt(0,np.pi,f))
'''

# Another approach
def MCI():
    x=np.random.uniform(a,b,N)
    return (b-a)*np.mean(f(x))
N=10000
a,b=0,np.pi
print (MCI())
X=[MCI() for i in range(10000)]
with plt.xkcd():
    plt.hist(X,bins=50,color='crimson',ec='blue')
    plt.show()

    
