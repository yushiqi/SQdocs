5.1 Numpy
---------

NumPy(Numerical Python) 是 Python
语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

**Numpy的优势**

-  Numpy执行数值计算任务要比python代码便捷
-  Numpy中的数组存储效率和输入输出的性能远优于Python中等价的数据结构，且能够提升的性能是与数组中的元素成比例的
-  Numpy中的大部分代码是C编写的，具有优异的性能

**Numpy的array与Python原生list运行效率对比**

.. code:: python

   import numpy as np
   import time
   import random

   a = []
   for i in range(100000000):
       a.append(i)
   t = time.time()
   sum(a)
   print(time.time()-t)

   b = np.array(a)
   t = time.time()
   np.sum(b)
   print(time.time()-t)

   0.5847101211547852
   0.09261441230773926

1. Numpy的Ndrray对象
~~~~~~~~~~~~~~~~~~~~

Numpy最重要的一个特点是N维数组对象ndarry，它是一系列同类型数据的集合，以下标0为开始进行集合中元素的索引。

1.1 创建一维数组
^^^^^^^^^^^^^^^^

.. code:: python

   import numpy as np
   # 1. 直接传入列表
   t1 = np.array([1,2,3,4])

   # 2. 传入range生成序列
   t2 = np.array(range(5))

   # 3. 使用numpy自带的np.array()生成数组
   t3 = np.arange(0, 10, 2)

1.2 创建二维数组
^^^^^^^^^^^^^^^^

.. code:: python

   import numpy as np
   list_ = [[1,2],[3,4],[5,6]]
   print(np.array(list_))

   [[1 2]
    [3 4]
    [5 6]]

1.3 常用属性
^^^^^^^^^^^^

.. code:: python

   import numpy as np
   list_ = [[1,2],[3,4],[5,6]]
   A = np.array(list_)

   # 数组的维度
   A.ndim

   # 数组形状
   A.shape

   # 数组有多少元素
   A.size

================ ======================================================================================
属性             说明
================ ======================================================================================
ndarray.ndim     秩，即轴的数量或维度的数量
ndarray.shape    数组的维度，对于矩阵，n 行 m 列
ndarray.size     数组元素的总个数，相当于 .shape 中 n*m 的值
ndarray.dtype    ndarray 对象的元素类型
ndarray.itemsize ndarray 对象中每个元素的大小，以字节为单位
ndarray.flags    ndarray 对象的内存信息
ndarray.real     ndarray元素的实部
ndarray.imag     ndarray 元素的虚部
ndarray.data     包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
================ ======================================================================================

1.4 调整数组形状
^^^^^^^^^^^^^^^^

.. code:: python

   four = np.array([[1,2,3],[4,5,6]])
   # 修改的是原有的
   four.shape = (3,2)
   print(four)

   # 返回一个新的数组
   four = four.reshape(3,2)
   print(four)

   # 将多维变成一维数组
   five = four.reshape((6,),order='F')
   # 默认情况下‘C’以行为主的顺序展开，‘F’（Fortran风格）意味着以列的顺序展开
   six = four.flatten(order='F')
   print(five)
   print(six)

   # 拓展：数组的形状
   t = np.arange(24)
   print(t)
   print(t.shape)

   # 转换成二维
   t1 = t.reshape((4,6))
   print(t1)
   print(t1.shape)

   # 转成三维
   t2 = t.reshape((2,3,4))
   print(t2)
   print(t2.shape)

1.5 数组转list
^^^^^^^^^^^^^^

.. code:: python

   # 将数组转成list
   a= np.array([9, 12, 88, 14, 25])
   list_a = a.tolist()
   print(list_a)
   print(type(list_a))

2. Numpy的数据类型
~~~~~~~~~~~~~~~~~~

.. code:: python

   f = np.array([1,2,3,4,5], dtype = np.int16)
   # 返回数组中每个元素的字节单位长度
   print(f.itemsize) # 1 np.int8(一个字节)

   # 获取数据类型
   print(f.dtype)

   # 调整数据类型
   f1 = f.astype(np.int64)
   print(f1.dtype)

   # 拓展随机生成小数
   # 使用python语法，保留两位
   print(round(random.random(),2))
   arr = np.array([random.random() for i in range(10)])
   # 取小数点后两位
   print(np.round(arr,2))

Numpy的基本类型

========== ==========================================================================
名称       描述
========== ==========================================================================
bool\_     布尔型数据类型（True 或者 False）
int\_      默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
intc       与 C 的 int 类型一样，一般是 int32 或 int 64
intp       用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
int8       字节（-128 to 127）
int16      整数（-32768 to 32767）
int32      整数（-2147483648 to 2147483647）
int64      整数（-9223372036854775808 to 9223372036854775807）
uint8      无符号整数（0 to 255）
uint16     无符号整数（0 to 65535）
uint32     无符号整数（0 to 4294967295）
uint64     无符号整数（0 to 18446744073709551615）
float\_    float64 类型的简写
float16    半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32    单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64    双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex\_  complex128 类型的简写，即 128 位复数
complex64  复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128 复数，表示双 64 位浮点数（实数部分和虚数部分）
========== ==========================================================================

3. 广播
~~~~~~~

广播(Broadcast)是 Numpy 对不同形状(shape)的数组进行数值计算的方式，
对数组的算术运算通常在相应的元素上进行。

如果两个数组 a 和 b 形状相同，即满足 **a.shape == b.shape**\ ，那么 a*b
的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。

**相同形状的数组进行计算**

.. code:: python

   t1 = np.arange(24).reshape((6,4))
   t2 = np.arange(24).reshape((6,4))
   print(t1)
   print(t2)
   print(t1+t2)
   print(t1*t2)

   [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]
    [12 13 14 15]
    [16 17 18 19]
    [20 21 22 23]]

   [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]
    [12 13 14 15]
    [16 17 18 19]
    [20 21 22 23]]

   [[ 0  2  4  6]
    [ 8 10 12 14]
    [16 18 20 22]
    [24 26 28 30]
    [32 34 36 38]
    [40 42 44 46]]

   [[  0   1   4   9]
    [ 16  25  36  49]
    [ 64  81 100 121]
    [144 169 196 225]
    [256 289 324 361]
    [400 441 484 529]]

**与列数相同的一维数组进行计算**

.. code:: python

   t1 = np.arange(24).reshape((4,6))
   t2 = np.arange(0,6)
   print(t1)
   print(t2)
   print(t1-t2)

   [[ 0  1  2  3  4  5]
    [ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]
    
   [0 1 2 3 4 5]

   [[ 0  0  0  0  0  0]
    [ 6  6  6  6  6  6]
    [12 12 12 12 12 12]
    [18 18 18 18 18 18]]

**与行数相同的以为数组进行计算**

.. code:: python

   t1 = np.arange(24).reshape((4,6))
   t2 = np.arange(4).reshape((4,1))
   print(t1)
   print(t2)
   print(t1-t2)

   [[ 0  1  2  3  4  5]
    [ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]

   [[0]
    [1]
    [2]
    [3]]

   [[ 0  1  2  3  4  5]
    [ 5  6  7  8  9 10]
    [10 11 12 13 14 15]
    [15 16 17 18 19 20]]

4. 索引和切片
~~~~~~~~~~~~~

**一维数组操作**

.. code:: python

   import numpy as np
   a = np.arange(10)
   # 冒号分隔切片参数 start:stop:step 来进行切片操作
   print(a[2:7:2])    # 从索引 2 开始到索引 7 停止，间隔为 2

   # 如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素
   print(a[2],a)

   # 如果为 [2:]，表示从该索引开始以后的所有项都将被提取
   print(a[2:])

   [2 4 6]
   2 [0 1 2 3 4 5 6 7 8 9]
   [2 3 4 5 6 7 8 9]

**多维数组操作**

.. code:: python

   import numpy as np
   t1 = np.arange(24).reshape(4,6)
   print(t1)

   print('*'*20)

   print(t1[1]) # 取一行(一行代表是一条数据，索引也是从0开始的)

   print(t1[1,:]) # 取一行

   print(t1[1:])# 取连续的多行

   print(t1[1:3,:])# 取连续的多行

   print(t1[[0,2,3]])# 取不连续的多行

   print(t1[[0,2,3],:])# 取不连续的多行

   print(t1[:,1])# 取一列

   print(t1[:,1:])# 连续的多列

   print(t1[:,[0,2,3]])# 取不连续的多列

   print(t1[2,3])# # 取某一个值,三行四列

   print(t1[[0,1,1],[0,1,3]])# 取多个不连续的值，[[行，行。。。],[列，列。。。]]


   [[ 0  1  2  3  4  5]
    [ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]

   ********************

   [ 6  7  8  9 10 11]

   [ 6  7  8  9 10 11]

   [[ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]

   [[ 6  7  8  9 10 11]
    [12 13 14 15 16 17]]

   [[ 0  1  2  3  4  5]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]

   [[ 0  1  2  3  4  5]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]

   [ 1  7 13 19]

   [[ 1  2  3  4  5]
    [ 7  8  9 10 11]
    [13 14 15 16 17]
    [19 20 21 22 23]]

   [[ 0  2  3]
    [ 6  8  9]
    [12 14 15]
    [18 20 21]]

   15

   [0 7 9]

5. 修改数组中的数值
~~~~~~~~~~~~~~~~~~~

.. code:: python

   import numpy as np
   t = np.arange(24).reshape(4,6)
   # 修改某一行的值
   t[1,:]=0
   # 修改某一列的值
   t[:,1]=0
   # 修改连续多行
   t[1:3,:]=0
   # 修改连续多列
   t[:,1:4]=0
   # 修改多行多列，取第二行到第四行，第三列到第五列
   t[1:4,2:5]=0
   # 修改多个不相邻的点
   t[[0,1],[0,3]]=0
   # 可以根据条件修改，比如讲小于10的值改掉
   t[t<10]=0
   # 使用逻辑判断
   # np.logical_and &
   # np.logical_or |
   # np.logical_not ~
   t[(t>2)&(t<6)]=0 # 与
   t[(t<2)|(t>6)]=0 # 或
   t[~(t>6)]=0 # 非
   print(t)
   # 拓展
   # 三目运算（ np.where(condition, x, y)满足条件(condition)，输出x，不满足输出y。)）
   # score = np.array([[80,88],[82,81],[75,81]])
   # result = np.where(score>80,True,False)
   # print(result)

6. 数组的添加、删除和去重
~~~~~~~~~~~~~~~~~~~~~~~~~

6.1 append
^^^^^^^^^^

append 函数在数组的末尾添加值。
追加操作会分配整个数组，并把原来的数组复制到新数组

**参数说明：**

-  arr：输入数组
-  values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
-  axis：默认为
   None。当axis无定义时，是横向加成，返回总是为一维数组！当axis有定义的时候，分别为0和1的时候。当
   axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）

.. code:: python

   import numpy as np
   a = np.array([[1,2,3],[4,5,6]])
   print ('第一个数组：')
   print (a)
   print ('\n')
   print ('向数组添加元素：')
   print (np.append(a, [7,8,9]))
   print ('\n')
   print ('沿轴 0 添加元素：')
   print (np.append(a, [[7,8,9]],axis = 0))
   print ('\n')
   print ('沿轴 1 添加元素：')
   print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))

执行结果

.. code:: txt

   第一个数组：
   [[1 2 3]
    [4 5 6]]


   向数组添加元素：
   [1 2 3 4 5 6 7 8 9]


   沿轴 0 添加元素：
   [[1 2 3]
    [4 5 6]
    [7 8 9]]


   沿轴 1 添加元素：
   [[1 2 3 5 5 5]
    [4 5 6 7 8 9]]

6.2 insert
^^^^^^^^^^

insert函数在给定索引之前，沿给定轴在输入数组中插入值。

.. code:: python

   import numpy as np
   a = np.array([[1,2],[3,4],[5,6]])
   print ('第一个数组：')
   print (a)
   print ('\n')
   print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
   print (np.insert(a,3,[11,12]))
   print ('\n')
   print ('传递了 Axis 参数。 会广播值数组来配输入数组。')
   print ('沿轴 0 广播：')
   print (np.insert(a,1,[11],axis = 0))
   print ('\n')
   print ('沿轴 1 广播：')
   print (np.insert(a,1,11,axis = 1))

执行结果

.. code:: txt

   第一个数组：
   [[1 2]
    [3 4]
    [5 6]]


   未传递 Axis 参数。 在插入之前输入数组会被展开。
   [ 1  2  3 11 12  4  5  6]


   传递了 Axis 参数。 会广播值数组来配输入数组。
   沿轴 0 广播：
   [[ 1  2]
    [11 11]
    [ 3  4]
    [ 5  6]]


   沿轴 1 广播：
   [[ 1 11  2]
    [ 3 11  4]
    [ 5 11  6]]
