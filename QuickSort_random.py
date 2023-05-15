from numpy import random
from time import perf_counter_ns
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
# Quick sort

def partition(array, low, high):

  # wybieranie pivota
  pivot = array[high]

  # pointer for greater element
  i = low - 1


  # porównanie każdej liczby z pivotem
  for j in range(low, high):
    if array[j] <= pivot:
      # to co mniejsze niż pivot zamień za element i
      i = i + 1

      # zamiana
      (array[i], array[j]) = (array[j], array[i])

  # zamiana pivota
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    #znajdowanie pivota
    pi = partition(array, low, high)

    # szukanie na lewo od piwota
    quickSort(array, low, pi - 1)

    # szukanie na prawo od piwota
    quickSort(array, pi + 1, high)


x = 100
sumar = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    size=len(liczby)
    start = perf_counter_ns()
    quickSort(liczby, 0, size - 1)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

srednia_100 = sumar / 100
print("sredni czas itereacji", x, "elementów to: ", srednia_100)

x = 500
sumar = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    size=len(liczby)
    start = perf_counter_ns()
    quickSort(liczby, 0, size - 1)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

srednia_500 = sumar / 100
print("sredni czas itereacji", x, "elementów to: ", srednia_500)

x = 1000
sumar = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    size=len(liczby)
    start = perf_counter_ns()
    quickSort(liczby, 0, size - 1)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

srednia_1000 = sumar / 100
print("sredni czas itereacji", x, "elementów to: ", srednia_1000)

x = 5000
sumar = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    size=len(liczby)
    start = perf_counter_ns()
    quickSort(liczby, 0, size - 1)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

srednia_5000 = sumar / 100
print("sredni czas itereacji", x, "elementów to: ", srednia_5000)

x = 100
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_optymistyczne_100 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_100)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_pesymistyczna_100 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_100)

x = 500
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_optymistyczne_500 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_500)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_pesymistyczna_500 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_500)

x = 1000
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_optymistyczne_1000 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_1000)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_pesymistyczna_1000 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_1000)

x = 5000
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_optymistyczne_5000 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_5000)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
size=len(liczby)
start = perf_counter_ns()
quickSort(liczby, 0, size - 1)
stop = perf_counter_ns()
roznica_pesymistyczna_5000 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_5000)

srednia = [srednia_100, srednia_500, srednia_1000, srednia_5000]
XD = [100, 500, 1000, 5000]
plt.plot(XD, srednia, color="r")
roznice_opt = [roznica_optymistyczne_100, roznica_optymistyczne_500, roznica_optymistyczne_1000,
               roznica_optymistyczne_5000]
plt.plot(XD, roznice_opt, color="g")
roznice_pes = [roznica_pesymistyczna_100, roznica_pesymistyczna_500, roznica_pesymistyczna_1000,
               roznica_pesymistyczna_5000]
plt.plot(XD, roznice_pes, color="b")
plt.ylabel("Czas w nanosekundach")
plt.xlabel("ilość losowań")
plt.title("Czas obliczeń poszczególnych sortowań z wykorzystaniem algorytmu Quick Sort")
plt.show()
