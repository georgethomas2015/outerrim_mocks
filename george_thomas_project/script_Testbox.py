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

# Reading the whole file
start1 = time.time()
data1 = np.genfromtxt("Testbox1.txt", usecols=(6))
end1 = time.time()
time1 = end1 - start1
data2 = np.genfromtxt("Testbox2.txt", usecols=(6))
data3 = np.genfromtxt("Testbox3.txt", usecols=(6))
#print (logM1, logM2, logM3)


# Reading line-by-line
start2 = time.time()
# Count the lines in the file
ff = open('Testbox1.txt')
num = 0

for line in ff:
        num += 1

ff.close()

print(num, ' lines in ', 'Testbox1.txt')

# Downsample to plot
sampling_rate = 0.001

if num>10000000:
        sampling_rate = 0.0001

xp, yp, zp = [np.empty((0,1), float) for i in range(3)]
ff = open('Testbox1.txt')

for line in ff:
        xx = float(line.split()[0])
        yy = float(line.split()[1])
        zz = float(line.split()[2])
#       print (xx, yy, zz)
ff.close()

end2 = time.time()
time2 = end2 - start2
print (time2/time1)

sys.exit()

logMmin = 8.0
logMmax = 16.0
dlogM = 0.1

mbins = np.arange(logMmin,logMmax,dlogM)
mhist = mbins + dlogM*0.5

H1, bins_edges1 = np.histogram(logM1, bins=np.append(mbins, logMmax))
H2, bins_edges2 = np.histogram(logM2, bins=np.append(mbins, logMmax))
H3, bins_edges3 = np.histogram(logM3, bins=np.append(mbins, logMmax))

#print (len(mbins), len(mhist), len(H), H)
dNhdlogMh1 = H1
dNhdlogMh2 = H2
dNhdlogMh3 = H3
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
#plt.plot(mhist, H1, linewidth=3, label='Testbox 1')
#plt.plot(mhist, H2, linewidth=3, label='Testbox 2')
#plt.plot(mhist, H3, linewidth=3, label='Testbox 3')
plt.plot(mhist, np.log10(H1), linewidth=3, label='Testbox 1')
plt.plot(mhist, np.log10(H2), linewidth=3, label='Testbox 2')
plt.plot(mhist, np.log10(H3), linewidth=3, label='Testbox 3')
#plt.plot(mhist, np.log10(ncen), linewidth=3)
leg = plt.legend(loc=1)
leg.draw_frame(False)
plt.show()
fig.savefig(path2plot + plotname)
print ('Ouput: ', path2plot + plotname)
