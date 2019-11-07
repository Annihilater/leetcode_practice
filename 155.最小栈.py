#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/7 15:48
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : 155.最小栈.py


class MinStack:
    """
    数据栈存数据
    辅助栈存数据站内最小值的索引
    """

    def __init__(self):
        self.data = []  # 数据栈
        self.helper = []  # 辅助栈

    def push(self, x):
        """
        辅助栈没有元素时，则与数据栈同步 push
        x < 最小值（先取索引，再从数据栈取最小值），辅助栈同步 push
        否则不同步 push
        :param x:新值
        :return:
        """
        self.data.append(x)
        if len(self.helper) == 0 or x < self.data[self.helper[-1]]:
            index = self.data.index(x)
            self.helper.append(index)

    def pop(self):
        """
        如果 pop 的数的索引位与最小值索引位相同，辅助栈同步 pop
        否则不 pop
        :return: 数据栈顶的数
        """
        if self.data:
            index = len(self.data) - 1  # 此处 数据栈的长度-1 就是数据栈顶元素的索引
            if index == self.helper[-1]:
                self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def get_min(self):
        if self.helper:
            index = self.helper[-1]
            return self.data[index]


if __name__ == '__main__':
    # [0, 1, 0]
    min_stack = MinStack()
    min_stack.push(0)
    min_stack.push(1)
    min_stack.push(0)
    print(min_stack.get_min())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.get_min())
