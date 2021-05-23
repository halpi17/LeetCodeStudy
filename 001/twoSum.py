# coding=utf-8
class Solution():
  def twoSum(self, nums, target):
    h = {}
    for index, x in enumerate(nums):
      y = target - x
      if y in h:
        return [h[y], index]  # h[num]はhのnumに対するindex
      else:
        h[x] = index  # h = {num: index}
    return []

def main():
  nums = [2,7,11,15]
  target = 9

  solution = Solution()
  print(solution.twoSum(nums, target))

if __name__ == '__main__':
  main()
