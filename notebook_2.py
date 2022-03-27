# -*- coding: utf-8 -*-
"""Notebook_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoQawciJlYcEesi1zwWLYBfgQdUujAlc
"""

'Sorting'
def selection_sort(arr):
  size = len(arr)
  for row in range(size - 1):
    min_index = row
    for col in range(min_index + 1, size):
      if arr[col] < arr[min_index]:
        min_index = col
    if row != min_index:
      arr[row], arr[min_index] = arr[min_index], arr[row]

lst = []
i = 5
while i > 0:
  a = int(input().__str__())
  lst.append(a)
  i -= 1


elements = lst
selection_sort(elements)
num = len(elements) - 1
while num >= 0:
  print(elements[num])
  num -= 1