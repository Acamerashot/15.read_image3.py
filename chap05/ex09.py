import numpy as np, cv2

m = np.random.randn(3, 6) * 1000 // 10;

reduce_avg_row = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)
reduce_avg_col = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_AVG)

print(m)
print(reduce_avg_row)
print(reduce_avg_col)