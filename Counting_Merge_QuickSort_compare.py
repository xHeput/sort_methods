from numpy import random
from time import perf_counter_ns
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

def count_sort(arr):
    maxy = int(max(arr))
    miny = int(min(arr))
    zasieg = maxy - miny + 1

    # tworzy array dla całego zasiegu (licznik)
    count_arr = [0 for _ in range(zasieg)]
    # tworzy array dla długosci zbioru
    output_arr = [0 for _ in range(len(arr))]

    # zlicza ilosci poszczególnych cyfr dla całosci
    for i in range(0, len(arr)):
        count_arr[arr[i] - miny] += 1

    # dodawanie tej kumultatywnej
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # sortowanie już po kolei wszystko elegancko
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - miny] - 1] = arr[i]
        count_arr[arr[i] - miny] -= 1

    # wklejenie do naszego array zeby to wyswietlic
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr

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
sumar_merge = 0
sumar_Quick = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    count_sort_liczby = liczby
    MergeSort_liczby = liczby
    QuickSort_liczby = liczby
    # CountSort
    start = perf_counter_ns()
    count_sort(count_sort_liczby)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica
    # MergeSort
    start_Merge = perf_counter_ns()
    mergeSort(MergeSort_liczby)
    stop_Merge = perf_counter_ns()
    roznica_merge = stop_Merge - start_Merge
    sumar_merge += roznica_merge

    #QuickSort
    size = len(QuickSort_liczby)
    start_Quick = perf_counter_ns()
    quickSort(QuickSort_liczby, 0, size - 1)
    stop_Quick = perf_counter_ns()
    roznica_Quick = stop_Quick - start_Quick
    sumar_Quick += roznica_Quick

srednia_100_Count = sumar / 100
print("sredni czas itereacji Count Sort dla", x, "elementów to: ", srednia_100_Count)

srednia_100_Merge = sumar_merge / 100
print("sredni czas itereacji Merge Sort dla", x, "elementów to: ", srednia_100_Count)

srednia_100_Quick = sumar_Quick / 100
print("sredni czas itereacji Quick Sort dla", x, "elementów to: ", srednia_100_Count)

x = 500
sumar = 0
sumar_merge = 0
sumar_Quick = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    count_sort_liczby = liczby
    MergeSort_liczby = liczby
    QuickSort_liczby = liczby

    #CountSort
    start = perf_counter_ns()
    count_sort(count_sort_liczby)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

    #MergeSort+
    start_Merge = perf_counter_ns()
    mergeSort(MergeSort_liczby)
    stop_Merge = perf_counter_ns()
    roznica_merge = stop_Merge - start_Merge
    sumar_merge += roznica_merge

    #QuickSort
    size = len(QuickSort_liczby)
    start_Quick = perf_counter_ns()
    quickSort(QuickSort_liczby, 0, size - 1)
    stop_Quick = perf_counter_ns()
    roznica_Quick = stop_Quick - start_Quick
    sumar_Quick += roznica_Quick

srednia_500_Count = sumar / 100
print("sredni czas itereacji Count Sort dla", x, "elementów to: ", srednia_500_Count)

srednia_500_Merge = sumar_merge / 100
print("sredni czas itereacji Merge Sort dla", x, "elementów to: ", srednia_500_Merge)

srednia_500_Quick = sumar_Quick / 100
print("sredni czas itereacji Quick Sort dla", x, "elementów to: ", srednia_500_Quick)


x = 1000
sumar = 0
sumar_merge = 0
sumar_Quick = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    count_sort_liczby = liczby
    MergeSort_liczby = liczby
    QuickSort_liczby = liczby

    #Count Sort
    start = perf_counter_ns()
    count_sort(count_sort_liczby)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

    #MergeSort
    start_Merge = perf_counter_ns()
    mergeSort(MergeSort_liczby)
    stop_Merge = perf_counter_ns()
    roznica_merge = stop_Merge - start_Merge
    sumar_merge += roznica_merge

    #QuickSort
    size = len(QuickSort_liczby)
    start_Quick = perf_counter_ns()
    quickSort(QuickSort_liczby, 0, size - 1)
    stop_Quick = perf_counter_ns()
    roznica_Quick = stop_Quick - start_Quick
    sumar_Quick += roznica_Quick

srednia_1000_Count = sumar / 100
print("sredni czas itereacji Count Sort dla", x, "elementów to: ", srednia_1000_Count)

srednia_1000_Merge = sumar_merge / 100
print("sredni czas itereacji Merge Sort dla", x, "elementów to: ", srednia_1000_Merge)

srednia_1000_Quick = sumar_Quick / 100
print("sredni czas itereacji Quick Sort dla", x, "elementów to: ", srednia_1000_Quick)


x = 5000
sumar = 0
sumar_merge = 0
sumar_Quick = 0
for lp in range(100):
    liczby = random.randint(0, 5000, size=x)
    count_sort_liczby = liczby
    MergeSort_liczby = liczby
    QuickSort_liczby = liczby

    #CountSort
    start = perf_counter_ns()
    count_sort(count_sort_liczby)
    stop = perf_counter_ns()
    # print("Wygenerowanie liczb zaczeło się: ", start, "Skończyło się: ", stop,)
    # print("Całosc trwała: ", stop-start, "ns")
    roznica = stop - start
    sumar += roznica

    #MergeSort
    start_Merge = perf_counter_ns()
    mergeSort(MergeSort_liczby)
    stop_Merge = perf_counter_ns()
    roznica_merge = stop_Merge - start_Merge
    sumar_merge += roznica_merge

    #QuickSort
    size = len(QuickSort_liczby)
    start_Quick = perf_counter_ns()
    quickSort(QuickSort_liczby, 0, size - 1)
    stop_Quick = perf_counter_ns()
    roznica_Quick = stop_Quick - start_Quick
    sumar_Quick += roznica_Quick

srednia_5000_Count = sumar / 100
print("sredni czas itereacji Count Sort dla", x, "elementów to: ", srednia_5000_Count)

srednia_5000_Merge = sumar_merge / 100
print("sredni czas itereacji Merge Sort dla", x, "elementów to: ", srednia_5000_Merge)

srednia_5000_Quick = sumar_Quick / 100
print("sredni czas itereacji Quick Sort dla", x, "elementów to: ", srednia_5000_Quick)


srednia = [srednia_100_Count, srednia_500_Count, srednia_1000_Count, srednia_5000_Count]
XD = [100, 500, 1000, 5000]
plt.plot(XD, srednia, color="r")
srednia_Merge = [srednia_100_Merge, srednia_500_Merge, srednia_1000_Merge, srednia_5000_Merge]
plt.plot(XD, srednia_Merge, color="g")
srednia_Quick = [srednia_100_Quick, srednia_500_Quick, srednia_1000_Quick, srednia_5000_Quick]
plt.plot(XD, srednia_Quick, color="b")
plt.ylabel("Czas w nanosekundach")
plt.xlabel("ilość losowań")
plt.title("Czas obliczeń poszczególnych sortowań")
plt.show()