import numpy as np 
import matplotlib.pyplot as plt


def logistic (r,initialTerm,n) :
    
    xlogistic = np.zeros((n,1))
    ylogistic = np.zeros((n,1)) 
           
    ylogistic[0] = initialTerm
    
    for i in range(1,n):
        ylogistic[i] = r*ylogistic[i-1]*(1-ylogistic[i-1])
        #print(ylogistic[i]) 
    
    xlogistic[0] = ylogistic[49]
    for i in range(1,n,1):
        xlogistic[i] = r*xlogistic[i-1]*(1-xlogistic[i-1])
        #print(xlogistic[i])
        
    return(xlogistic)

def logbifurc(R1,R2) :
    step = (R2-R1)/100
    x0 = 0.5
    
    while R1 < R2 :
        theLogisticMap = logistic(R1,x0,50)
        RR = R1 * np.ones((50,1))
        plt.plot(RR,theLogisticMap,'.')  
        R1 = R1 + step

    plt.show()
    return()

"""
Testing the Function
"""
logbifurc(1,4)