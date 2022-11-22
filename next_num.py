import numpy as np
import  time
from collections import Counter
import matplotlib.pyplot as plt
np.random.seed(1)
st =  time.time() #start time
f = open("num.txt", "r")
num = f.read().splitlines()
N = len(num)
s = ""
for x in num:
    s += x
#100-0,004, 1000-0,03, 10000-0,3 100000-5 (s)
#duplicate
more = 100 - N
N = N + more
dupl = np.random.randint( 100000000, 999999999, size = more)
for x in dupl:
    s += str(x)

numbers = np.array(list(s))
numbers = np.reshape( numbers, (N, 9)) #crate matrix
#print(numbers.shape)
next_number = ""
fig, list_pos = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True)
list_pos = list_pos.flatten()
fig.suptitle('Most frequent digits')
fig.tight_layout(pad=2.0)

for i in range(9):
    col = np.array(numbers[:, i]) #each column
    count = Counter(sorted(col.flat))
    list_pos[i].bar(count.keys(), count.values())
    list_pos[i].title.set_text( str(i) + 'th pos')
    next_number += count.most_common(1)[0][0]
print(next_number)
plt.show()
et = time.time() #end time
print("--- %s seconds ---" % (et - st))











