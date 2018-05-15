class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        newnums = list(nums)
        j = len(nums)
        k %= j
        if j > 1:
            for i in range(j):
                if i + k <= j - 1:
                    nums[i+k] = newnums[i]
                else :
                    m = i + k - j
                    nums[m] = newnums[i]

                
                
        
        
        # 逐个向前推移
        # l = len(nums)  
        # k %= l
        # if k != 0:  
        #     for i in range(k):  
        #         j = l - 1  
        #         temp = nums[j]  
        #         while j > 0:  
        #             nums[j] = nums[j - 1]  
        #             j -= 1  
        #         nums[0] = temp