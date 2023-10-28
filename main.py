
#Author: יפתח

#Program nameהצפנה ראשונה

#Description:

#Date: 1/10/23

import sys
import os
import logging

LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/lucky.log'

MSG1= "My bounty is as boundless as the sea, My love as deep; " \
      "the more I give to thee, The more I have, for both are infinite."
INC1 = "48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,90," \
       "98,91,19,16,98,90,16,12,99,98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,16,98" \
       ",34,36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19,16,16,99,98,65,19,16,98,34,36,39,16,98,44,98" \
       ",19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,35,30,91,16,100,"

INPUT_CHAR = {'A':56, 'B':57, 'C':58, 'D':59, 'E':40, 'F':41, 'G':42, 'H':43, 'I':44, 'J':45,
                  'K':46, 'L':47, 'M':48, 'N':49, 'O':60, 'P':61, 'Q':62, 'R':63, 'S':64, 'T':65,
                  'U':66, 'V':67, 'W':68, 'X':69, 'Y':10, 'Z':11, 'a':12, 'b':13, 'c':14, 'd':15,
                  'e':16, 'f':17, 'g':18, 'h':19, 'i':30, 'j':31, 'k':32, 'l':33, 'm':34, 'n':35,
                  'o':36, 'p':37, 'q':38, 'r':39, 's':90, 't':91, 'u':92, 'v':93, 'w':94, 'x':95,
                  'y':96, 'z':97, ' ':98, ',':99, '.':100, ';':101, "'":102, '?':103, '!':104, ':':105, '':''}

OUTPUT_CHAR = { 56:'A', 57:'B', 58:'C', 59:'D', 40:'E', 41:'F', 42:'G', 43:'H', 44:'I', 45:'J',
                  46:'K', 47:'L', 48:'M', 49:'N', 60:'O', 61:'P', 62:'Q', 63:'R', 64:'S', 65:'T',
                  66:'U', 67:'V', 68:'W', 69:'X', 10:'Y', 11:'Z', 12:'a', 13:'b', 14:'c', 15:'d',
                  16:'e', 17:'f', 18:'g', 19:'h', 30:'I', 31:'j', 32:'k', 33:'l', 34:'m', 35:'n',
                  36:'o', 37:'p', 38:'q', 39:'r', 90:'s', 91:'t', 92:'u', 93:'v', 94:'w', 95:'x',
                  96:'y', 97:'z', 98:' ', 99:',', 100:'.', 101:';', 102:"'", 103:'?', 104:'!', 105:':', '':''}

def isvalid():
    if sys.argv[1] == 'encrypt' or sys.argv[1] == 'decrypt':
        return True
    else: return False

def incript():
    my_str = input('write a messege')
    str1 = ""
    for i in my_str:
        str1 += INPUT_CHAR[i]
        str1 += ','
    file = open("encrypted_msg.txt", 'w')
    file.write(str1)
    file.close()


def incriptAssert(my_str):
    str1 = ""
    for i in my_str:
        str1 += INPUT_CHAR[i]
        str1 += ','
    return str1

def decript():
    file = open("encrypted_msg.txt", 'r')
    str2 = file.read()
    enclist = list(str2.split(','))
    declist = []
    for j in enclist:
        if i != '':
            declist.append(OUTPUT_CHAR[j])
    print(declist)
def main():
    if (sys.argv[1]== 'encrypt'):
        incript()
    elif (sys.argv[1]== 'decrypt'):
        decript()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert isvalid()
    assert incriptAssert(MSG1) == INC1

    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
