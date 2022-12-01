substitutionBox = [
    ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
    ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
    ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
    ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
    ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
    ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
    ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
    ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
    ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
    ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
    ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
    ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
    ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
    ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
    ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
    ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]
]

inverseSubstitutionBox = [
    ["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"],
    ["7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb"],
    ["54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"],
    ["08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25"],
    ["72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"],
    ["6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84"],
    ["90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06"],
    ["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b"],
    ["3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"],
    ["96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e"],
    ["47", "f1", "1a", "71", "1d", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b"],
    ["fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"],
    ["1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f"],
    ["60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"],
    ["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61"],
    ["17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]
]
count = 0


# JUST USED FOR PREPROCESSING
# BUILD A MATRIX FROM A STRING
def Initiate(cipherKey):
    keys = []
    w = []
    str1 = ""
    for i in range(0, len(cipherKey)):
        if cipherKey[i] == " ":
            if len(str1) == 2:
                w.append(str1)
                str1 = ""
                if len(w) == 4:
                    keys.append(w)
                    w = []
        else:
            str1 = str1 + cipherKey[i]
        if i + 1 >= len(cipherKey):
            w.append(str1)
            keys.append(w)

    return keys


# ROTATING OF THE WORD BY THE FACTOR EQUAL TO NUMBER OF BYTES
def RotWord(temp, bytes=2):
    word = temp[bytes:]
    word = word + temp[0:bytes]
    return word


# GET SUBSTITUTION BOX VALUE
def GetBoxValue(temp):
    row = int(temp[0], 16)
    column = int(temp[1], 16)
    return substitutionBox[row][column]


# SUBSTITUTE A VALUE AFTER GETTING FROM THE BOX
def SubWord(temp):
    result = ""
    str1 = ""
    for i in range(0, len(temp)):
        str1 = str1 + temp[i]
        # If two character combined
        if len(str1) == 2:
            result = result + GetBoxValue(str1)
            str1 = ""
    return result


# TAKE TWO NUMBER AND PERFORM XOR
def PerformXOR(number1, number2):
    result = int(number1, 16) ^ int(number2, 16)

    return hex(result)


def XorRcon(temp, binary):
    result = PerformXOR(temp, binary)

    # If the user wants to get rid of the suffix '0b' at the start
    return result[2:]


def TempXor(present, less):
    less = "".join(less)

    # Performing XOR
    result = PerformXOR(present, less)
    # Returning after taking XOR
    result = result[2:]

    # APPENDING MORE ZEROS AT THE LEFT SIDE IF LESS THAN EIGHT ZEROS

    if len(result) < 8:
        while True:
            print("Appending")
            result = "0" + result
            if len(result) == 8:
                break

    return result


def FormMatrix(temp):
    final = [
        [],
        [],
        [],
        []
    ]

    for i in range(0, len(temp)):
        for j in range(0, len(temp[i])):
            final[j].append(temp[i][j])

    return final


def SubBytes(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = GetBoxValue(matrix[i][j])

    return matrix


def ShiftRows(matrix):
    shiftMatrix = []
    for i in range(0, len(matrix)):
        # Converting list to string for shifting bytes
        temp = "".join(matrix[i])
        # Now shifting bytes
        shiftResult = RotWord(temp, i * 2)

        w = []
        str1 = ""
        for j in range(0, len(shiftResult)):

            # Appending character by character to the string
            str1 = str1 + shiftResult[j]

            if len(str1) == 2:
                w.append(str1)

                # Emptying the string for storing next two character
                str1 = ""

        shiftMatrix.append(w)

    return shiftMatrix


# ***************************************************************************************************
# ////////////////////////////////////// GALOIS FIELD  //////////////////////////////////////////////
# ***************************************************************************************************
# THIS FUNCTION TAKES A STRING AS ARGUMENT AND APPEND BITS IF THEY ARE LESS
def Complete8Bits(binary):
    # IF 8 BITS NOT PRESENT
    if len(binary) < 8:
        while True:
            binary = "0" + binary
            if len(binary) == 8:
                break
    return binary


# THIS FUNCTION TAKES A HEXADECIMAL(STRING) NUMBER AND RETURNS A BINARY(STRING) OF IT
def getBinary(temp):
    # Convert HEX TO BINARY
    binary = bin(int(temp, 16)).zfill(0)

    # IF THE USER WANTS TO GET RID OF THE SUFFIX '0b' AT THE START
    binary = binary[2:]
    result = Complete8Bits(binary)

    return result


# THIS FUNCTION CONVERTS A BINARY NUMBER TO DECIMAL
def BinToHex(n):
    # CONVERT BINARY TO INT
    num = int(n, 2)

    # CONVERT INT TO HEXADECIMAL
    hex_num = hex(num)

    return hex_num


# THIS FUNCTION TAKES TWO NUMBERS AS ARGUMENT AND PERFORM XOR
def OperationXor(number1, number2):
    # TAKING XOR
    result = int(number1, 16) ^ int(number2, 16)

    result = hex(result)
    result = result[2:]
    result = Complete8Bits(result)
    return result


# THIS FUNCTION WILL TAKE NUMBERS AND THEN  MAKE THE GALLIOS FIELD MULTIPLICATION
def multiply(fx, gx):
    # FIRST OCCURRENCE OF 1 FROM LEFT SIDE
    index = gx.find("1")
    index = (len(gx) - 1) - index

    # APPENDING ALL THE RESULTS
    values = []
    values.append(fx)
    for k in range(0, index):
        # IF LEFT MOST BIT IS (0) THAN ONLY PERFORM THE LEFT SHIFT
        if fx[0] == "0":
            fx = fx[1:]
            fx = fx + "0"
            values.append(fx)

        # IF LEFT MOST BIT IS (1) THAN  PERFORM THE LEFT SHIFT AND XOR
        else:
            fx = fx[1:]
            fx = fx + "0"
            # TAKING X0R
            const = "00011011"
            fx = OperationXor(fx, const)
            values.append(fx)

    values.reverse()

    # MAKING A LIST OF LENGTH 8 EQUAL TO g(x)
    while True:
        if len(values) == 8:
            break
        values.insert(0, "00000000")
    # print("Values : ", values)

    # TAKING XOR OF ALL THE VALUES AT THE END
    result = "00000000"
    for i in range(0, len(gx)):
        if gx[i] == "1":
            result = OperationXor(values[i], result)

    return result


def GaloisField(matrix, comp):
    if comp == 0:
        const = [
            ["02", "03", "01", "01"],
            ["01", "02", "03", "01"],
            ["01", "01", "02", "03"],
            ["03", "01", "01", "02"]
        ]
    else:
        const = [
            ["0E", "0B", "0D", "09"],
            ["09", "0E", "0B", "0D"],
            ["0D", "09", "0E", "0B"],
            ["0B", "0D", "09", "0E"]
        ]
    final = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    finalValue = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):

            # FOR MATRIX MULTIPLICATION
            for k in range(0, 4):
                # print(const[i][k], " X ", matrix[k][j])
                #
                gx = getBinary(const[i][k])
                fx = getBinary(matrix[k][j])
                result = multiply(fx, gx)
                finalValue.append(result)

            # TAKING X0R OF ALL THE VALUES
            result = "00000000"
            for k in range(0, len(finalValue)):
                result = OperationXor(finalValue[k], result)

            # print("Result : ", BinToHexa(result))

            # CONVERTING BINARY TO HEXADECIMAL
            # If the user wants to get rid of the suffix '0b' at the start
            final[i][j] = BinToHex(result)[2:]
            finalValue = []

    return final


def GetInverseBoxValue(temp):
    row = int(temp[0], 16)
    column = int(temp[1], 16)
    return inverseSubstitutionBox[row][column]


def AddRoundKey(mixcol, key):
    result = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(len(key)):
        for j in range(len(key[0])):
            value = OperationXor(mixcol[i][j], key[i][j])
            result[i][j] = value[6:]

    return result


def InverseSubBytes(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = GetInverseBoxValue(matrix[i][j])

    return matrix


def CircularShift(temp, bytes=2):
    stop = len(temp) - bytes
    word = temp[0:stop]
    word = temp[stop:] + word

    return word


def InverseShiftRows(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = transform(matrix[i][j])

    shiftMatrix = []

    for i in range(0, len(matrix)):
        # Converting list to string for shifting bytes
        temp = "".join(matrix[i])
        # Now shifting bytes
        shift_result = CircularShift(temp, i * 2)
        w = []
        str1 = ""
        for j in range(0, len(shift_result)):
            # Appending character by character to the string
            str1 = str1 + shift_result[j]

            if len(str1) == 2:
                w.append(str1)
                # Emptying the string for storing next two character
                str1 = ""

        shiftMatrix.append(w)

    return shiftMatrix


# THIS FUNCTION COMPLETE THE TWO HEX NUMBER
def transform(hexa_number):
    if len(hexa_number) == 2:
        return hexa_number
    else:
        new_hex = "0" + hexa_number
        return new_hex
