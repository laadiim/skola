import random

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_sum_of_primes(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n-i) and i != n - i:
            return n-i
    return 0

def input_natural_number():
    while True:
        x = input('Zadej cislo: ')
        try:
            x = int(x)
        except:
            print('jsi bulgur')
        else:
            if int(x) > 0 and abs(int(x) - float(x)) < 0.00001:
                return int(x)
            else:
                print('buliguri')

if __name__ == '__main__':
    x = input_natural_number()
    print(is_sum_of_primes(x))
    print(is_prime(is_sum_of_primes(x)))