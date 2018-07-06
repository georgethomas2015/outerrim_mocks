import numpy as np
import matplotlib.pyplot as plt

def CalcNsat(M, M0, M1, alpha, Asat):
	Nsat_Mh = 0.
        if (M>M0):
                Nsat_Mh =  Asat*(((10**M) - 10**M0)/10**M1)**alpha
	return Nsat_Mh
  

def CalcNcent(M, mu, sig, Acen):
	return Acen/(sig*np.sqrt(np.pi*2.0))*np.exp(-(10**M - 10**mu)**2/(2.0*sig**2))

Nsat = np.vectorize(CalcNsat)
Ncent = np.vectorize(CalcNcent)

data = np.genfromtxt("/users/ghthomas/outerrim_mocks/george_thomas_project/Mn_n_b_Halostest_halfres.txt")
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
logM0 = mu
logM1 = 1 + mu

#print (Nsat(logM, logM0, logM1, alpha, Asat))
#print (Ncent(logM, mu, sig, Acen))

Nsat = np.vectorize(CalcNsat)

fig = plt.figure(1)
xtit = '${\\rm M_{h}}$'
ytit = '${\\rm <N_{Sat}>}$'
plt.xlabel(xtit)
plt.ylabel(ytit)
plt.plot(10**logM, (Nsat(logM, logM0, logM1, alpha, Asat)), 'r-')
plt.show(fig)

fig = plt.figure(2)
xtit = '${\\rm logM_{h}}$'
ytit = '${\\rm <N_{Cen}>}$'
plt.xlabel(xtit)
plt.ylabel(ytit)
plt.plot(logM, (Ncent(logM, mu, sig, Acen)), 'r-')
plt.show(fig)
