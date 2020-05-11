import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#N Population Size
N = 1000
#Initial conditions and vector
I0 = 1
R0 = 0
S0 = 999
initial = S0, I0, R0
#time
t = np.linspace(0, 200, 200)

#SIR model
def SIRmodel(v, t, N, beta, gamma):
    """Determines three differential equations of the SIR model depending on initial
    conditions and chosen parameters. dSdt determines the rate of change of
    those that are not infected but are susceptible to being infected. dIdt 
    determines the rate of change of the total infected individuals. dRdt
    determines the rate of change of the individuals who have recovered.
    
    Paramaters:
    v - vector of integers
    t - numeric sequence of form np.linspace(start, end, number of breakpoints)
    N - integer
    beta - float
    gamma - float
    
    Returns:
    Tuple of 3 floats, the change in the values of the differential 
    equations of the model at one instant in time
    """
    S, I, R = v
    dSdt = (-1 * beta * S * I) / N
    dIdt = (beta * S * I / N) - (gamma * I)
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Integrating and plotting the differential equations in the SIR model
def integrate_SIR(gamma, beta):
    """Plots the SIR model of disease for given gamma and beta parameters
    
    Parameters:
    gamma - float, reciprocal of average period of infectiousness
    beta - float, proportionality of how many people get into contact with the infected person.

    
    Returns:
    Plot of number of susceptible individuals, infected individuals, and 
    recovered individuals over time
    """
    int_SIR = odeint(SIRmodel, initial, t, args=(N, beta, gamma))
    S, I, R = int_SIR.T
    
    # Plot S(t), I(t) and R(t)
    plt.plot(t, S, 'b', label='Susceptible Individuals')
    plt.plot(t, I, 'r', label='Infected Individuals')
    plt.plot(t, R, 'g', label='Recovered Individuals')
    plt.xlabel('Time (days)')
    plt.ylabel('Number of Individuals')
    plt.title('SIR Model of Disease Spread with \u03B3 = '+ str(round(gamma,2))+ ' \u03B2 = '+ str(beta))
    plt.legend()
    plt.show()

#Plotting for a variety of chosen beta and gamma parameters
integrate_SIR(1/10, 0.2)
integrate_SIR(1/10, 0.1)
integrate_SIR(1/7, 0.2)
integrate_SIR(1/14, 0.2)

