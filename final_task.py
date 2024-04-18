
import numpy as np
import time
from scipy import linalg
import matplotlib.pyplot as plt



#1次から1000次の正方行列を生成してリスト化
matrix_list = []
right_side_list = []
for size in range(100,501):
    matrix = np.random.randint(-10,10 , size = (size, size))
    matrix_list.append(matrix)
    right_side = np.random.randint(-10, 10, size = size)
    right_side_list.append(right_side)

#1次から1000次の連立方程式を生成してリスト
left_side_list = matrix_list



#リストをforループで回し行列式の計算
determinant_time_list = []
for i, matrix in enumerate(matrix_list):
    start_time = time.time() 
    determinant = linalg.det(matrix)#行列式計算
    end_time = time.time()
    diff_time = end_time - start_time
    determinant_time_list.append(diff_time)

#何回か計算して分散を表示したほうがよさそう
plt.plot(determinant_time_list)
plt.title("determinant")
plt.xlabel("degree")
plt.ylabel("time [s]")
plt.show()

#連立方程式の計算

equations_time_list = []
for left_side, right_side in zip(left_side_list, right_side_list):
    
    start_time = time.time() 
    solver = np.linalg.solve(left_side, right_side)
    end_time = time.time() 
    diff_time = end_time - start_time
    equations_time_list.append(diff_time)
    
    

plt.plot(equations_time_list)
plt.title("equations")
plt.xlabel("degree")
plt.ylabel("time [s]")
plt.show()