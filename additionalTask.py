import numpy as np
import time
import rsg
import f

def compareTime(n, W, N):
    my = 0.0
    nump = 0.0
    for i in range(10):
        s = rsg.getRandomSignal(n, W, N)
        start = time.perf_counter()
        f.f(s)
        stop = time.perf_counter()
        my += (stop-start)
        start = time.perf_counter()
        np.fft.fft(s)
        stop = time.perf_counter()
        nump += (stop-start)
    return my, nump
