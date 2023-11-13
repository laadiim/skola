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
        x = input('Zadej prirozene cislo: ')
        try:
            x = int(x)
        except:
            print('jsi bulgur')
        else:
            if int(x) > 0 and abs(int(x) - float(x)) < 0.00001:
                return int(x)
            else:
                print('buliguri')

def main():
    number = input_natural_number()
    result = is_sum_of_primes(number)
    if result == 0:
        print('Nelze rozlozit')
    else:
        print(f'Lze rozlozit: {number - result} + {result} = {number}')

if __name__ == '__main__':
    main()