from collections import defaultdict
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 定义计数排序函数
        def cnt_sort():
            # 创建一个默认值为 0 的字典
            # cnt[num] 表示数字 num 在数组中出现的次数
            cnt = defaultdict(int)

            # 找到数组中的最小值和最大值
            # 这样可以确定需要遍历的数字范围
            minVal, maxVal = min(nums), max(nums)

            # 遍历数组中的每一个数字
            for num in nums:
                # 统计当前数字出现的次数
                cnt[num] += 1

            # idx 表示下一个要写入 nums 的位置
            idx = 0

            # 从最小值遍历到最大值，保证数字按升序处理
            for num in range(minVal, maxVal + 1):

                # 如果当前数字还有剩余次数，
                # 就将它写入 nums
                while cnt[num] > 0:
                    # 将当前数字放入数组的下一个位置
                    nums[idx] = num

                    # 移动写入位置
                    idx += 1

                    # 当前数字的剩余次数减一
                    cnt[num] -= 1

        # 调用计数排序函数，对 nums 原地排序
        cnt_sort()

        # 返回排序后的数组
        return nums