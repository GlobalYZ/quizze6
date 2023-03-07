"""
Nicole Hsu A01340726
<<<<<<< HEAD
Muyang LI
"""


def check_password_strength(password):
    isUpper = False
    isLower = False
    isEight = False
    isDigit = False
    index = 1
    for letter in password:
        index += 1
        if letter.isupper() == True:
            isUpper = True
            break
    for letter in password:
        if letter.islower == True:
            islower = True
            break
    for letter in password:
        if letter.isdigit() == True:
            isDigit = True
            break
    if index >= 8:
        isEight = True
    if isUpper is False:
        raise ValueError('password needs upperCase')
    elif isLower is False:
        raise ValueError('password needs lowerCase')
    elif isEight is False:
        raise ValueError('password should be 8 characters or more')
    elif isDigit is False:
        raise ValueError('password needs 1 digit')
    else:
        print("password Corrtect")

=======
"""

def check_password_strength(password):
    """
    Check the strength of the given password.

    This function checks the strength of the given password. This function considers a password strong if it contains
    at least 8 characters, has at least one uppercase letter, one lowercase letter, and at least one digit.
    If the password is deemed strong, this function returns True, otherwise False, as a boolean.

    :param password: a string
    :precondition: password must be a string
    :postcondition: correctly asserts that the given password is strong or not
    :return: True if the password is strong, False otherwise, as a boolean

    >>> check_password_strength("Hell0W0rld")
    True
    >>> check_password_strength("EightLetters123")
    True
    >>> check_password_strength("ASDFjkl0")
    True
    """
>>>>>>> 96ade170ec20d3f6c84fb93c117487611871bb88


def main():
    """
    Drives the program.
    """
<<<<<<< HEAD
    check_password("wda1")
=======
>>>>>>> 96ade170ec20d3f6c84fb93c117487611871bb88

if __name__ == "__main__":
    main()