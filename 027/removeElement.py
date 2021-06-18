from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [num for num in nums if num != val]
        return len(nums)

def main():
    # nums = [3, 2, 2, 3]
    # val = 3
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(f"Input: {nums}")
    solution = Solution()
    print(f"Output: {solution.removeElement(nums, val)}, nums = {nums}")

if __name__ == "__main__":
    main()
