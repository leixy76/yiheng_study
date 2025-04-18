# -*- coding: UTF-8 -*-
import numpy as np
a=np.array([2,4,5,8,-3])
print('向量a：',a)
print ('向量a的1-范数:')
print(np.linalg.norm(a,ord=1))
print ('向量a的2-范数:')
print(np.linalg.norm(a,ord=2))
print ('向量a的∞-范数:')
print(np.linalg.norm(a,ord=np.inf))
# -*- coding: UTF-8 -*-
import numpy as np
A=np.arange(3,15).reshape(3,4)
print('矩阵A：',A)
print('矩阵A的1-范数:')
print(np.linalg.norm(A,ord=1))
print('矩阵A的2-范数:')
print(np.linalg.norm(A,ord=2))
print('矩阵的∞-范数:')
print(np.linalg.norm(A,ord=np.inf))
print('矩阵A的F-范数:')
print(np.linalg.norm(A,ord='fro'))
print('矩阵A列向量的2-范数:')
print(np.linalg.norm(A,ord=2,axis=0))
print('矩阵A行向量的2-范数:')
print(np.linalg.norm(A,ord=2,axis=1))