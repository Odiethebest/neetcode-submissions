class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        small = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        scales = ["Billion", "Million", "Thousand", ""]
        result = []
        remaining = num
        for divisor, scale in zip([1000000000, 1000000, 1000, 1], scales):
            value, remaining = divmod(remaining, divisor)
            if value == 0:
                continue
            if value >= 100:
                result.extend([small[value // 100], "Hundred"])
                value %= 100
            if value >= 20:
                result.append(tens[value // 10])
                value %= 10
            if value:
                result.append(small[value])
            if scale:
                result.append(scale)
        return " ".join(result)
