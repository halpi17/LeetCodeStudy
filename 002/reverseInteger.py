# coding=utf-8
class Solution:
  def reverse(self, x: int) -> int:
    while x % 10 == 0:
      x /= 10
    if x >= 0:
      reverse_x = int(str(x)[::-1])
    if x < 0:
      reverse_x = -1 * int(str(-1*x)[::-1])
    return reverse_x

def main():
  input_x = 123
  solution = Solution()
  print(solution.reverse(input_x))

if __name__ == '__main__':
  main()
