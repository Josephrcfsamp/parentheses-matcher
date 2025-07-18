# Function to check if the parentheses are balanced
def is_balanced(expression):
    stack = []  # Stack to hold opening parentheses
    # Pilha para armazenar os parênteses de abertura
    
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0
