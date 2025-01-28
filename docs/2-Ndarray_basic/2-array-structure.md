# Part 2. 数组内存结构

在本节中，我将介绍 `ndarray` 的内存结构。

**学习目标**


在完成这一节的学习之后，你将会掌握:

- 行主序(C 风格)和列主序(Fortran 风格)的区别
- `ndarray`的内存结构


```python
import numpy as np
```

## 课程视频

## `ndarray`的内存结构


```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
```

`ndarray`的一个实例由计算机内存中的一个连续的一维内存段（由数组本身或其他对象拥有）和一个索引方案组合而成。该索引方案将 N 个整数组成的索引数组映射到内存块中的某个位置，索引数组可以变化的范围由数组的形状(`shape`)属性定义，每个单位数据占用的字节数以及如何解释这些数据由数组的数据类型对象(`dtype`)属性定义。


```python
arr.shape
```




    (4, 3)




```python
arr.dtype
```




    dtype('int64')



`ndarray`的内存可以适应任何步长(stride)的索引方案，在该索引方案中，N 维索引数组对应于该   `ndarray`的内存段的偏移量(offset 以字节为单位)为：

$$ n_{offset} = \sum^{N-1}_{k=0}s_kn_k $$

其中 $n = (n_0, n_1, ..., n_{N-1})$ 为索引数组， $s = (s_0, s_1, ..., s_{N-1})$为步长数组。


```python
arr.strides
```




    (24, 8)



列优先顺序(column-major order, 常在 Fortran 和 Matlab 中使用)和行优先顺序(row-major order, 常在 C 中使用) 只是步长方案的特定类型，他们对应于下述步长数组访问的内存：

 - 行优先顺序 (C 语言): $s_i = \prod^{N-1}_{k=i+1}shape[k]$
 - 列优先顺序 (Fortran 语言): $s_i = \prod^{j-1}_{k=0}shape[k]$

其中 $shape[j]$ 是数组在第 j 个维度的长度。


```python
np.array(arr, order='C').strides
```




    (24, 8)




```python
np.array(arr, order='F').strides
```




    (8, 32)



## `ndarray`的内存相关属性


```python
arr
```




    array([[ 1,  2,  3],
           [ 4,  5,  6],
           [ 7,  8,  9],
           [10, 11, 12]])



一下属性包含有关数组内存布局的信息:

 - `ndarray.flags`:有关数组内存布局的信息。


```python
arr.flags
```




      C_CONTIGUOUS : True
      F_CONTIGUOUS : False
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False



 - `ndarray.shape`:数组形状的元组。


```python
arr.shape
```




    (4, 3)



 - `ndarray.strides`:数组每个维度的步长元组。


```python
arr.strides
```




    (24, 8)



 - `ndarray.ndim`:数组的维数。


```python
arr.ndim
```




    2



 - `ndarray.data`:指向数组内存块开头的 Python 缓冲区对象。


```python
arr.data
```




    <memory at 0x000002D6E7E87510>



 - `ndarray.size`:数组中元素的数量。


```python
arr.size
```




    12



 - `ndarray.itemsize`:一个数组元素的大小(byte)。


```python
arr.itemsize
```




    8



 - `ndarray.nbytes`:数组占用内存的总字节数。


```python
arr.nbytes
```




    96



 - `ndarray.base`:如果内存来自其他对象，则为基对象。


```python
repr(arr.base)
```




    'None'



 - `ndarray.dtype`:数组数据类型。


```python
arr.dtype
```




    dtype('int64')


