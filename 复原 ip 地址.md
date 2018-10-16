# 复原 ip 地址



给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。



**示例:**

```
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```



解决方案：

```python
"""
Created by Annihilater on time.
"""
import time


class Solution1(object):
    def restoreIpAddresses(self, s):
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, ips, res):
        if not s and len(ips) == 4:
            res.append('.'.join(ips))
            return None
        for i in range(1, 4):
            if i > len(s):
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], ips + [s[:i]], res)


class Solution2(object):
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, ips, res):
        if len(s) > (4 - len(ips)) * 3:
            return
        if not s and len(ips) == 4:
            res.append(".".join(ips))
            return
        for i in range(min(3, len(s))):
            head = s[:i + 1]
            if (len(head) >= 2 and head[0] == '0') or int(head) > 255:
                continue
            self.dfs(s[i + 1:], ips + [s[:i + 1]], res)


class Solution3(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(0, s, [], res)
        return res

    def dfs(self, length, s, ips, res):
        if not s and length == 4:
            res.append(".".join(ips))
            return None
        if length == 4:
            return None

        self.dfs(length + 1, s[1:], ips + [s[:1]], res)

        if s[0] != '0':
            if len(s) >= 2:
                self.dfs(length + 1, s[2:], ips + [s[:2]], res)
            if len(s) >= 3 and int(s[:3]) <= 255:
                self.dfs(length + 1, s[3:], ips + [s[:3]], res)


a = "25525511135"
solution1 = Solution1()
solution2 = Solution2()
solution3 = Solution3()

start = time.clock()
result1 = solution1.restoreIpAddresses(a)
end = time.clock()
run_time = end - start
print(result1, '运行时间：', run_time)

start = time.clock()
result2 = solution2.restoreIpAddresses(a)
end = time.clock()
run_time = end - start
print(result1, '运行时间：', run_time)

start = time.clock()
result3 = solution3.restoreIpAddresses(a)
end = time.clock()
run_time = end - start
print(result1, '运行时间：', run_time)
---------------------------------------------------
Connected to pydev debugger (build 182.4323.49)
['255.255.11.135', '255.255.111.35'] 运行时间： 0.008958000000000022
['255.255.11.135', '255.255.111.35'] 运行时间： 0.00012299999999998423
['255.255.11.135', '255.255.111.35'] 运行时间： 0.00016500000000008175

Process finished with exit code 0
```

思路：

`Solution1`、`Solution2`、`Solution3`三种方法大致思路如下，只是在写法上略有不同，`Solution2`运行时间最短：



将字符串从左至右分别取一个、取两个、取三个、取四个的组成列表，若取四个之后原字符串为空，则将新组成的列表按照`.`号分隔开添加到 `result`列表返回。

- 在取两个、三个字符之前需要判断剩余字符串的首位是否为0；
  - 在取两个字符的时候，需要判断剩余的字符串长度是否大于2；
  - 在取三个字符的时候，需要判断剩余的字符串长度是否大于3，且所取的三个字符串转化为整数之后必须小于255；