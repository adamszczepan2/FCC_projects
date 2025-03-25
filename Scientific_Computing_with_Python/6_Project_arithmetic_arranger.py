def arithmetic_arranger(problems, show_answers=False):
    
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        value_1, sign, value_2 = problem.split(' ')

        if len(value_1) > 4 or len(value_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if sign not in ('+', '-'):
            return "Error: Operator must be '+' or '-'." 

        if not (value_1.isdigit() and value_2.isdigit()):
            return 'Error: Numbers must only contain digits.'
                
        max_length = max(len(value_1), len(value_2)) + 2 
        score = int(value_1) + int(value_2) if sign == '+' else int(value_1) - int(value_2)

        line_1 += value_1.rjust(max_length) + ' ' * 4
        line_2 += sign + value_2.rjust(max_length - 1) + ' ' * 4
        line_3 += '-' * max_length + ' ' * 4
        line_4 += str(score).rjust(max_length) + ' ' * 4

    problems = f"{line_1.rstrip()}\n{line_2.rstrip()}\n{line_3.rstrip()}"

    if show_answers:
        problems += f"\n{line_4.rstrip()}"
                  
    return problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')


"""Wersja code review by chatGPT"""

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for problem in problems:
        value_1, sign, value_2 = problem.split()

        if not (value_1.isdigit() and value_2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(value_1) > 4 or len(value_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if sign not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        max_length = max(len(value_1), len(value_2)) + 2
        score = str(int(value_1) + int(value_2)) if sign == '+' else str(int(value_1) - int(value_2))

        first_line.append(value_1.rjust(max_length))
        second_line.append(sign + value_2.rjust(max_length - 1))
        third_line.append('-' * max_length)
        fourth_line.append(score.rjust(max_length))

    arranged_problems = '\n'.join([
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(third_line),
    ])

    if show_answers:
        arranged_problems += '\n' + '    '.join(fourth_line)

    return arranged_problems

# Test
print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))