import numpy as np
from scipy.special import erf

def CalcNsat(M, M0, M1, alpha):
	#print(M,">?",M0)
	#print(M*alpha,">?",M0
        if (M*alpha>M0*alpha):
                return (((10**M) - 10**M0)/10**M1)**alpha
        else:
                return 0.

Nsat = np.vectorize(CalcNsat)

def CalcNcent(M, Mmin, sig):
	return 0.5*( 1 + erf((M - Mmin)/sig))

Ncent = np.vectorize(CalcNcent)


data = np.genfromtxt("Mn_n_b_Halostest_halfres.txt")
logM = data[:,0]
N = data[:,1]
b = data[:,2]

V = 500**3
n = N/V
alpha = 1.0
sig = 2.0
logM0 = 11.0
logMmin = 12.8
logM1 = 11
#logM1 = 1 +logMmin
#print(logM)
#print(Nsat(logM, logM0, logM1, alpha) )
#print(Nsat(logM[0], logM0, logM1, alpha) )

Integrand1 = n*(Ncent(logM, logMmin, sig) + Nsat(logM, logM0, logM1, alpha)) 

ngaltot = np.trapz(Integrand1, x=logM)

print (ngaltot)

Integrand2 = b*n*(Ncent(logM, logMmin, sig) + Nsat(logM, logM0, logM1, alpha))

bgaltot = (1.0/ngaltot)*np.trapz(Integrand2, x=logM)

print (bgaltot)

Integrand3 = n*(Nsat(logM, logM0, logM1, alpha))

fgaltot = (1.0/ngaltot)*np.trapz(Integrand3, x=logM)

print (fgaltot)
