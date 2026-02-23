# n = 58735
# c=0
# num = n
# while num>0:
#     num = num//10
#     c+=1

# print("No of digits:",c)

from math import *
def countD(num):
    return int(log10(num)+1)

c = countD(654323)
print(c)