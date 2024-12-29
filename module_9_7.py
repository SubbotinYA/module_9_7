def is_prime(func):
    '''Декоратор возвращает проверку результата функции на простое число'''
    def wrapper(*kwarg):
        res = func(*kwarg)
        if res > 1:
            for i in range(2, res):
                if res % i == 0:
                    print(f"не является простым числом")
                    break
            else:
                print(f"является простым числом")
        return res
    return wrapper

@is_prime
def sum_three(*kwarg)->int:
    ''' Функция возвращает сумму чисел'''
    sum=0
    for i in kwarg:
        sum+=i
    return sum

def main():
    result = sum_three(2, 3, 6)
    print(result)


if __name__ == '__main__':
    main()