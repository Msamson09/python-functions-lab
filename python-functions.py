#1

def sum_to (n):
  total = 0
  for i in range(1, n + 1, 1):
    total += i
  return total


#2

def largest (list):
  list.sort()
  return list[-1]

#3

def occurances (string1, string2):
  return string1.count(string2)

#4

def product (*args):
  product = 1
  for arg in args:
    product *= arg
  return product