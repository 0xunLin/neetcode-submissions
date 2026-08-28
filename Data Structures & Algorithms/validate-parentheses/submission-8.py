class Solution:
    def isValid(self, s: str) -> bool:
        new_s = []

        for char in s:
            match char:
                case '(':
                    new_s.append(')')
                case '{':
                    new_s.append('}')
                case '[':
                    new_s.append(']')
                case ')' | '}' | ']':
                    if not new_s or new_s.pop() != char:
                        return False
                case _ :
                    pass
        return not new_s
                
                    