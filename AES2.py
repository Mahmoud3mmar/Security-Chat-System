s_box = ['1001', '0100', '1010', '1011',
         '1101', '0001', '1000', '0101',
         '0110', '0010', '0000', '0011',
         '1100', '1110', '1111', '0111']
inv_s_box = [
    '1010', '0101', '1001', '1011',
    '0001', '0111', '1000', '0101',
    '0110', '0010', '0000', '0011',
    '1100', '1110', '1111', '0111'
]

MultiplyTable = [
         ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
         ['2', '4', '6', '8', 'a', 'c', 'e', '3', '1', '7', '5', 'b', '9', 'f', 'd'],
         ['3', '6', '5', 'c', 'f', 'a', '9', 'b', '8', 'd', 'e', '7', '4', '1', '2'],
         ['4', '8', 'c', '3', '7', 'b', 'f', '6', '2', 'e', 'a', '5', '1', 'd', '9'],
         ['5', 'a', 'f', '7', '2', 'd', '8', 'e', 'b', '4', '1', '9', 'c', '3', '6'],
         ['6', 'c', 'a', 'b', 'd', '7', '1', '5', '3', '9', 'f', 'e', '8', '2', '4'],
         ['7', 'e', '9', 'f', '8', '1', '6', 'd', 'a', '3', '4', '2', '5', 'c', 'b'],
         ['8', '3', 'b', '6', 'e', '5', 'd', 'c', '4', 'f', '7', 'a', '2', '9', '1'],
         ['9', '1', '8', '2', 'b', '3', 'a', '4', 'd', '5', 'c', '6', 'f', '7', 'e'],
         ['a', '7', 'd', 'e', '4', '9', '3', 'f', '5', '8', '2', '1', 'b', '6', 'c'],
         ['b', '5', 'e', 'a', '1', 'f', '4', '7', 'c', '2', '9', 'd', '6', '8', '3'],
         ['c', 'b', '7', '5', '9', 'e', '2', 'a', '6', '1', 'd', 'f', '3', '4', '8'],
         ['d', '9', '4', '1', 'c', '8', '5', '2', 'f', 'b', '6', '3', 'e', 'a', '7'],
         ['e', 'f', '1', 'd', '3', '2', 'c', '9', '7', '6', '8', '4', 'a', 'b', '5'],
         ['f', 'd', '2', '9', '6', '4', 'b', '1', 'e', 'c', '3', '8', '7', '5', 'a']]
my_table = [
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
    ['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'b', 'a', 'd', 'c', 'f', 'e'],
    ['2', '3', '0', '1', '6', '7', '4', '5', 'a', 'b', '8', '9', 'e', 'f', 'c', 'd'],
    ['3', '2', '1', '6', '7', '6', '5', '4', 'b', 'a', '9', '8', 'f', 'e', 'd', 'c'],
    ['4', '5', '6', '7', '0', '1', '2', '3', 'c', 'd', 'e', 'f', '8', '9', 'a', 'b'],
    ['5', '4', '7', '6', '1', '0', '3', '2', 'd', 'c', 'f', 'e', '9', '8', 'b', 'a'],
    ['6', '7', '4', '5', '2', '3', '0', '1', 'e', 'f', 'c', 'd', 'a', 'b', '8', '9'],
    ['7', '6', '5', '4', '3', '2', '1', '0', 'f', 'e', 'd', 'c', 'b', 'a', '9', '8'],
    ['8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7'],
    ['9', '8', 'b', 'a', 'd', 'c', 'f', 'e', '1', '0', '3', '2', '5', '4', '7', '6'],
    ['a', 'b', '8', '9', 'e', 'f', 'c', 'd', '2', '3', '0', '1', '6', '7', '4', '5'],
    ['b', 'a', '9', '8', 'f', 'e', 'd', 'c', '3', '2', '1', '0', '7', '6', '5', '4'],
    ['c', 'd', 'e', 'f', '8', '9', 'a', 'b', '4', '5', '6', '7', '0', '1', '2', '3'],
    ['d', 'c', 'f', 'e', '9', '8', 'b', 'a', '5', '4', '7', '6', '1', '0', '3', '2'],
    ['e', 'f', 'c', 'd', 'a', 'b', '8', '9', '6', '7', '4', '5', '2', '3', '0', '1'],
    ['f', 'e', 'd', 'c', 'b', 'a', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    ]


invs_box = {
    "1001": "0000",
    "0100": "0001",
    "1010": "0010",
    "1011": "0011",
    "1101": "0100",
    "0001": "0101",
    "1000": "0110",
    "0101": "0111",
    "0110": "1000",
    "0010": "1001",
    "0000": "1010",
    "0011": "1011",
    "1111": "1110",
    "1100": "1100",
    "1110": "1101",
    "0111": "1111"
}




def sub_nibble(nibble):
    """Perform nibble substitution using AES S-box"""
    s_box = ['0110', '0101', '0011', '1010', '1101', '0001', '0100', '1000', '1100', '0111', '0000', '1110', '1011', '1001', '0010', '1111']
    idx = int(nibble, 2)  # convert nibble to integer index
    return s_box[idx]  # return corresponding value from S-box

def sbox_to_nibble(sbox_val):
    """Convert S-box value to nibble"""
    for i in range(16):
        nibble = format(i, '04b')
        if sub_nibble(nibble) == sbox_val:
            return nibble
    return None  # sbox_val is not a valid output of the AES S-box





def toBinary(a):
    decimal_num = int(a, 2)
    binary_num = bin(decimal_num)[2:].zfill(len(a))
    return binary_num

def XOR (a,b):
    decimal_num = int(a, 2)
    binary_num = bin(decimal_num)[2:].zfill(len(a))
    key_str = b
    key_num = int(key_str, 2)

    result_num = decimal_num ^ key_num
    result_str = bin(result_num)[2:].zfill(len(binary_num))
    return result_str

def todecimal(a):
    decimal_number = int(a, 2)
    return decimal_number
# print(toBinary("Hello world"))
def subniRotnib(a):
    first_byte4bit, second_byte4bit = split_binary_8bit(a)
    subnib_value1 = subnib(second_byte4bit, s_box)

    subnib_value2 = subnib(first_byte4bit, s_box)
    c = str(subnib_value1) + str(subnib_value2)
    c = toBinary(c)
    return c


def subnib(input_nib, s_box):
    # Convert the 4-bit input to a decimal integer
    input_int = int(input_nib, 2)
    # Get the corresponding subnib value from the S-box
    subnib = s_box[input_int]
    return subnib


def tostring(ciphertext):
    result_string = ""
    for string in ciphertext:
        result_string += string
    byte_list = [result_string[i:i + 8] for i in range(0, len(result_string), 8)]
    char_string = "".join([chr(int(byte, 2)) for byte in byte_list])
    return char_string


def split_binary_16bit(binary_string):
    first_byte = binary_string[0:8]
    second_byte = binary_string[8:16]
    return (first_byte, second_byte)

def split_binary_8bit(binary_string):
    first_byte = binary_string[0:4]
    second_byte = binary_string[4:8]
    return (first_byte, second_byte)

def Plain_to_Binary2(plaintext):
    binary_blocks = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext):
            # If there are two characters left in plaintext
            binary_block = format(ord(plaintext[i]), '08b') + format(ord(plaintext[i + 1]), '08b')
        else:
            # If there is only one character left in plaintext
            binary_block = format(ord(plaintext[i]), '08b') + '00000000'
        binary_blocks += binary_block

    # Pad the binary string with zeros if its length is not a multiple of 16
    while len(binary_blocks) % 16 != 0:
        binary_blocks += '0'

    # Return only the first 16 bits of the binary string
    return binary_blocks[:16]

def Plain_to_Binary(plaintext):
    binary_blocks = []
    for i in range(0, len(plaintext), 2):
        if i+1 < len(plaintext):
            # If there are two characters left in plaintext
            binary_block = format(ord(plaintext[i]), '08b') + format(ord(plaintext[i+1]), '08b')
        else:
            # If there is only one character left in plaintext
            binary_block = format(ord(plaintext[i]), '08b') + '00000000'
        binary_blocks.append(binary_block)
    return binary_blocks
def R1(a):
    first8bit, second8bit = split_binary_16bit(a)
    first4bitinfirst, second4bitinfirst = split_binary_8bit(first8bit)
    first4bitinsecond, second8bitinsecond = split_binary_8bit(second8bit)
    first4bitinfirst = subnib(first4bitinfirst, s_box)
    second4bitinfirst = subnib(second4bitinfirst, s_box)
    first4bitinsecond = subnib(first4bitinsecond, s_box)
    second8bitinsecond = subnib(second8bitinsecond, s_box)
    plaintextXor = str(first4bitinfirst) + str(second8bitinsecond) + str(first4bitinsecond) + str(second4bitinfirst)
    s00 = todecimal(first4bitinfirst)
    s10 = todecimal(second8bitinsecond)
    s01 = todecimal(first4bitinsecond)
    s11 = todecimal(second4bitinfirst)

    s00_ = my_table[int(MultiplyTable[1 - 1][s00 - 1], 16)][int(MultiplyTable[4 - 1][s10 - 1], 16)]
    s10_ = my_table[int(MultiplyTable[4 - 1][s00 - 1], 16)][int(MultiplyTable[1 - 1][s10 - 1], 16)]
    s01_ = my_table[int(MultiplyTable[1 - 1][s01 - 1], 16)][int(MultiplyTable[4 - 1][s11 - 1], 16)]
    s11_ = my_table[int(MultiplyTable[4 - 1][s01 - 1], 16)][int(MultiplyTable[1 - 1][s11 - 1], 16)]

    s00_ = bin(int(s00_,16))[2:].zfill(4)
    s10_ = bin(int(s10_,16))[2:].zfill(4)
    s01_ = bin(int(s01_,16))[2:].zfill(4)
    s11_ = bin(int(s11_,16))[2:].zfill(4)
    plaintextXor = str(s00_) + str(s10_) + str(s01_) + str(s11_)
    plaintextXor = toBinary(plaintextXor)
    return plaintextXor

def R2(a):
    first8bit, second8bit = split_binary_16bit(a)
    first4bitinfirst, second4bitinfirst = split_binary_8bit(first8bit)
    first4bitinsecond, second8bitinsecond = split_binary_8bit(second8bit)
    first4bitinfirst = subnib(first4bitinfirst, s_box)
    second4bitinfirst = subnib(second4bitinfirst, s_box)
    first4bitinsecond = subnib(first4bitinsecond, s_box)
    second8bitinsecond = subnib(second8bitinsecond, s_box)
    plaintextXor = str(first4bitinfirst) + str(second8bitinsecond) + str(first4bitinsecond) + str(second4bitinfirst)
    plaintextXor = toBinary(plaintextXor)
    return plaintextXor

def Key_Generate(a):
    binary_blocks = Plain_to_Binary(a)
    w0, w1 = split_binary_16bit('0100101011110101')
    c = subniRotnib(w1)

    first_byte_bin = toBinary(w0)

    xor = XOR(first_byte_bin, "10000000")

    w2 = XOR(xor, c)

    w3 = XOR(w2, w1)

    w4 = XOR(w2, "00110000")
    c1 = subniRotnib(w3)
    w4 = XOR(w4, c1)
    w5 = XOR(w4, w3)
    k0 = str(w0) + str(w1)
    k0 = toBinary(k0)

    k1 = str(w2) + str(w3)
    k1 = toBinary(k1)

    k2 = str(w4) + str(w5)
    k2 = toBinary(k2)

    return k0,k1,k2

def Decrypt(result_string, k0, k1, k2):
    cihpher = []
    for i in range(len(result_string)):
        output = XOR(result_string[i], k2)
        first8bit, second8bit = split_binary_16bit(output)
        first4bitinfirst, second4bitinfirst = split_binary_8bit(first8bit)
        first4bitinsecond, second8bitinsecond = split_binary_8bit(second8bit)

        first4bitinfirst = invs_box[first4bitinfirst]  # nibble1 = '1001'
        second4bitinfirst = invs_box[second4bitinfirst]  # nibble1 = '1001'
        first4bitinsecond = invs_box[first4bitinsecond]  # nibble1 = '1001'
        second8bitinsecond = invs_box[second8bitinsecond]  # nibble1 = '1001'
        plaintextXor = str(first4bitinfirst) + str(second8bitinsecond) + str(first4bitinsecond) + str(second4bitinfirst)
        plaintextXor = toBinary(plaintextXor)
        # round1

        plaintextXor = XOR(plaintextXor, k1)
        first8bit, second8bit = split_binary_16bit(plaintextXor)
        first4bitinfirst, second4bitinfirst = split_binary_8bit(first8bit)
        first4bitinsecond, second8bitinsecond = split_binary_8bit(second8bit)

        s00 = todecimal(first4bitinfirst)
        s10 = todecimal(second4bitinfirst)
        s01 = todecimal(first4bitinsecond)
        s11 = todecimal(second8bitinsecond)

        s00_ = my_table[int(MultiplyTable[9 - 1][s00 - 1], 16)][int(MultiplyTable[2 - 1][s10 - 1], 16)]
        s10_ = my_table[int(MultiplyTable[2 - 1][s00 - 1], 16)][int(MultiplyTable[9 - 1][s10 - 1], 16)]
        s01_ = my_table[int(MultiplyTable[9 - 1][s01 - 1], 16)][int(MultiplyTable[2 - 1][s11 - 1], 16)]
        s11_ = my_table[int(MultiplyTable[2 - 1][s01 - 1], 16)][int(MultiplyTable[9 - 1][s11 - 1], 16)]

        s00_ = bin(int(s00_, 16))[2:].zfill(4)
        s10_ = bin(int(s10_, 16))[2:].zfill(4)
        s01_ = bin(int(s01_, 16))[2:].zfill(4)
        s11_ = bin(int(s11_, 16))[2:].zfill(4)

        s00_ = invs_box[str(s00_)]
        s10_ = invs_box[str(s10_)]
        s01_ = invs_box[str(s01_)]
        s11_ = invs_box[str(s11_)]
        plaintextXor = str(s00_) + str(s11_) + str(s01_) + str(s10_)
        plaintextXor = toBinary(plaintextXor)

        # print(plaintextXor)
        plaintext = XOR(plaintextXor, k0)
        cihpher.append(plaintext)
    return cihpher

def Encrypt(plaintext, k0, k1, k2):
    ciphertext = []
    for i in range(len(plaintext)):
        plaintextXor = XOR(plaintext[i], k0)
        result = R1(plaintextXor)
        plaintextXor = XOR(result, k1)
        result = R2(plaintextXor)
        result = XOR(result, k2)
        ciphertext.append(result)
    return ciphertext


