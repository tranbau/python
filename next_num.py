import numpy as np
import  time
from collections import Counter

st =  time.time() #start time
f = open("num.txt", "r")
num = f.read().splitlines()
N = len(num)
s = ""
for x in num:
    s += x
numbers = np.array(list(s))
numbers = np.reshape( numbers, (N, 9)) #create matrix
#print(numbers.shape)

next_number = ""
for i in range(9):
    col = np.array(numbers[:, i]) #each column
    next_number += Counter(col.flat).most_common(1)[0][0]

print(next_number)
et = time.time() #end time
print("--- %s seconds ---" % (et - st))



