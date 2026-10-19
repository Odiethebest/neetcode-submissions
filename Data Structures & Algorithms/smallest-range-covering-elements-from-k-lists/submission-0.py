class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        items = sorted((v, i) for i, row in enumerate(nums) for v in row)
        counts = [0] * len(nums)
        covered = left = 0
        answer = [items[0][0], items[-1][0]]
        for value, group in items:
            if counts[group] == 0: covered += 1
            counts[group] += 1
            while covered == len(nums):
                low, old = items[left]
                if (value - low, low) < (answer[1] - answer[0], answer[0]): answer = [low, value]
                counts[old] -= 1
                if counts[old] == 0: covered -= 1
                left += 1
        return answer