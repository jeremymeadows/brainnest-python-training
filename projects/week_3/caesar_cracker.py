# This program can hack messages encrypted with the Caesar cipher from the
# previous project, even if you don’t know the key. There are only 26 possible
# keys for the Caesar cipher, so a computer can easily try all possible
# decryptions and display the results to the user. In cryptography, we call
# this technique a brute-force attack.

from caesar_cipher import decrypt

CIPHERTEXT = "Ted'j buj qdoreto adem jxyi iushuj Y xqlu!"

print('Key: decrypted text')
for i in range(1, 26):
    print(f'{i:02}:', decrypt(i, CIPHERTEXT))
