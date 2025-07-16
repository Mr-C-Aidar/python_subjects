def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top, bottom, line, result = [], [], [], []

    for p in problems:
        d = p.split()
        if d[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not d[0].isdigit() or not d[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(d[0]) > 4 or len(d[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        w = max(len(d[0]), len(d[2])) + 2
        top.append(d[0].rjust(w))
        bottom.append(d[1] + ' ' + d[2].rjust(w - 2))
        line.append('-' * w)

        if show_answers:
            r = str(eval(d[0] + d[1] + d[2]))
            result.append(r.rjust(w))

    arranged = '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(line)
    if show_answers:
        arranged += '\n' + '    '.join(result)

    return arranged