def add(a, b):
    return a - b  # BUG: toplama yerine cikarma


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Sifira bolme hatasi")
    return a / b


def power(base, exp):
    return base ** exp
