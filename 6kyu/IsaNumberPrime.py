def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_prime_best(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))
    
print(is_prime(4))