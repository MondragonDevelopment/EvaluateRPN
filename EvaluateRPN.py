t1 = ["2","1","+","3","*"]
t2 = ["4", "13", "5", "/", "+"]
t3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens):
    stack = []
    result = 0

    for st in range(len(tokens)):
        if tokens[st] == "+" and len(stack) > 1:
            result = stack[len(stack) - 2] + stack[len(stack) - 1]
            stack.pop()
            stack.pop()
            stack.append(result)
        elif tokens[st] == "-" and len(stack) > 1:
            result = stack[len(stack) - 2] - stack[len(stack) - 1]
            stack.pop()
            stack.pop()
            stack.append(result)
        elif tokens[st] == "*" and len(stack) > 1:
            result = stack[len(stack) - 2] * stack[len(stack) - 1]
            stack.pop()
            stack.pop()
            stack.append(result)
        elif tokens[st] == "/" and len(stack) > 1:
            result = int(stack[len(stack) - 2] / stack[len(stack) - 1])
            stack.pop()
            stack.pop()
            stack.append(result)
        else:
            stack.append(int(tokens[st]))
    return result

print(evalRPN(t1))
print(evalRPN(t2))
print(evalRPN(t3))