import numpy as np


def CalcNsat(M, M0, M1, alpha, Asat):
        if (M>M0):
                return Asat*(((10**M) - 10**M0)/10**M1)**alpha
        else:
                return 0.


Nsat = np.vectorize(CalcNsat)

def CalcNcent(M, mu, sig, Acen):
        return Acen/(sig*np.sqrt(np.pi*2.0))*np.exp(-(M - mu)**2/(2.0*sig**2))

Ncent = np.vectorize(CalcNcent)


data = np.genfromtxt("Mn_n_b_Halostest_halfres.txt")
logM = data[:,0]
N = data[:,1]
b = data[:,2]

V = 500**3
n = N/V

alpha = 1.0
sig = 2.0
mu = 12.0
Acen = 1.0
Asat = 0.1
logM0 = mu # If this value is larger than any logM values, this results in negative Nsat vlaues. Or set alpha as an even number.
logM1 = 1 + mu


#print(logM)
#print (n)
#print(Nsat(logM, logM0, logM1, alpha, Asat))
#print(Ncent(logM, mu, sig, Acen))

#def integration(integrand,lower,upper,*args):
#     panels = 100000
#     limits = [lower, upper]
#     h = ( limits[1] - limits[0] ) / (2 * panels)
#     n = (2 * panels) + 1
#     x = np.linspace(limits[0],limits[1],n)
#     y = integrand(x,*args)
#     #Simpson 1/3
#     I = 0
#     start = -2
#     for looper in range(0,panels):
#             start += 2
#             counter = 0
#             for looper in range(start, start+3):
#                     counter += 1
#                     if (counter ==1 or counter == 3):
#                             I += ((h/3) * y[looper])
#                     else:
#                             I += ((h/3) * 4 * y[looper])
#     return I

#def f(x, a, b):
#     return a*np.log(x/b)
 
#integration(f, 3, 4, 2, 5)

Integrand1 = n*(Ncent(logM, mu, sig, Acen) + Nsat(logM, logM0, logM1, alpha, Asat)) 
#print (Integrand1)
ngaltot = np.trapz(Integrand1, x=logM)
#ngaltot = integration(Integrand1, np.min(logM
print (ngaltot)

Integrand2 = b*n*(Ncent(logM, mu, sig, Acen) + Nsat(logM, logM0, logM1, alpha, Asat))

bgaltot = (1.0/ngaltot)*np.trapz(Integrand2, x=logM)

print (bgaltot)

Integrand3 = n*(Nsat(logM, logM0, logM1, alpha, Asat))

fgaltot = (1.0/ngaltot)*np.trapz(Integrand3, x=logM)

print (fgaltot)
