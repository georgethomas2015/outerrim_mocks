import numpy as np
import scipy.integrate as integrate

# Bins
edges = np.array([10.3, 10.7, 10.8, 10.9, 11., 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12., 12.1, 12.2, 12.3, 12.4, 12.5, 12.7, 13., 13.5, 14., 15., 16., 17.])
mhist = np.array([10.5, 10.75, 10.85, 10.95, 11.05, 11.15, 11.25, 11.35, 11.45, 11.55, 11.65, 11.75, 11.85, 11.95, 12.05, 12.15, 12.25, 12.35, 12.45, 12.6, 12.85, 13.25, 13.75, 14.5, 15.5, 16.5])
dm = edges[1:]-edges[:-1]

y = np.zeros(len(mhist))
y.fill(1.0)

mass = np.zeros(len(mhist))
mass[:] = mhist

print (mass)


result = np.trapz(mass, mass)
result2 = integrate.simps(mass, mass)

print (result, result2)

sys.exit()
# Reading line-by-line (is this needed for this testfile?)
start2 = time.time()
# Count the lines in the file
ff = open('Testbox1.txt')
num = 0

for line in ff:
        num += 1

ff.close()

print(num, ' lines in ', 'Testbox1.txt')


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

