def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Isolate nums & operators
    num1 = []
    num2 = []
    operator = []
    for i in problems:
        if i[0:i.index(' ')].isnumeric() and i[i.index(' ') + 3::].isnumeric():
            num1.append(int(i[0:i.index(' ')]))
            num2.append(int(i[i.index(' ') + 3::]))
        else:
            return 'Error: Numbers must only contain digits.'
        if i[i.index(' ') + 1:i.index(' ') + 2] == '+' or i[i.index(' ') + 1:i.index(' ') + 2] == '-':
            operator.append(i[i.index(' ') + 1:i.index(' ') + 2])
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if len(i[0:i.index(' ')]) > 4 or len(i[i.index(' ') + 3::]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # Compute solutions
    solutions = [num1[i] + num2[i] if operator[i] == '+' else num1[i] - num2[i] for i in range(len(num1))]

    longest_num = [num1[i] if len(str(num1[i])) >= len(str(num2[i])) else num2[i] for i in range(len(num1))]

    formatted = ''
    for i in range(len(num1)):
        # TOP PART
        if len(str(longest_num[i])) == len(str(num2[i])):
            for _ in range(abs(len(str(num1[i])) - len(str(num2[i])))):
                formatted += ' ' # 1 space
        formatted += '  ' + str(num1[i]) + '    ' # 2 / 4 spaces        

    formatted = formatted[:-4:] + '\n'

    for i in range(len(num1)):
        # MID PART
        formatted += str(operator[i])
        if len(str(num2[i])) == len(str(longest_num[i])):
            formatted += ' ' # 1 space
        else:
            for _ in range(abs(len(str(num1[i])) - len(str(num2[i]))) + 1):
                formatted += ' ' # 1 space

        formatted += str(num2[i]) + '    ' # 4 spaces
    
    formatted = formatted[:-4:] + '\n'

    # DASHED PART
    for i in range(len(longest_num)):
        for _ in range(len(str(longest_num[i]))):
            formatted += '-'
        formatted += '--' + '    ' # 4 spaces

    formatted = formatted[:-4:]

    if show_answers:
        formatted += '\n'
        for i in range(len(solutions)):
            if len(str(solutions[i])) == len(str(longest_num[i])):
                formatted += ' ' # 1 space  
            if(len(str(solutions[i])) < len(str(longest_num[i]))):
                for _ in range(abs(len(str(longest_num[i])) - len(str(solutions[i])))):
                    formatted += ' ' # 1 space
                formatted += '  ' + str(solutions[i]) + '    ' # 2 / 4 spaces
            else:
                formatted += ' ' + str(solutions[i]) + '    ' # 1 / 4 spaces
        formatted = formatted[:-4:]

    return formatted

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "230 - 0"])}')

print('\n' + arithmetic_arranger(['3012 - 23', '9930 - 9999', '43 + 23', '34 - 2', '230 - 0'], True))
print('\n' + arithmetic_arranger(["3801 - 2", "123 + 49"]))

print('\n' + arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "98 + 40"], True))