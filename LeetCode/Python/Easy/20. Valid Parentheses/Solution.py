class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:  # 1. Iterate through characters directly
            # 2. Check for ALL opening brackets
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                
            elif char == ")":
                # 3. Always check if stack is empty before reading stack[-1]
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False  # 4. Return False immediately if it's a mismatch
                    
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
                    
            elif char == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
                    
        # 5. Simple shorthand for checking if stack is empty
        return len(stack) == 0 
