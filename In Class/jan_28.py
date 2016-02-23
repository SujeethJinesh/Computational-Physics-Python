from pylab import imshow, show, gray, hot, spectral, bone, hsv, colorbar, xlim, ylim
from numpy import loadtxt

data = loadtxt("circular.txt", float)
#imshow(data)
imshow(data, origin="lower")
#imshow(data, origin = "lower", extent = [0, 10, 0, 5]) #change scale
#imshow(data, origin = "lower", extent = [0, 10, 0, 5], aspect = 2.0) #force it into square
#xlim(2,8)
#ylim(*,*)
#gray()
#bone()
#colorbar()
#show