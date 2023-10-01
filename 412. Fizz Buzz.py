class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            if (i+1)%3 == 0:
                if (i+1)%5 == 0:
                    answer.append("FizzBuzz")
                else:
                    answer.append("Fizz")
            elif (i+1)%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i+1))
        return answer
            