from typing import List


def maxProduct(self, nums: List[int]) -> int:        
        max_ = [nums[0]-1, nums[1]-1] if nums[0]-1>nums[1]-1 else [nums[1]-1, nums[0]-1]

        for i in range(2, len(nums)):
            if nums[i]-1 > max_[1]:
                if nums[i]-1 > max_[0]:
                    max_[1] = max_[0]
                    max_[0] = nums[i]-1
                else:
                    max_[1] = nums[i]-1
            # print(max_)
        return max_[0] * max_[1]
