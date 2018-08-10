import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import sys
import scipy.integrate as integrate
from scipy.special import erf

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

def CalcNsat2(M, M0, M1, alpha):
	if (M*alpha>M0*alpha):
		return (((10**M) - 10**M0)/10**M1)**alpha
	else:
		return 0.

Nsat2 = np.vectorize(CalcNsat2)

def CalcNcent2(M, Mmin, sig):
	return 0.5*( 1 + erf((M - Mmin)/sig))

Ncent2 = np.vectorize(CalcNcent2)

#Input variables
V = 200**3

data = np.genfromtxt("/mnt/lustre/eboss/OuterRim/OuterRim_sim/ascii/vol200Mpc/OuterRim_STEP266_z0.865/OuterRim_STEP266_fofproperties_200Mpc.txt")
M = data[:,2] #Halo masses
logM = np.log10(M)

logMmin = 8.0 #Minimum log(mass)
logMmax = 16.0 #Maximum log(mass)
dlogM = 0.1 #Histogram bin width

Acen = 1.0
sig = 0.12
mu = 12.0

logM0 = mu
alpha = 0.8
logM1 = 1.0 + mu
logMmin2 = 12.8

fsat = 0.05

mbins = np.arange(logMmin,logMmax,dlogM) #Creates the bins
mhist = mbins + dlogM*0.5 #Defines the middle of each bin

H, bins_edges = np.histogram(logM, bins=np.append(mbins, logMmax)) #Creates a histogram, used to define dNh/dlogMh
dNhdlogMh = H

ncen = Ncent(mhist, mu, sig, Acen)
ncen2 = Ncent2(mhist, logMmin2, sig)

#Asat calculation
Integrand = dNhdlogMh*ncen
Ncentot = Acen*integrate.simps(Integrand, mhist)
Denominator = integrate.simps(dNhdlogMh*dlogM*MExpr(mhist, logM0, logM1, alpha), mhist)
Numerator = Ncentot*(1.0/fsat - 1)**(-1)
Asat = Numerator/Denominator
print ('Asat=', Asat)

fsatspec = np.array([0.05, 0.10, 0.15, 0.20, 0.25])

#For multiple fsat values
fsat2 =np.linspace(0.0, 1.0, num=20, endpoint=False)
Numerator2 = Ncentot*(1.0/fsat2 - 1)**(-1)
Asat2 = Numerator2/Denominator

doplot1 = False
doplot2 = False
doplot3 = True

#LogM vs LogNcen plot
if doplot1:
	path2plot = "/users/ghthomas/output_plots/"
	plotname = "Ex3.1_200Mpc.png"
	fig = plt.figure(figsize = (8., 9.))
	xtit = '${\\rm logM_{h}}$'
	ytit = '${\\rm logN_{h}}$'
	plt.xlabel(xtit)
	plt.ylabel(ytit)
	plt.ylim([-5, 6])
	plt.rc('xtick', labelsize=10)
	plt.plot(mhist, np.log10(H), linewidth=3)
	plt.plot(mhist, np.log10(ncen), linewidth=3)
	plt.show()
	fig.savefig(path2plot + plotname)
	print ('Ouput: ', path2plot + plotname)


#Asat vs fsat plot
if doplot2:
	path2plot = "/users/ghthomas/output_plots/"
	plotname = "Asat vs fsat graph_200Mpc.png"
	fig = plt.figure(figsize = (8., 9.))
	xtit = '${\\rm f_{Sat}}$'
	ytit = '${\\rm A_{Sat}}$'
	plt.xlabel(xtit)
	plt.ylabel(ytit)
	plt.rc('xtick', labelsize=10)
	plt.plot(fsat2, Asat2, 'r-')
	plt.show()
	fig.savefig(path2plot + plotname)
	print ('Ouput: ', path2plot + plotname)


#Ncen and Nsat plot
if doplot3:
	path2plot = "/users/ghthomas/output_plots/"
	plotname = "logMh vs logNcen and logNsat_200Mpc.png"
	fig = plt.figure(figsize = (8., 9.))
	xtit = '${\\rm logM_{h}}$'
	ytit = '${\\rm logN}$'
	plt.xlabel(xtit)
	plt.ylabel(ytit)
	plt.xlim([11, 16.5])
	plt.ylim([-1, 6])
	plt.plot(mhist, np.log10(ncen), label='${\\rm N_{cen}}$')

	for f in fsatspec:
		Numeratorspec = Ncentot*(1.0/f - 1)**(-1)
		Asatspec = Numeratorspec/Denominator
		plt.plot(mhist, np.log10(Nsat(mhist, logM0, logM1, alpha, Asatspec)), label='$N_{sat}, f_{sat}=$' + str(f))	

	plt.plot(mhist, np.log10(ncen2), '--',label='${\\rm N_{cen}, 5pHOD}$')
	plt.plot(mhist, np.log10(Nsat2(mhist, logM0, logM1, alpha)), '--',label='${\\rm N_{sat}, 5pHOD}$')
	leg = plt.legend(loc=1)
	leg.draw_frame(False)
	plt.show()
	fig.savefig(path2plot + plotname)
	print ('Ouput: ', path2plot + plotname)
