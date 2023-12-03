class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        res = ''
        sign = 1

        # Check for the sign
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        # Read digits until a non-digit character is encountered
        for i in s:
            if i.isdigit():
                res += i
            else:
                break

        # Convert the result to an integer
        if res == "":
            return 0
        res = int(res) * sign

        # Clamp the result to the 32-bit signed integer range
        int_min, int_max = -2**31, 2**31 - 1
        if res < int_min:
            return int_min
        elif res > int_max:
            return int_max
        else:
            return res
