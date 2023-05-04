# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It
# encrypts letters by shifting them over by a certain number of places in the
# alphabet. We call the length of shift the key. For example, if the key is 3,
# then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message,
# you must shift the encrypted letters in the opposite direction. This program
# lets the user encrypt and decrypt messages according to this algorithm.
#
# When you run the code, the output will look like this:
#
# Do you want to (e)ncrypt or (d)ecrypt?
# > e
# Please enter the key (0 to 25) to use.
# > 4
# Enter the message to encrypt.
# > Meet me by the rose bushes tonight.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
#
# Do you want to (e)ncrypt or (d)ecrypt?
# > d
# Please enter the key (0 to 26) to use.
# > 4
# Enter the message to decrypt.
# > QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# MEET ME BY THE ROSE BUSHES TONIGHT.


def encrypt(key: int, text: str) -> str:
    return ''.join([
        chr((ord(char) % (
            offset := ord('A') if char.isupper() else ord('a')) + key) % 26 + offset
            ) if char.isalpha() else char
        for char in text
    ])


def decrypt(key: int, text: str) -> str:
    return ''.join([
        chr((ord(char) % (
            offset := ord('A') if char.isupper() else ord('a')) - key) % 26 + offset
            ) if char.isalpha() else char
        for char in text
    ])


def main():
    mode = input('Do you want to (e)ncrypt or (d)ecrypt?\n> ')

    match mode:
        case 'encrypt' | 'e':
            key = int(input('Please enter the key (0 to 25) to use.\n> '))
            msg = input('Enter the message to encrypt.\n>')
            print(encrypt(key, msg))
        case 'd':
            key = int(input('Please enter the key (0 to 25) to use.\n> '))
            msg = input('Enter the message to decrypt.\n>')
            print(decrypt(key, msg))
        case _:
            print('invalid option:', mode)


if __name__ == '__main__':
    main()
