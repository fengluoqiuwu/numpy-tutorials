# 习题2.1 ndarray 快速入门

这里是2.1节的习题。我们先在这里`import`所有需要用到的库。


```python
import numpy as np
import pandas as pd

arr1 = np.load("data/1-task-arr1.npy")
arr2 = np.load("data/1-task-arr2.npy")

iris_df = pd.read_csv("data/iris.csv")
```

## 基础练习

1. 请创建形状为`(3, 4, 5)`的全0，全1，全2 数组.


```python
# 请在这里输入你的代码
```

2. 请创建长度为16的一维数组，其中数据为 24,22,20,18...,-6.


```python
# 请在这里输入你的代码
```

3. 请获取数组`arr1`的维度、形状与类型.


```python
# 请在这里输入你的代码
```

4. 请获取`arr2`的简略字符串与详细字符串.


```python
# 请在这里输入你的代码
```

5. 请计算将`arr2`中的每个元素加100的平方根后的数组, 并求出它的最大值、均值与标准差.


```python
# 请在这里输入你的代码
```

6. 请遍历`arr2`中的所有元素并存储到一个集合`set`中.


```python
# 请在这里输入你的代码
```

7. 请获取一个数值为1 ~ 9 ,形状为 (3, 3)的数组，将其存储至`arr3`中.


```python
# 请在这里输入你的代码
```

8. 请计算`arr2`与`arr3`在第一个轴上的堆叠，`arr2`在`arr3`之前.


```python
# 请在这里输入你的代码
```

## 实战演练

这里我们使用了经典的鸢尾花数据集（Iris Dataset）。已知数组`iris_arr`存储的是`iris_df`的特征，即其中第2-5列的数据(按照顺序)，数组`iris_index`存储的是这四列的名称，`iris_target`存储的是目标特征，即`species`列中的数据。请完成下述问题。


```python
iris_arr = iris_df.to_numpy()[:,1:5]
iris_index = iris_df.columns[1:5].to_list().copy()
iris_target = iris_df.to_numpy()[:, 5].copy()
iris_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



1. 请计算每个特征的均值和方差


```python
# 请在这里输入你的代码
```

2. 请将`iris`数据标准化（均值为0，方差为1）


```python
# 请在这里输入你的代码
```

3. 请计算每个类别的平均特征值


```python
# 请在这里输入你的代码
# 提示：可以通过np.unique(arr)获取所有不同的值
```
