"""
Nicole Hsu A01340726
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


def main():
    """
    Drives the program.
    """

if __name__ == "__main__":
    main()