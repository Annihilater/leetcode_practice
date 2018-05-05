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








