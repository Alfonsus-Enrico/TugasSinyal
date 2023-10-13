import numpy as np

#Define Array
array1 = [0,1,2,3]
array2 = [0,1,2,3,4,5,6]

m = len(array1)
n = len(array2)

#Tentukan panjang array
length = m+n-1
conv = [0] * length

#Isi array konvolusi
for i in range(m):
    for j in range(n):
        conv[i+j] += array1[i]*array2[j]

print(conv)
print(np.convolve(array1,array2))