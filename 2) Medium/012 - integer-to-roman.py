class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """     
        user_num = num
        # List in constant length, Dictionary lookup = O(1) time complexity
        romanNumerals= [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]
        
        result=""
        
        for roman_key,int_value in romanNumerals:
            while user_num>=int_value:
                result+=roman_key
                user_num-=int_value
            if user_num==0:
                return result

#*-------Tests-------#
sol = Solution()
test1=sol.intToRoman(3749)
test2=sol.intToRoman(58)
test3=sol.intToRoman(1994)
print(f"Test: {1},\t Roman String:{test1}")
print(f"Test: {2},\t Roman String:{test2}")
print(f"Test: {3},\t Roman String:{test3}")
#^ Time Complexity:
#^ O(log(num)) - the algorithm processes each digit of input number, and the number of digits grows logarithmically with the input size.
#^ Space Complexity: 
#^ O(log(num)) - the result string grows in proportion to the number of Roman numeral characters, which is logarithmic in terms of the input number.