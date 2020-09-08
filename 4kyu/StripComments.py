# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string,markers):
    if string == '':
        return ''
    seperate = string.split('\n')
    for pos in range(1, len(seperate)):
        seperate[pos] ='\n'+seperate[pos]
    if string[-1] == '\n':
        seperate[-1] += '\n'
    ans = ''
    jump = False
    for pos in range(len(seperate)):
        jump = False
        for letter_pos in range(len(seperate[pos])):
            for mark in markers:
                if seperate[pos][letter_pos] == mark:
                    ans += ''.join(seperate[pos][:letter_pos].rstrip(' '))
                    jump = True
                    break
            if jump :
                break
        if not jump:
            ans += ''.join(seperate[pos])
    return ans.strip(' ')

def solution_best(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)            

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution('apples bananas strawberries pears\napples strawberries pears = apples @\n@ - watermelons bananas', ['?', ',', "'", '#', '@', '=', '^', '!', '.']))
print(solution("bananas bananas watermelons bananas ' avocados\nlemons avocados apples\npears strawberries pears strawberries\nbananas watermelons\n. lemons", ["'", '.', '^', '=', '?', ',']))