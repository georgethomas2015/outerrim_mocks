import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import sys
import scipy.integrate as integrate
import time

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

# Reading line-by-line
start2 = time.time()
# Count the lines in the file
ff = open('/mnt/lustre/eboss/OuterRim/OuterRim_sim/ascii/OuterRim_STEP266_z0.865/subvols27/OuterRim_STEP266_fofproperties_000.txt')
num = 0

for line in ff:
        num += 1

ff.close()

print(num, ' lines in ', '/mnt/lustre/eboss/OuterRim/OuterRim_sim/ascii/OuterRim_STEP266_z0.865/subvols27/OuterRim_STEP266_fofproperties_000.txt')

ff = open('/mnt/lustre/eboss/OuterRim/OuterRim_sim/ascii/OuterRim_STEP266_z0.865/subvols27/OuterRim_STEP266_fofproperties_000.txt')

for line in ff:
        xx = float(line.split()[0])
        yy = float(line.split()[1])
        zz = float(line.split()[2])
#       print (xx, yy, zz)
ff.close()

end2 = time.time()
time2 = end2 - start2

# Reading the whole file.
start1 = time.time()
data1 = np.genfromtxt("/mnt/lustre/eboss/OuterRim/OuterRim_sim/ascii/OuterRim_STEP266_z0.865/subvols27/OuterRim_STEP266_fofproperties_000.txt", usecols=(6))
end1 = time.time()
time1 = end1 - start1
#data2 = np.genfromtxt("Testbox2.txt")
#data3 = np.genfromtxt("Testbox3.txt")
#print (logM1, logM2, logM3)

print (time2/time1)

sys.exit()

logMmin = 8.0
logMmax = 16.0
dlogM = 0.1

mbins = np.arange(logMmin,logMmax,dlogM)
mhist = mbins + dlogM*0.5
mminedge = mbins
mmaxedge = mbins + dlogM

H, bins_edges = np.histogram(logM, bins=np.append(mbins, logMmax))

#print (len(mbins), len(mhist), len(H), H)
dNhdlogMh = H

Acen = 2.0
sig = 0.12
mu = 12.0


ncen = Ncent(mhist, mu, sig, Acen)
#print (ncen)

#sys.exit()

path2plot = "/users/ghthomas/output_plots/"
plotname = "Littlebox_test.png"
fig = plt.figure(figsize = (8., 9.))
xtit = '${\\rm logM_{h}}$'
ytit = '${\\rm \\frac{dN}{dlogM_{h}}}$'
plt.xlabel(xtit)
plt.ylabel(ytit)
#plt.ylim([-5, 1])
plt.plot(mhist, np.log10(H), linewidth=3, label='Testbox 1')
#plt.plot(mhist, np.log10(ncen), linewidth=3)
leg = plt.legend(loc=1)
leg.draw_frame(False)
plt.show()
fig.savefig(path2plot + plotname)
print ('Ouput: ', path2plot + plotname)
