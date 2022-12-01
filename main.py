from controller2 import Initiate
from controller2 import RotWord
from controller2 import SubWord
from controller2 import XorRcon
from controller2 import TempXor
from controller2 import SubBytes
from controller2 import FormMatrix
from controller2 import ShiftRows
from controller2 import GaloisField
from controller2 import AddRoundKey
from controller2 import InverseSubBytes
from controller2 import InverseShiftRows

import time


def ReadFile(filename):
    f = open(filename, "r")
    content = f.read()

    return content


def WriteFile(filename, content):
    f = 0
    for i in range(0, len(content)):
        str1 = " ".join(content[i])
        if i == 0:
            f = open(filename, "w")
            str1 = str1 + "\n"
            f.write(str1)
            f.close()
        else:
            f = open(filename, "a")
            str1 = str1 + "\n"
            f.write(str1)

    f.close()


# APPENDING KEY
def append_keys(keys, final):
    w = []
    str1 = ""
    for i in range(0, len(final)):
        str1 = str1 + final[i]

        if len(str1) == 2:
            w.append(str1)
            str1 = ""
    keys.append(w)


def GenerateKeys(cipher_key):
    # USED FOR KEY EXPANDING

    rcon = ["01000000", "02000000", "04000000", "08000000", "10000000", "20000000", "40000000", "80000000",
            "1b000000",
            "36000000"]
    rcon_count = 0

    # CONVERTING TO THE MATRIX FORM
    keys = Initiate(cipher_key)
    print("Initial 4 keys : ", keys)

    for i in range(4, 44):
        print("-------------------------------------- ", i, "---------------------------------------")
        if i % 4 == 0:
            temp = keys[i - 1]
            temp = "".join(temp)
            print("Temp : ", temp)

            # SHIFTING
            print("Here ", temp)
            rotWord = RotWord(temp, 2)
            print("Rot word : ", rotWord)

            # SUBSTITUTION
            subWord = SubWord(rotWord)
            print("Sub word : ", subWord)

            XOR_Rcon = XorRcon(subWord, rcon[rcon_count])
            print("XOR RCON :", XOR_Rcon)

            rcon_count = rcon_count + 1

            final = TempXor(XOR_Rcon, keys[i - 4])
            print("Final : ", final)

            append_keys(keys, final)
        else:
            temp = keys[i - 1]
            temp = "".join(temp)
            print("Temp : ", temp)

            final = TempXor(temp, keys[i - 4])
            print("Final  : ", final)

            append_keys(keys, final)

    print("Expanded Keys : ", keys)

    return keys


def Encryption(plain_text, keys):
    print("***********************************************  ENCRYPTION  **********************************************")

    plainText = Initiate(plain_text)
    print("Plain text : ", plainText)

    addRoundKey = 0
    rowNum = 0
    for round in range(0, 11):
        print("--------------------------------------------", round, "-----------------------------------------------")

        # IF ROUND 1
        if round == 0:
            matrix = FormMatrix(plainText)
            print("matrix : ", matrix)

            key = keys[rowNum:rowNum + 4]
            rowNum = rowNum + 4
            key = FormMatrix(key)
            print("key : ", key)

            addRoundKey = AddRoundKey(matrix, key)
            print("Round Key : ", addRoundKey)

        # IF LAST ROUND
        elif round == 10:
            subMatrix = SubBytes(addRoundKey)
            print("Sub Bytes : ", subMatrix)

            shiftRows = ShiftRows(subMatrix)
            print("Shift Rows : ", shiftRows)

            # Getting next key
            key = keys[rowNum:rowNum + 4]
            rowNum = rowNum + 4
            key = FormMatrix(key)
            print("Round Key : ", key)

            addRoundKey = AddRoundKey(shiftRows, key)
            print("Add Round Key : ", addRoundKey)

        else:

            subMatrix = SubBytes(addRoundKey)
            print("Sub Bytes : ", subMatrix)

            shiftRows = ShiftRows(subMatrix)
            print("Shift Rows : ", shiftRows)

            # THIS FUNCTION DOES NOT APPEND ONE BIT AT THE START IF SINGLE BIT IS THERE
            mixColumns = GaloisField(shiftRows, 0)
            print("Mix Column : ", mixColumns)

            # Getting next key
            key = keys[rowNum:rowNum + 4]
            rowNum = rowNum + 4
            key = FormMatrix(key)
            print("Round Key : ", key)

            addRoundKey = AddRoundKey(mixColumns, key)
            print("Add Round Key : ", addRoundKey)

    finalCipherText = addRoundKey

    print("CIPHER TEXT :", finalCipherText)

    WriteFile("encryption.enc", finalCipherText)

    return finalCipherText


def Decryption(final_cipher_text, keys):
    print("*******************************************   DECRYPTION  ************************************************")
    addRoundKey = 0

    rowNum = 40
    for round1 in range(0, 11):
        print("--------------------------------------------", round1, "-----------------------------------------------")
        if round1 == 0:
            # Preparing matrix
            key = keys[rowNum:rowNum + 4]
            rowNum = rowNum - 4
            key = FormMatrix(key)
            addRoundKey = AddRoundKey(final_cipher_text, key)
            print("Add Round Key : ", addRoundKey)

            # LAST ROUND
        elif round1 == 10:
            inverseShiftRows = InverseShiftRows(addRoundKey)
            print("Inverse shift rows : ", inverseShiftRows)

            inverseSubBytes = InverseSubBytes(inverseShiftRows)
            print("Inverse Sub bytes : ", inverseSubBytes)

            # Preparing matrix
            key = keys[rowNum:rowNum + 4]
            rowNum = rowNum - 4
            key = FormMatrix(key)

            addRoundKey = AddRoundKey(inverseSubBytes, key)
            print("Add Round Key : ", addRoundKey)

        else:
            # THIS USES THE PREVIOUS addRoundKey GENERATED FROM Round 0
            inverseShiftRows = InverseShiftRows(addRoundKey)
            print("Inverse shift rows : ", inverseShiftRows)

            inverseSubBytes = InverseSubBytes(inverseShiftRows)
            print("Inverse Sub bytes : ", inverseSubBytes)

            # Preparing matrix that is w[36:39] matrix
            key = keys[rowNum:rowNum + 4]
            rowNum = rowNum - 4
            key = FormMatrix(key)
            print("Round Key : ", key)

            addRoundKey = AddRoundKey(inverseSubBytes, key)
            print("Add Round Key : ", addRoundKey)

            inverseMixColumns = GaloisField(addRoundKey, 1)
            print("Inverse mix column : ", inverseMixColumns)

            addRoundKey = inverseMixColumns

    print("DECRYPTION RESULT : ", addRoundKey)
    WriteFile("decryption.dec", addRoundKey)


if __name__ == "__main__":
    # READING KEY FROM A FILE
    Cipher_Key = ReadFile("aes.key")
    print("Cipher key is : ", Cipher_Key)

    # READING PLAIN TEXT FROM A FILE
    Plaintext = ReadFile("plainText.pt")
    print("PLain text is : ", Plaintext)

    # THIS FUNCTION RETURNS THE GENERATED KEYS
    keys = GenerateKeys(Cipher_Key)

    # STARTING TIME FOR ENCRYPTION
    EncryptionStart = time.time()
    # TAKE THE KEY AND PLAIN TEXT AND ENCRYPT IT
    CipherText = Encryption(Plaintext, keys)
    # ENDING TIME FOR ENCRYPTION
    EncryptionEnd = time.time()

    # STARTING TIME FOR DECRYPTION
    DecryptionStart = time.time()
    # TAKE THE KEY AND CIPHER TEXT AND PERFORM DECRYPTION
    Decryption(CipherText, keys)
    # ENDING TIME FOR DECRYPTION
    DecryptionEnd = time.time()

    print("Total time taken for encryption : ", EncryptionEnd - EncryptionStart)
    print("Total time taken for decryption : ", DecryptionEnd - DecryptionStart)

    # Cipher_Key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"
    # Plaintext = "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34"

    # Plaintext = "54 77 6F 20 4F 6E 65 20 4E 69 6E 65 20 54 77 6F"
    # Cipher_Key = "54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75"
