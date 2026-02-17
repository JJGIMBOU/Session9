def add_numbers(a, b, c=0):
    """Adds 3 numbers
    :param a: first number
    param b: second number
    param c: third number
    :return: result of addition of two numbers
    """
    return a + b + c

print(add_numbers(1, 2, 3))
print(add_numbers(5, 7))

#a function can call itself a recursive function
def factorial(n):
    """Calculates the factorial of a number
    :param n: the n
    :return: facatorial result
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def rec_factorial(n):
    if n == 0:
        return 1
    return n * rec_factorial(n - 1)

print(factorial(6))
print(rec_factorial(6))

#function can call other function

def bond_greeting(first, last, lang = "en"):
    """
    Does the Bond Greeting
    :param first: first name
    :param last: last name
    :param lang: esp
    :return: the greeting
    """
    if lang == "en":
        return english_greeting(first, last)
    elif lang == "fr":
        return french_greeting(first, last)
    elif lang == "esp":
        return spanish_greeting(first, last)


def english_greeting(first, last):
    return f"The name is: {last}, {first} {last}"
def french_greeting(first, last):
    return f"Je mappelle: Le {last}, {first}, {last}"
def spanish_greeting(first, last):
    return f"Hola {last}, {first} {last}"

print(bond_greeting("James","Bond"))
print(bond_greeting("James","Bond", "fr"))
