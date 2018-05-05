[toc]
# 两个数组的交集 II
## 问题
给定两个数组，写一个方法来计算它们的交集。

**例如:**
给定 `nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]`, 返回 `[2, 2]`。

> 注意：
> - 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
> - 我们可以不考虑输出结果的顺序。


> 跟进：
> - 如果给定的数组已经排好序呢？你将如何优化你的算法？
> - 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
> - 如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

## 实现
### 方法一：字典方法
#### 执行时间：204ms
1. 先将两个列表分别转换为字典，字典的值是相应元素出现的次数；
2. 再比较相同元素在两个列表中出现的次数，取次数少的值；
3. 然后再将该元素循环添加到交集列表。
```python
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []
        dict_nums1 = dict(Counter(nums1))
        dict_nums2 = dict(Counter(nums2))
        for i in nums1:
            for j in nums2:
                if i == j:
                    if dict_nums1[i] <= dict_nums2[j]:
                        while dict_nums1[i]:
                            nums3.append(i)
                            dict_nums1[i] -= 1
                    else:
                        while dict_nums2[j]:
                            nums3.append(j)
                            dict_nums2[j] -= 1
        return nums3
```

### 方法二：排序-按索引比较元素
#### 执行时间：56ms
1. 先将两个列表分别排序；
2. 再按照索引一对一比较元素
    - 如果处于相同索引位置上的元素相等，则将该元素添加到结果列表，两个索引数同时+1
    - 如果处于相同索引位置上的元素不相等，则将较小元素的索引+1，再次比较，直到循环完其中一个列表
#### 写法一
```python
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []          # 定义返回的交集
        nums1.sort()        # 列表1排序
        nums2.sort()        # 列表2排序
        l1 = len(nums1)     # 定义l1为列表1长度
        l2 = len(nums2)     # 定义l2位列表2长度
        
        i = 0       # 定义列表1的索引起始位
        j = 0       # 定义列表2的索引起始位
        
        if l1 == 0 or l2 == 0:      # 考虑存在空集的情况
            return nums3            # 交集为空
        else:
            while i < l1:                       # 若超出列表1长度则停止循环
                if nums1[i] == nums2[j]:        # 比较相同索引位上的元素是否相等
                    nums3.append(nums1[i])
                    i += 1
                    j += 1
                    if j >= l2:                 # 若超出列表2长度则停止循环
                        return nums3
                else:
                    if nums1[i] > nums2[j]:     # 若不相等则，较小元素的索引位+1
                        j += 1
                        if j >= l2:
                            return nums3
                    else:
                        i += 1
            return nums3
                    
        
```

#### 写法二（比写法一更简洁）

```python
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []      # 定义结果列表
        nums1.sort()    # 列表1排序
        nums2.sort()    # 列表2排序
        l1 = len(nums1)     # 定义l1为列表1长度
        l2 = len(nums2)     # 定义l2位列表2长度
        
        i = 0 
        j = 0
        
        if l1 == 0 or l2 == 0:
            return nums3
        else:
            while (i < l1 and j < l2):
                if nums1[i] > nums2[j]:
                    j += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    nums3.append(nums1[i])
                    i += 1
                    j += 1
            return nums3
                    
        
```






