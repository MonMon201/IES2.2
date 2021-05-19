import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg
import f
import additionalTask as at

n = 12
W = 2400
N = 1024
time = range(N)
signal = rsg.getRandomSignal(n, W, N)

s = f.f(signal)
my, nump = at.compareTime(n, W, N)
print("my fft: ", my, ", numpy fft: ", nump)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Lab 2.2')

ax1.plot(signal, linewidth=0.8)
ax1.set_title('Generated signal')
ax1.set(xlabel='time', ylabel='generated signal')

ax2.plot(s, color='r', linewidth=0.8)
ax2.set_title('Fast Fourier transform')
ax2.set(xlabel='p', ylabel='F(p)')

fig.savefig("lab2.2.png")

plt.show()