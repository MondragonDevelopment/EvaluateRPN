t1 = ["2","1","+","3","*"]
t2 = ["4", "13", "5", "/", "+"]
t3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]

print(evalRPN(t1))
print(evalRPN(t2))
print(evalRPN(t3))