from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # not nums = ...
        nums[:] = sorted(list(set(nums)))
        return len(nums)


def main():
    nums = [1, 3, 2, 1]
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Input: {nums}")
    solution = Solution()
    print(f"Output: {solution.removeDuplicates(nums)}, nums = {nums}")

if __name__ == "__main__":
    main()
