class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        table = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I"),
   ]
        for cap, roman in table:
            d, m = divmod(num, cap)
            res += roman * d
            num = m

        return res
obj1=Solution()
print(obj1.intToRoman(3))
print(obj1.intToRoman(58))
print(obj1.intToRoman(515))

            