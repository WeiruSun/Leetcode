# question

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


```Python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        

        for i in range(len(operations)):
            if operations[i] == "+":
                current = stack[-2] + stack[-1]
                stack.append(current)
            elif operations[i] == "D":
                current = int(stack[-1])*2
                stack.append(current)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))
        # res = 0
        
        # for i in range(len(stack)):
        #     res += stack[i]
        
        # return res
        return sum(stack)


```

