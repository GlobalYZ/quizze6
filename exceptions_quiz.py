"""
Nicole Hsu A01340726
Muyang Li A01352306
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
    :return: True if the password is strong
    :raises ValueError: if password does not meet the strength requirements


    >>> check_password_strength("Hell0W0rld")
    True
    >>> check_password_strength("EightLetters123")
    True
    >>> check_password_strength("ASDFjkl0")
    True
    """

    is_upper = False
    is_lower = False
    is_eight = False
    is_digit = False
    index = 1
    for letter in password:
        index += 1
        if letter.isupper():
            is_upper = True
            break
    for letter in password:
        if letter.islower():
            is_lower = True
            break
    for letter in password:
        if letter.isdigit():
            is_digit = True
            break
    if len(password) >= 8:
        is_eight = True
    if is_upper is False:
        raise ValueError('password needs upperCase letter')
    elif is_lower is False:
        raise ValueError('password needs lowerCase letter')
    elif is_eight is False:
        raise ValueError('password should be 8 characters or more')
    elif is_digit is False:
        raise ValueError('password needs a digit')
    else:
        return True


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()