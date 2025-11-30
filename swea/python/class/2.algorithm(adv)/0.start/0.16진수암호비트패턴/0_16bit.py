import sys
sys.stdin = open('input.txt')

dict_hex = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

dict_code = {
    0 : '001101',
    1 : '010011',
    2 : '111011',
    3 : '110001',
    4 : '100011',
    5 : '110111',
    6 : '001011',
    7 : '111101',
    8 : '011001',
    9 : '101111',
}

def hexa_to_binary(hexa):
    binary = ""
    for digit in hexa:
        binary += dict_hex[digit]
    return binary

def find_secret_code(binary):
    result = []
    idx = 0

    while idx < len(binary):

        for key, value in dict_code.items():
            if binary[idx:idx+6] == value:
                result += [key]
                idx += 6
                break
        else:
            idx += 1

    return result

T = int(input())
for test_case in range(1, T+1):
    string = input()
    bin_str = hexa_to_binary(string)
    key_list = find_secret_code(bin_str)
    print(f'#{test_case}', *key_list)

