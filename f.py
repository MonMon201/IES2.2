import math

def fCoef(pk, N):
  arg = 2 * math.pi * pk / N
  return complex(math.cos(arg), -math.sin(arg))

def f(signal):
  N = len(signal)
  if N == 1: return signal
  length = int(N / 2)
  spectre = [None] * N
  evens = f(signal[::2])
  odds = f(signal[1::2])
  for p in range(length):
    w = fCoef(p, N)
    product = odds[p] * w
    spectre[p] = evens[p] + product
    spectre[p + length] = evens[p] - product
  return spectre