class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_of_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s: 
            if char in map_of_brackets:
                if not stack or stack[-1] != map_of_brackets[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0