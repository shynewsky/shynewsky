import sys
sys.stdin = open('input.txt')

dict = {
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

def hexa_to_binary(hexa):
    binary = ""
    for digit in hexa:
        binary += dict[digit]
    return binary

def cut_binary(bin):
    binary = []
    i = 0
    while i < len(bin):
        if bin[i:i+7] == "0000000":
            i += 4
        else:
            binary += [bin[i:i+7]]
            i += 7
    return binary

def binary_to_decimal(bin): # pow, bin은 예약어므로 변수명 사용은 피하자
    decimal = 0
    pow = 0
    for digit in reversed(bin):
        if digit == '1':
            decimal += 2 ** pow
        pow += 1
    # for digit in bin:
    #     decimal *= 2
    #     if digit == '1':
    #         decimal += 1
    return decimal

T = int(input())
for test_case in range(1,T+1):
    string = input()
    bin_str = hexa_to_binary(string)
    bin_list = cut_binary(bin_str)
    dec_list = [binary_to_decimal(i) for i in bin_list]

    print(bin_list)
    print(dec_list)
