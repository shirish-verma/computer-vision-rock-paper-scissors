import numpy as np
a_oldld = np.arange(6).reshape(2,3) + 10
a = np.array([2.3956735e-02, 5.2369774e-06, 4.8421123e-05, 9.7598958e-01])
print(a)
# [[10 11 12]
#  [13 14 15]]

print(np.argmax(a))
# 5

print(np.argmax(a, axis=0))
# array([1, 1, 1])

ind = np.unravel_index(np.argmax(a), a.shape)
print(ind)
print(a[ind])

my_array = np.array([2.3956735e-02, 5.2369774e-06, 4.8421123e-05, 9.7598958e-01])
my_list = list(my_array)
print(max(my_list))
print(my_list.index(max(my_list)))