import numpy as np

m = np.array([
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
])
r = m[[1,2,3]]
# print(r)

# r = m[[1,2,3],[1,2,3]]
# print(r)
idx_arr = np.array([
            [True, False, True, False, True],
            [True, False, True, False, True],
            [True, False, True, False, True],
            [True, False, True, False, True]
])
print(m[idx_arr])

print(m[m>4])











