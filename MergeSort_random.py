from numpy import random
from time import perf_counter_ns
import matplotlib.pyplot as plt

# MergeSort


def mergeSort(array):
    if len(array) > 1:

        #  dzielenie na 2 arraye
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # sortowanie połówek
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        #porównanie L i M i wsadzanie mniejszego do array
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1


        # po skończonym cyklu wsadz liczby z L i M do reszty miejsc w array
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1



def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


x = 100
sumar = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    start = perf_counter_ns()
    mergeSort(liczby)
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
    start = perf_counter_ns()
    mergeSort(liczby)
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
    start = perf_counter_ns()
    mergeSort(liczby)
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
    start = perf_counter_ns()
    mergeSort(liczby)
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
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_optymistyczne_100 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_100)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_pesymistyczna_100 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_100)

x = 500
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_optymistyczne_500 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_500)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_pesymistyczna_500 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_500)

x = 1000
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_optymistyczne_1000 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_1000)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_pesymistyczna_1000 = stop - start
print("sredni czas itereacji pesymistycznej", x, "elementów to: ", roznica_pesymistyczna_1000)

x = 5000
# optymizm
liczby = sorted(random.randint(0, 5000, size=x))
start = perf_counter_ns()
mergeSort(liczby)
stop = perf_counter_ns()
roznica_optymistyczne_5000 = stop - start
print("sredni czas itereacji optymistycznej", x, "elementów to: ", roznica_optymistyczne_5000)
# pesymizm
liczby = sorted(random.randint(0, 5000, size=x), reverse=True)
start = perf_counter_ns()
mergeSort(liczby)
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
plt.title("Czas obliczeń poszczególnych sortowań z wykorzystaniem algorytmu Merge Sort")
plt.show()
