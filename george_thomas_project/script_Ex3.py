import numpy as np
import matplotlib.pyplot as plt

def CalcNsat(M, M0, M1, alpha, Asat):
	Nsat_Mh = Asat*(((10**M) - 10**M0)/10**M1)**alpha
	if (M>M0):
	        return Nsat_Mh
	else:
		return 0.

Nsat = np.vectorize(CalcNsat)

def CalcNcent(M, mu, sig, Acen):
        return Acen/(sig*np.sqrt(np.pi*2.0))*np.exp(-(10**M - 10**mu)**2/(2.0*sig**2))

Ncent = np.vectorize(CalcNcent)

data = np.genfromtxt("Mn_n_b_Halostest_halfres.txt")
logM = data[:,0]
N = data[:,1]
b = data[:,2]
dNdlogMh = np.array([0.0, 0.0, 0.0, 34285952.0, 58398560.0, 7240800.0, -24836608.0, -16693120.0, -14453856.0, -10092608.0, -7813344.0, -6188096.0, -4827488.0, -3658912.0, -2749600.0, -2118784.0, -1637920.0, -1221632.0, -937376.0, -709472.0, -528064.0, -403552.0, -296160.0, -253072.0, -179320.0, -75176.0, -37952.0, -17372.0, -6510.0, -602.0, -8.0])

V = 500**3
n = N/V

Acen = 1.0
sig = 2.0
mu = 12.0
logM0 = mu
alpha = 1.0
logM1 = 1.0 + mu

fsat = np.linspace(0.0, 1.0, num=20, endpoint=False)


#fmeas = np.linspace(0.0, 1.0, num=100, endpoint=False)

#Delta = (f - fmeas)**2

#Dmin = np.min(Delta)

#fchose = fmeas[np.where(Delta == Dmin)]

Nc = Acen*np.trapz(dNdlogMh*Ncent(logM, mu, sig, Acen))

IntegrandA = dNdlogMh*(((10**logM) - 10**logM0)/10**logM1)**alpha 

#Asat = (Nc*(1.0/fsat - 1)**(-1))/np.trapz(IntegrandA)

for fs in fsat:
	Asat = (Nc*(1.0/fsat - 1)**(-1))/np.trapz(IntegrandA)
	print (Asat)



fig = plt.figure(1)
xtit = '${\\rm f_{Sat}}$'
ytit = '${\\rm A_{Sat}}$'
plt.xlabel(xtit)
plt.ylabel(ytit)
plt.plot(fsat, Asat, 'r-')
plt.show(fig)

