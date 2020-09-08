def countBits(n):
    num = bin(n)
    num = num[2:]
    cnt = 0
    for i in num:
        if i =='1':
            cnt += 1
    return cnt

def countBits_best(n):
    return bin(n).count("1")

print(countBits(1234))