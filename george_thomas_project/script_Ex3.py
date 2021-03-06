import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import sys
import scipy.integrate as integrate

def CalcNsat(M, M0, M1, alpha, Asat):
	Nsat_Mh = Asat*(((10**M) - 10**M0)/10**M1)**alpha
	if (M>M0):
	        return Nsat_Mh
	else:
		return 0.

Nsat = np.vectorize(CalcNsat)

def CalcNcent(M, mu, sig, Acen):
        return Acen/(sig*np.sqrt(np.pi*2.0))*np.exp(-(M - mu)**2/(2.0*sig**2))

Ncent = np.vectorize(CalcNcent)

def CalcMExpr(M, M0, M1, alpha):
	if (M>M0):
		return (((10**M) - 10**M0)/10**M1)**alpha
	else:
		return 0.

MExpr = np.vectorize(CalcMExpr)

#Test
#data = np.genfromtxt("Mn_n_b_Halostest_halfres.txt")
#logM = data[:,0]
#N = data[:,1]
#b = data[:,2]
#print (logM, len(logM))

#logMmin = 8.0
#logMmax = 16.0
#dlogM = 0.1

#mbins = np.arange(logMmin,logMmax,dlogM)
#mhist = mbins + dlogM*0.5

#H, bins_edges = np.histogram(logM, bins=np.append(mbins, logMmax))
#print (len(mbins), len(mhist), len(H), H)
#dNhdlogMh = H

#Acen = 1.0
#sig = 0.12
#mu = 12.0
#ncen = np.zeros(len(mhist))
 

#for i in enumerate(mhist):
#	ncen[i] = Ncent(i, mu, sig, Acen)
#ncen = Ncent(mhist, mu, sig, Acen)
#print (ncen)
#Nc = Acen*np.trapz(dNhdlogMh*Ncent(logM, mu, sig, Acen))

#path2plot = "/users/ghthomas/output_plots/"
#plotname = "Ex3.1_test.png"
#fig = plt.figure(figsize = (8., 9.))
#xtit = '${\\rm logM_{h}}$'
#ytit = '${\\rm logN_{h}}$'
#plt.xlabel(xtit)
#plt.ylabel(ytit)
#plt.ylim([-5, 1])
#plt.plot(mhist, np.log10(H), linewidth=3)
#plt.plot(mhist, np.log10(ncen), linewidth=3)
#plt.show()
#fig.savefig(path2plot + plotname)
#print ('Ouput: ', path2plot + plotname)

#OuterRim 200Mpc
data = np.genfromtxt("/mnt/lustre/eboss/OuterRim/OuterRim_sim/ascii/vol200Mpc/OuterRim_STEP266_z0.865/OuterRim_STEP266_fofproperties_200Mpc.txt")
M = data[:,2]
logM = np.log10(M)
#print (logM, len(logM))

logMmin = 8.0
logMmax = 16.0
dlogM = 0.1

mbins = np.arange(logMmin,logMmax,dlogM)
mhist = mbins + dlogM*0.5

H, bins_edges = np.histogram(logM, bins=np.append(mbins, logMmax))
#print (len(mbins), len(mhist), len(H), H)
dNhdlogMh = H

Acen = 1.0
sig = 0.12
mu = 12.0
ncen = Ncent(mhist, mu, sig, Acen)

#path2plot = "/users/ghthomas/output_plots/"
#plotname = "Ex3.1_200Mpc.png"
#fig = plt.figure(figsize = (8., 9.))
#xtit = '${\\rm logM_{h}}$'
#ytit = '${\\rm logN_{h}}$'
#plt.xlabel(xtit)
#plt.ylabel(ytit)
#plt.ylim([-5, 6])
#plt.rc('xtick', labelsize=10)
#plt.plot(mhist, np.log10(H), linewidth=3)
#plt.plot(mhist, np.log10(ncen), linewidth=3)
#plt.show()
#fig.savefig(path2plot + plotname)
#print ('Ouput: ', path2plot + plotname)

#sys.exit()

V = 200**3
#n = N/V

logM0 = mu
alpha = 0.8
logM1 = 1.0 + mu

fsat = np.linspace(0.0, 1.0, num=20, endpoint=False)

#print (MExpr(mhist, logM0, logM1, alpha))

#fmeas = np.linspace(0.0, 1.0, num=100, endpoint=False)

#Delta = (f - fmeas)**2

#Dmin = np.min(Delta)

#fchose = fmeas[np.where(Delta == Dmin)]

#Nc = Acen*np.trapz(dNdlogMh*Ncent(logM, mu, sig, Acen))

Integrand = dNhdlogMh*ncen
#Ncentot = Acen*np.trapz(Integrand, x=mhist)
Ncentot = Acen*integrate.simps(Integrand, mhist)
#Denominator = np.trapz(dNhdlogMh*dlogM*MExpr(mhist, logM0, logM1, alpha), mhist)
Denominator = integrate.simps(dNhdlogMh*dlogM*MExpr(mhist, logM0, logM1, alpha), mhist)
Numerator = Ncentot*(1.0/fsat - 1)**(-1)
Asat = Numerator/Denominator
#print (Asat)
#for fs in fsat:
#	Asat = (Nc*(1.0/fsat - 1)**(-1))/np.trapz(IntegrandA)
#	print (Asat)

#sys.exit()

#Asat vs fsat plot
#path2plot = "/users/ghthomas/output_plots/"
#plotname = "Asat vs fsat graph_test.png"
#plotname = "Asat vs fsat graph_200Mpc.png"
#fig = plt.figure(figsize = (8., 9.))
#xtit = '${\\rm f_{Sat}}$'
#ytit = '${\\rm A_{Sat}}$'
#plt.xlabel(xtit)
#plt.ylabel(ytit)
#plt.rc('xtick', labelsize=10)
#plt.plot(fsat, Asat, 'r-')
#plt.show()
#fig.savefig(path2plot + plotname)
#print ('Ouput: ', path2plot + plotname)

fsatspec = np.array([fsat[1], fsat[2], fsat[3], fsat[4], fsat[5]])

#Ncen and Nsat plot
path2plot = "/users/ghthomas/output_plots/"
#plotname = "logMh vs logNcen and logNsat_test.png"
plotname = "logMh vs logNcen and logNsat_200Mpc.png"
fig = plt.figure(figsize = (8., 9.))
xtit = '${\\rm logM_{h}}$'
ytit = '${\\rm logN}$'
plt.xlabel(xtit)
plt.ylabel(ytit)
#plt.ylim([-3, 5])
plt.ylim([-1, 5])
plt.plot(mhist, np.log10(ncen), label='${\\rm N_{cen}}$')

for f in fsatspec:
	Numeratorspec = Ncentot*(1.0/f - 1)**(-1)
	Asatspec = Numeratorspec/Denominator
	plt.plot(mhist, np.log10(Nsat(mhist, logM0, logM1, alpha, Asatspec)), label='$N_{sat}, f_{sat}=$' + str(f))	

leg = plt.legend(loc=1)
leg.draw_frame(False)
plt.show()
fig.savefig(path2plot + plotname)
print ('Ouput: ', path2plot + plotname)
