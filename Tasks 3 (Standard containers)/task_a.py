
def calc_postfix_entry(postfix : list[str]):
    stack_num = []
    n = len(postfix)
    for i in range(n):
        if postfix[i] == '+':
            tmp = stack_num.pop() + stack_num.pop()
            stack_num.append(tmp)
        elif postfix[i] == "-":
            num1 = stack_num.pop()
            num2 = stack_num.pop()
            stack_num.append(num2 - num1)
        elif postfix[i] == "*":
            tmp = stack_num.pop() * stack_num.pop()
            stack_num.append(tmp)
        else:
            stack_num.append(int(postfix[i]))
    return stack_num.pop()


if __name__ == '__main__':
    postfix = list(input().split())
    print(calc_postfix_entry(postfix))