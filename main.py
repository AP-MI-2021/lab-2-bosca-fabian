from math import sqrt


def is_palindrome(n):
    """
    Verifica daca un numar este palindrom
    :param n: numarul verificat
    :return: True daca este palindrom, False in caz contrar
    """
    copie_nr = n
    palindrom = ''
    while copie_nr:
        palindrom = palindrom + copie_nr[-1]
        copie_nr = copie_nr[:-1]
    return bool(palindrom == n)


def test_is_palindrome():
    assert is_palindrome("1001") == 1
    assert is_palindrome("5") == 1
    assert is_palindrome("-151") == 0
    assert is_palindrome("1889881") == 1
    assert is_palindrome("666") == 1


def is_prime(n):
    """
    Verifica daca un numar este prim
    :param n: numarul verificat
    :return: True daca este prim, False in caz contrar
    """
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


def is_superprime(n):
    """
    Verifica daca un numar este superprim
    :param n: numarul verificat
    :return: True daca este supeprim, False in caz contrar
    """
    if n < 0:
        return False
    while n:
        copie_nr = n
        if is_prime(copie_nr) == 0:
            return False
        n = n // 10
    return True


def test_is_superprime():
    assert is_superprime(233) == 1
    assert is_superprime(237) == 0
    assert is_superprime(1) == 0
    assert is_superprime(0) == 0
    assert is_superprime(-123) == 0


def main():
    while True:
        print("1. Verificare daca un numar este palindrom")
        print("2. Verificare daca un numar este superprim")
        print("x. Iesire")
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            nr = input("Introduceti numarul: ")
            if is_palindrome(nr):
                print(f"Numarul {nr} este un palindrom")
            else:
                print(f"Numarul {nr} NU este un palindrom")
        elif optiune == '2':
            nr = int(input("Introduceti numarul: "))
            if is_superprime(nr):
                print(f"Numarul {nr} este superprim")
            else:
                print(f"Numarul {nr} NU este superprim")
        elif optiune == 'x':
            break


test_is_palindrome()
test_is_superprime()
main()
