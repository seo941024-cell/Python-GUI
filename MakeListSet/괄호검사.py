def check_brackets(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != match[ch]:
                return "ERROR"  # 스택이 비었거나 짝이 다름
            stack.pop()
    
    return "OK" if not stack else "ERROR"  # 스택이 비어야 정상