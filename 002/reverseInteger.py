# coding=utf-8
class Solution:
  def reverse(self, x: int) -> int:
    while x % 10 == 0:
      x /= 10
    if x >= 0:
      reverse_x = int(str(x)[::-1])
    if x < 0:
      reverse_x = -1 * int(str(-1*x)[::-1])
    min_reverse_x = -2 ** 31
    max_reverse_x = -2 ** 31 -1
    if reverse_x in range(min_reverse_x, max_reverse_x):
      return 0
    return reverse_x

def main():
  input_x = 123
  solution = Solution()
  print(solution.reverse(input_x))

if __name__ == '__main__':
  main()
