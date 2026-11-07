def is_prime(number):
    """Zwraca True jeżeli liczba jest pierwsza."""
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Wyswietla kolejną liczbę pierwsza większą niż podana liczba"""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
        break

print(is_prime(9))
print_next_prime(101)