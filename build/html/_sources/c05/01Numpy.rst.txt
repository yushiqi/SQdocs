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

6.3 delete
^^^^^^^^^^

delete函数返回从输入数组中删除指定子数组的新数组。与 insert()
函数的情况一样，如果未提供轴参数， 则输入数组将展开。

**参数说明**\ ：

-  arr：输入数组
-  obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
-  axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开

.. code:: python

   a = np.arange(12).reshape(3,4)
   print ('第一个数组：')
   print (a)
   print ('\n')
   print ('未传递 Axis 参数。 在删除之前输入数组会被展开。')
   print (np.delete(a,5))
   print ('\n')
   print ('删除每一行中的第二列：')
   print (np.delete(a,1,axis = 1))
   print ('\n')

执行结果

.. code:: txt

   第一个数组：
   [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]


   未传递 Axis 参数。 在删除之前输入数组会被展开。
   [ 0  1  2  3  4  6  7  8  9 10 11]


   删除每一行中的第二列：
   [[ 0  2  3]
    [ 4  6  7]
    [ 8 10 11]]

6.4 unique
^^^^^^^^^^

unique 函数用于去除数组中的重复元素。

**参数说明：**

-  arr：输入数组，如果不是一维数组则会展开

-  return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
-  return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
-  return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数

.. code:: python

   a = np.array([5,2,6,2,7,5,6,8,2,9])
   print ('第一个数组：')
   print (a)
   print ('\n')
   print ('第一个数组的去重值：')
   u = np.unique(a)
   print (u)
   print ('\n')
   print ('去重数组的索引数组：')
   u,indices = np.unique(a, return_index = True)
   print (indices)
   print ('\n')
   print ('我们可以看到每个和原数组下标对应的数值：')
   print (a)
   print ('\n')
   print ('去重数组的下标：')
   u,indices = np.unique(a,return_inverse = True)
   print (u)
   print (indices)
   print ('\n')
   print ('返回去重元素的重复数量：')
   u,indices = np.unique(a,return_counts = True)
   print (u)
   print (indices)

执行结果

.. code:: txt

   第一个数组：
   [5 2 6 2 7 5 6 8 2 9]


   第一个数组的去重值：
   [2 5 6 7 8 9]


   去重数组的索引数组：
   [1 0 2 4 7 9]


   我们可以看到每个和原数组下标对应的数值：
   [5 2 6 2 7 5 6 8 2 9]


   去重数组的下标：
   [2 5 6 7 8 9]
   [1 0 2 0 3 1 2 4 0 5]


   返回去重元素的重复数量：
   [2 5 6 7 8 9]
   [3 2 2 1 1 1]

7. 排序和条件筛选
~~~~~~~~~~~~~~~~~

7.1 排序
^^^^^^^^

NumPy 提供了多种排序的方法。
这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。
下表显示了三种排序算法的比较。

============================= ==== =============== ======== ======
种类                          速度 最坏情况        工作空间 稳定性
============================= ==== =============== ======== ======
``'quicksort'``\ （快速排序） 1    ``O(n^2)``      0        否
``'mergesort'``\ （归并排序） 2    ``O(n*log(n))`` ~n/2     是
``'heapsort'``\ （堆排序）    3    ``O(n*log(n))`` 0        否
============================= ==== =============== ======== ======

-  **numpy.sort()**

numpy.sort() 函数返回输入数组的排序副本。函数格式如下：

::

   numpy.sort(a, axis, kind, order)

参数说明：

-  a: 要排序的数组
-  axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序，
   axis=0 按列排序，axis=1 按行排序
-  kind: 默认为’quicksort’（快速排序）
-  order: 如果数组包含字段，则是要排序的字段

-  **numpy.argsort()**

numpy.argsort() 函数返回的是数组值从小到大的索引值。

-  **numpy.lexsort()**

numpy.lexsort()
用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。

-  **msort、sort_complex、partition、argpartition**

========================================= =================================================================================
函数                                      描述
========================================= =================================================================================
msort(a)                                  数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。
sort_complex(a)                           对复数按照先实部后虚部的顺序进行排序。
partition(a, kth[, axis, kind, order])    指定一个数，对数组进行分区
argpartition(a, kth[, axis, kind, order]) 可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
========================================= =================================================================================

7.2 筛选
^^^^^^^^

-  **numpy.argmax() 和 numpy.argmin()**

numpy.argmax() 和
numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。

-  **numpy.nonzero()**

numpy.nonzero() 函数返回输入数组中非零元素的索引。

-  **numpy.where()**

numpy.where() 函数返回输入数组中满足给定条件的元素的索引。

-  **numpy.extract()**

numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素。

8. 数组迭代
~~~~~~~~~~~

NumPy 迭代器对象 ``numpy.nditer``
提供了一种灵活访问一个或者多个数组元素的方式。

.. code:: python

   import numpy as np
    
   a = np.arange(6).reshape(2,3)
   print (a)
   print ('\n')
   print ('迭代输出：')
   for x in np.nditer(a):
       print (x, end=", " )
   print ('\n')

执行结果

.. code:: txt

   [[0 1 2]
    [3 4 5]]


   迭代输出：
   0, 1, 2, 3, 4, 5, 

**控制遍历顺序**

-  ``for x in np.nditer(a, order='F'):``\ Fortran order，即是列序优先；
-  ``for x in np.nditer(a.T, order='C'):``\ C order，即是行序优先；

.. code:: python

   import numpy as np 
    
   a = np.arange(0,60,5) 
   a = a.reshape(3,4)  
   print ('原始数组是：')
   print (a)
   print ('\n')
   print ('以 C 风格顺序排序：')
   for x in np.nditer(a, order =  'C'):  
       print (x, end=", " )
   print ('\n')
   print ('以 F 风格顺序排序：')
   for x in np.nditer(a, order =  'F'):  
       print (x, end=", " )

执行结果

.. code:: txt

   原始数组是：
   [[ 0  5 10 15]
    [20 25 30 35]
    [40 45 50 55]]


   以 C 风格顺序排序：
   0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 

   以 F 风格顺序排序：
   0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,

**使用外部循环**

nditer类的构造器拥有flags参数，常用的值有：

================= ==============================================
参数              描述
================= ==============================================
``c_index``       可以跟踪 C 顺序的索引
``f_index``       可以跟踪 Fortran 顺序的索引
``multi-index``   每次迭代可以跟踪一种索引类型
``external_loop`` 给出的值是具有多个值的一维数组，而不是零维数组
``read-write``    遍历数组的同时，实现对数组元素值得修改
``write-only``    遍历数组的同时，实现对数组元素值得修改
================= ==============================================

.. code:: python

   import numpy as np
    
   a = np.arange(0,60,5) 
   a = a.reshape(3,4)  
   print ('原始数组是：')
   print (a)
   print ('\n')
   for x in np.nditer(a, op_flags=['readwrite']): 
       x[...]=2*x 
   print ('修改后的数组是：')
   print (a)

执行结果

.. code:: txt

   原始数组是：
   [[ 0  5 10 15]
    [20 25 30 35]
    [40 45 50 55]]


   修改后的数组是：
   [[  0  10  20  30]
    [ 40  50  60  70]
    [ 80  90 100 110]]

9. Numpy计算
~~~~~~~~~~~~

9.1 数学/算数函数
^^^^^^^^^^^^^^^^^

===================================================== ======================================
函数                                                  **描述**
===================================================== ======================================
numpy.sqrt(array)                                     平方根函数
numpy.exp(array)                                      指数函数
numpy.abs/fabs(array)                                 绝对值
numpy.square(array)                                   计算各元素的平方 等于array**2
numpy.log/log10/log2(array)                           对数函数
numpy.sign(array)                                     计算各元素的正负号
numpy.isnan(array)                                    判断各元素是否为NaN
numpy.isinf(array)                                    判断各元素是否为Inf
numpy.cos/cosh/sin/sinh/tan/tanh(array)               三角函数
numpy.modf(array)                                     整数和小数分离，返回两个数组
numpy.ceil(array)                                     向上取整
numpy.floor(array)                                    向下取整
numpy.rint(array)                                     四舍五入
numpy.trunc(array)                                    向0取整
numpy.add(array1,array2)                              元素级加法
numpy.subtract(array1,array2)                         元素级减法
numpy.multiply(array1,array2)                         元素级乘法
numpy.divide(array1,array2)                           元素级除法
numpy.power(array1,array2)                            元素级指数
numpy.maximum/minimum(array1,aray2)                   元素级最大/最小值
numpy.fmax/fmin(array1,array2)                        元素级最大/最小值，忽略NaN
numpy.mod(array1,array2)                              元素级求模
numpy.copysign(array1,array2)                         将第二个数组值得正负号复制给第一个数组
numpy.greater/greater_equal(array1,array2)            元素级比较运算，产生布尔型数组
numpy.less/less_equal (array1,array2)                 元素级比较运算，产生布尔型数组
numpy.equal/not_equal (array1,array2)                 元素级比较运算，产生布尔型数组
numpy.logical_end/logical_or/logic_xor(array1,array2) 元素级的真值逻辑运算
===================================================== ======================================

7.2 统计函数
^^^^^^^^^^^^

================== ============================================================
函数               描述
================== ============================================================
numpy.amin()       用于计算数组中的元素沿指定轴的最小值
numpy.amax()       用于计算数组中的元素沿指定轴的最大值
numpy.ptp()        计算数组中元素最大值与最小值的差
numpy.percentile() 计算百分位数
numpy.median()     计算中位数
numpy.mean()       计算算数平均值
numpy.average()    根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
numpy.std()        计算标准差
numpy.var()        计算方差
================== ============================================================

9.3 字符串函数
^^^^^^^^^^^^^^

======================= ==========================================
函数                    描述
======================= ==========================================
numpy.char.add()        对两个数组的逐个字符串元素进行连接
numpy.char.multiply()   返回按元素多重连接后的字符串
numpy.char.center()     居中字符串
numpy.char.capitalize() 将字符串第一个字母转换为大写
numpy.char.title()      将字符串的每个单词的第一个字母转换为大写
numpy.char.lower()      数组元素转换为小写
numpy.char.upper()      数组元素转换为大写
numpy.char.split()      指定分隔符对字符串进行分割，并返回数组列表
numpy.char.splitlines() 返回元素中的行列表，以换行符分割
numpy.char.strip()      移除元素开头或者结尾处的特定字符
numpy.char.join()       通过指定分隔符来连接数组中的元素
numpy.char.replace()    使用新字符串替换字符串中的所有子字符串
numpy.char.decode()     数组元素依次调用\ ``str.decode``
numpy.char.encode()     数组元素依次调用\ ``str.encode``
======================= ==========================================

10. 数组的拼接
~~~~~~~~~~~~~~

10.1 根据轴连接
^^^^^^^^^^^^^^^

**np.concatenate()**

.. code:: python

   a = np.array([[1,2],[3,4]])
   b = np.array([[5,6],[7,8]])
   print(a)
   print(b)
   print ('\n')
   # 要求a,b两个数组的维度相同
   print ('沿轴 0 连接两个数组：')
   print (np.concatenate((a,b),axis= 0))
   print ('\n')
   print ('沿轴 1 连接两个数组：')
   print (np.concatenate((a,b),axis = 1))

执行结果

.. code:: txt

   [[1 2]
    [3 4]]
   [[5 6]
    [7 8]]
    
   沿轴 0 连接两个数组：
   [[1 2]
    [3 4]
    [5 6]
    [7 8]]


   沿轴 1 连接两个数组：
   [[1 2 5 6]
    [3 4 7 8]]

10.2 根据轴堆叠
^^^^^^^^^^^^^^^

**np.stack()**

.. code:: python

   a = np.array([[1,2],[3,4]])
   b = np.array([[5,6],[7,8]])
   print(a)
   print(b)
   print ('\n')

   print ('沿轴 0 连接两个数组：')
   print (np.stack((a,b),axis= 0))
   print ('\n')
   print ('沿轴 1 连接两个数组：')
   print (np.stack((a,b),axis = 1))

执行结果

.. code:: txt

   [[1 2]
    [3 4]]
   [[5 6]
    [7 8]]


   沿轴 0 连接两个数组：
   [[[1 2]
     [3 4]]

    [[5 6]
     [7 8]]]


   沿轴 1 连接两个数组：
   [[[1 2]
     [5 6]]

    [[3 4]
     [7 8]]]

10.3 矩阵垂直/水平拼接
^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

   v1 = [[0,1,2,3,4,5],
   [6,7,8,9,10,11]]

   v2 = [[12,13,14,15,16,17],
   [18,19,20,21,22,23]]

   print(v1)
   print(v2)
   print('\n')

   # 矩阵垂直拼接
   result = np.vstack((v1,v2))
   print(result)

   v1 = [[0,1,2,3,4,5],
   [6,7,8,9,10,11]]

   v2 = [[12,13,14,15,16,17],
   [18,19,20,21,22,23]]

   # 矩阵水平拼接
   result = np.hstack((v1,v2))
   print(result)

执行结果

.. code:: txt

   [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
   [[12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23]]


   [[ 0  1  2  3  4  5]
    [ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]
   [[ 0  1  2  3  4  5 12 13 14 15 16 17]
    [ 6  7  8  9 10 11 18 19 20 21 22 23]]

**注意：**

-  **concatenate不增加新的维度， stack在原来的维度上增加了一个维度**
-  **hstack 和vstack是和concatenate函数是一样的，不增加新的维度**

.. code:: python

   a = np.array([[1,2],[3,4]])
   b = np.array([[5,6],[7,8]])
   print(a)
   print(b)
   print ('\n')
   print ('concatenate：')
   print (np.concatenate((a,b),axis= 0))
   print ('\n')

   print ('stack：')
   print (np.stack((a,b),axis= 0))
   print ('\n')

   print ('vstack：')
   print(np.vstack((a,b)))

执行结果

::

   [[1 2]
    [3 4]]
   [[5 6]
    [7 8]]


   concatenate：
   [[1 2]
    [3 4]
    [5 6]
    [7 8]]


   stack：
   [[[1 2]
     [3 4]]

    [[5 6]
     [7 8]]]


   vstack：
   [[1 2]
    [3 4]
    [5 6]
    [7 8]]

11. 数组的分割
~~~~~~~~~~~~~~

split将一个数组分割为多个子数组

**参数说明：**

-  ary：被分割的数组
-  indices_or_sections：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
-  axis：沿着哪个维度进行切向，默认为0，横向切分。为1时，纵向切分

.. code:: python

   arr = np.arange(9).reshape(3,3)
   print(arr)
   print('\n')
   print ('将数组分为三个大小相等的子数组：\n')
   b = np.split(arr,3)
   print (b)

执行结果

.. code:: txt

   [[0 1 2]
    [3 4 5]
    [6 7 8]]


   将数组分为三个大小相等的子数组：

   [array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]

水平轴分割数组，也可使用\ ``numpy.hsplit``

.. code:: python

   harr = np.floor(10 * np.random.random((2, 6)))
   print ('原array：')
   print(harr)
   print ('拆分后：')
   print(np.split(harr,2,1))
   print(np.hsplit(harr, 2))

执行结果

.. code:: txt

   原array：
   [[1. 9. 7. 7. 1. 9.]
    [8. 1. 3. 2. 6. 9.]]
   拆分后：
   [array([[1., 9., 7.],
          [8., 1., 3.]]), array([[7., 1., 9.],
          [2., 6., 9.]])]
   [array([[1., 9., 7.],
          [8., 1., 3.]]), array([[7., 1., 9.],
          [2., 6., 9.]])]

垂直轴分割数组，也可以使用\ ``numpy.vsplit``

::

   harr = np.floor(10 * np.random.random((2, 6)))
   print ('原array：')
   print(harr)
   print ('拆分后：')
   print(np.split(harr,2,0))
   print(np.vsplit(harr, 2))

执行结果

.. code:: txt

   原array：
   [[6. 1. 1. 1. 9. 9.]
    [0. 7. 8. 1. 4. 6.]]
   拆分后：
   [array([[6., 1., 1., 1., 9., 9.]]), array([[0., 7., 8., 1., 4., 6.]])]
   [array([[6., 1., 1., 1., 9., 9.]]), array([[0., 7., 8., 1., 4., 6.]])]

**注意：spli函数只能用于均等分割，如果不能均等分割则会报错：**\ ``array split does not result in an equal division``

12. 数组中nan和inf
~~~~~~~~~~~~~~~~~~

   inf 表示无穷大，需要使用 ``float(‘inf’)`` 函数来转化，那么对应的就有
   ``float('-inf')`` 表示无
   穷小了。这样你就可以使用任意数来判断和它的关系了。
   那什么时候会出现inf呢？
   比如一个数字除以0，Python中会报错，但是numpy中会是一个inf或者-inf

..

   nan在 pandans 中常见，表示缺失的数据，所以一般用 nan
   来表示。任何与其做运算结果都是 nan

.. code:: python

   a = np.nan
   b = np.inf
   print(a,type(a))
   print(b,type(b))
   print('\n')
   # --判断数组中为nan的个数
   t = np.arange(24,dtype=float).reshape(4,6)
   # print(t)
   # print('\n')

   t[2, 3:5] = np.NaN


   t[1, 2] = np.inf
   print(t)
   print('\n')


   print(np.isnan(t))
   print('\n')
   print(np.isinf(t))

执行结果

.. code:: txt

   nan <class 'float'>
   inf <class 'float'>


   [[ 0.  1.  2.  3.  4.  5.]
    [ 6.  7. inf  9. 10. 11.]
    [12. 13. 14. nan nan 17.]
    [18. 19. 20. 21. 22. 23.]]


   [[False False False False False False]
    [False False False False False False]
    [False False False  True  True False]
    [False False False False False False]]


   [[False False False False False False]
    [False False  True False False False]
    [False False False False False False]
    [False False False False False False]]

13. 二维数组转置
~~~~~~~~~~~~~~~~

**transpose**

.. code:: python

   a = np.arange(12).reshape(3,4)
   print ('原数组：')
   print (a )
   print ('\n')
   print ('对换数组：')
   print (np.transpose(a))

执行结果

.. code:: txt

   原数组：
   [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]


   对换数组：
   [[ 0  4  8]
    [ 1  5  9]
    [ 2  6 10]
    [ 3  7 11]]

**T转置**

.. code:: python

   a = np.arange(12).reshape(3,4)
   print ('原数组：')
   print (a)
   print ('\n')
   print ('转置数组：')
   print (a.T)

执行结果

.. code:: txt

   原数组：
   [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]


   转置数组：
   [[ 0  4  8]
    [ 1  5  9]
    [ 2  6 10]
    [ 3  7 11]]

**swapaxes**

.. code:: python

   a = np.arange(12).reshape(3,4)
   re = a.swapaxes(1,0)
   print ('原数组：')
   print (a)
   print ('\n')
   print ('调用 swapaxes 函数后的数组：')
   print (re)

执行结果

.. code:: txt

   原数组：
   [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]


   调用 swapaxes 函数后的数组：
   [[ 0  4  8]
    [ 1  5  9]
    [ 2  6 10]
    [ 3  7 11]]
