from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         nums.append(target)
    #         nums.sort()
    #         return nums.index(target)

def main():
    nums, target = [1, 3, 5, 6], 5 # Output: 2
    # nums, target = [1, 3, 5, 6], 2 # Output: 1
    # nums, target = [1, 3, 5, 6], 7 # Output: 4
    # nums, target = [1, 3, 5, 6], 0 # Output: 0
    # nums, target = [1], 0          # Output: 0
    solution = Solution()
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {solution.searchInsert(nums, target)}")

if __name__ == "__main__":
    main()
