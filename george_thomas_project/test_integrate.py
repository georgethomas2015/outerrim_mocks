import scipy.integrate as integrate
import numpy as np

logMmin = 8.0
logMmax = 16.0
dlogM = 0.1

mbins = np.linspace(logMmin,logMmax, num=(logMmax - logMmin)/dlogM)
mhist = mbins + dlogM*0.5

y = np.zeros(len(mhist))
y.fill(1.0)

#result = integrate.quad(lambda x: y, logMmin, logMmax)

#print (result)

#def y(x):
#	return x**2

#result = integrate.simps(y(mbins), mbins)

#print (result)

a = np.array([1, 2, 3])

b = np.array([1, 4, 9])

result = integrate.simps(b, a)

#result2 = integrate.simps(y(a), a)
#This integral becomes inaccurate for polynomials of order 4 or greater.
print (result)
