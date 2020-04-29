import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 100.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
T = np.arange(0, 1, Ts)
X = np.arange(0, 1, Ts)
Y = np.arange(0, 1, Ts)
Z = np.arange(0, 1, Ts)


serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)
for x in range(0, int(Fs)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    X[x] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    Y[x] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    Z[x] = float(line) #for x in range(0, int (Fs)):


fig, ax = plt.subplots(2, 1)

ax[0].plot(T, X, color = "red", linestyle = "-", label = "x")
ax[0].plot(T, Y, color = "blue", linestyle = "-", label = "y")
ax[0].plot(T, Z, color = "green", linestyle = "-", label = "z")
ax[0].legend(loc = 'upper left', frameon = False)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')




plt.show()
s.close()

