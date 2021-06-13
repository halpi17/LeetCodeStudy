from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        flag = True
        for i in range(len(strs)):
            prefix_candidate = strs[0][i]
            for str_element in strs[1:]:
                if str_element[i] != prefix_candidate:
                    flag = False
                    break
            if flag == True:
                prefix += prefix_candidate
        return prefix

def main():
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))

if __name__ == "__main__":
    main()
