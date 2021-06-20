from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_sum = nums[0]

    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             subarray_sum = sum(nums[i:i+j+1])
    #             # print(f"i: {i}, i+j: {i+j}, subarray_sum = {subarray_sum}")
    #             if max_sum < subarray_sum:
    #                 max_sum = subarray_sum

    #     return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sum = max_sum = nums[0]

        for num in nums[1:]:
            if num < subarray_sum + num:
                subarray_sum = subarray_sum + num
            else:
                subarray_sum = num
            if max_sum < subarray_sum:
                max_sum = subarray_sum

        return max_sum


def main():
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # Output:  6
    # nums = [1]                             # Output:  1
    # nums = [5, 4, -1, 7, 8]                # Output: 23
    nums = [-2, -1]                        # Output: -1

    solution = Solution()
    print(f"Input: nums = {nums}")
    print(f"Output: {solution.maxSubArray(nums)}")

if __name__ == "__main__":
    main()
