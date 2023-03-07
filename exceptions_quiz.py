"""
Nicole Hsu A01340726
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



def main():
    """
    Drives the program.
    """
    check_password("wda1")

if __name__ == "__main__":
    main()