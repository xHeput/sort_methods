from numpy import random
from time import perf_counter_ns
import matplotlib.pyplot as plt


# BubbleSort
def BubbleSort(macierz):
    for i in range(len(macierz)):

        for j in range(0, len(macierz) - i - 1):

            if macierz[j] > macierz[j + 1]:
                container = macierz[j]
                macierz[j] = macierz[j + 1]
                macierz[j + 1] = container


x = 100
sumar = 0
for lp in range(100):
    liczby = random.randint(-5000, 5000, size=x)
    start = perf_counter_ns()
    BubbleSort(liczby)
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
    liczby = random.randint(-5000, 5000, size=x)
    start = perf_counter_ns()
    BubbleSort(liczby)
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
    liczby = random.randint(-5000, 5000, size=x)
    start = perf_counter_ns()
    BubbleSort(liczby)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

srednia_1000 = sumar / 100
print("sredni czas itereacji", x, "elementów to: ", srednia_1000)
# Use only when you have lots of time
# x = 5000
# sumar = 0
# for lp in range(100):
    # liczby = random.randint(-5000, 5000, size=x)
    # start = perf_counter_ns()
    # BubbleSort(liczby)
    # stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    # roznica = stop - start
    # sumar += roznica

# srednia_5000 = sumar / 100
# print("sredni czas itereacji", x, "elementów to: ", srednia_5000)

srednia = [srednia_100, srednia_500, srednia_1000]#, srednia_5000]
XD = [100, 500, 1000]#, 5000]
plt.plot(srednia, XD)
plt.xlabel("Czas w nanosekundach")
plt.ylabel("ilość losowań")
plt.title("Czas obliczeń poszczególnych sortowań z wykorzystaniem algorytmu Bubble Sort")
plt.show()
