import matplotlib.pyplot as plot             #importing all necessary things
import numpy as np

(timeGWH1, H1) = np.loadtxt('GWH1.dat', float)
(timeGWL1, L1) = np.loadtxt('GWL1.dat', float)  #loading in information from .dat files
(timeNR, NR) = np.loadtxt('NR.dat', float)      #and assigning them into variables
(freqL1, ASL1) = np.loadtxt('ASDL1.dat', float)
(freqH1, ASH1) = np.loadtxt('ASDH1.dat', float)


newNR = np.concatenate([np.zeros(len(H1) - len(NR)), NR])
#newNRTime = np.concatenate([timeNR, np.zeros(len(H1) - len(NR))]) #adding zeros

def partA():                                #graph for part 1
    plot.ylim(-1.5e-21, 1.5e-21)
    plot.xlim(-0.2, 0.1)
    plot.plot(timeGWH1, H1, label = 'H1')
    plot.plot(timeGWL1, L1, label = 'L1')                 # plotting all the time vs height from files
    plot.plot(timeNR, NR/10.0)
    plot.xlabel('Time')
    plot.ylabel('Height')
    plot.title('H1 and L1 graphs')
    plot.legend(loc='best')
    plot.show() #displaying plot

def partB():                                  #graph for part 2
    plot.xlim(30, 1000)
    fftH1 = np.fft.fft(H1)
    fftL1 = np.fft.fft(L1)
    fftNR = np.fft.fft(newNR)
    fftNRfreq = np.fft.fftfreq(len(fftNR), d=(timeNR[1] - timeNR[0]))

    plot.loglog(fftNRfreq, np.abs(fftH1), label = 'H1')
    plot.loglog(fftNRfreq, np.abs(fftL1), label = 'L1')                # plotting all the time vs height from files
    plot.loglog(fftNRfreq, np.abs(fftNR), label = 'NR')
    plot.loglog(freqH1, ASH1)
    plot.loglog(freqL1, ASL1)
    plot.legend(loc='best')
    plot.title('FFTs of LIGO Data')
    plot.xlabel('Frequencies')
    plot.ylabel('Height')
    plot.show()                             #displaying plot