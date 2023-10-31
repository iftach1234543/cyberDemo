# Author: יפתח

# Program nameהצפנה ראשונה

# Description:

# Date: 1/10/23

import sys
import os
import logging

LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/lucky.log'

MSG1 = "My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, for both are infinite."

MSG2 = "Don't waste your love on somebody, who doesn't value it."

ENC1 = "48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,90,98,91,19,16,98,90,16,12,99," \
      "98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19," \
      "16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,35,30,91,16,100"

ENC2 = "59,36,35,102,91,98,94,12,90,91,16,98,96,36,92,39,98,33,36,93,16,98,36,35,98,90,36,34,16,13,36,15,96,99,98,94,19,36,98,15,36,16,90,35,102," \
      "91,98,93,12,33,92,16,98,30,91,100"

INC_CHAR = {"A": 56, "B": 57, "C": 58, "D": 59, "E": 40, "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46,
                "L": 47, "M": 48,
                "N": 49, "O": 60, "P": 61, "Q": 62, "R": 63, "S": 64, "T": 65, "U": 66, "V": 67, "W": 68, "X": 69,
                "Y": 10, "Z": 11,
                "a": 12, "b": 13, "c": 14, "d": 15, "e": 16, "f": 17, "g": 18, "h": 19, "i": 30, "j": 31, "k": 32,
                "l": 33, "m": 34,
                "n": 35, "o": 36, "p": 37, "q": 38, "r": 39, "s": 90, "t": 91, "u": 92, "v": 93, "w": 94, "x": 95,
                "y": 96, "z": 97,
                " ": 98, ",": 99, ".": 100, ";": 101, "'": 102, "?": 103, "!": 104, ":": 105}

DEC_CHAR = {}
for key, value in INC_CHAR.items():
    DEC_CHAR[value] = key


def isvalid():
    """"
    the function check if the parameter is valid
    """
    if sys.argv[1] == 'encrypt' or sys.argv[1] == 'decrypt':
        return True
    else:
        logging.error("the parameter didn't work")
        return False


def incript():
    """"
    the function get a message encript it and put it inside a  file
    """
    my_message = input('write a message')
    logging.debug('write a message' + my_message)
    inc_list = []
    for i in my_message:
        inc_list.append(str(INC_CHAR[i]))
    inc_list = ','.join(inc_list)
    logging.debug(inc_list)
    file = open("encrypted_msg.txt", 'w')
    file.write(inc_list)
    file.close()


def incript_Assert(my_message):
    """"
    the function gets a message in order to check if the dictionery is right
    """
    inc_list = []
    for i in my_message:
        inc_list.append(str(INC_CHAR[i]))
    inc_list = ','.join(inc_list)
    return inc_list


def decript():
    """"
    the function open a file with an encripted nessage and decript it
    """
    file = open("encrypted_msg.txt", 'r')
    temp = file.read()
    logging.debug(temp)
    what_to_dec = temp.split(",")
    dec_message = ""
    for i in what_to_dec:
        dec_message += DEC_CHAR[int(i)]
    logging.debug(dec_message)
    print(dec_message)


def main():
    logging.debug(INC_CHAR)
    logging.debug(DEC_CHAR)
    if sys.argv[1] == 'encrypt':
        incript()
    elif sys.argv[1] == 'decrypt':
        decript()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert  isvalid()
    assert incript_Assert(MSG1) == ENC1
    assert incript_Assert(MSG2) == ENC2
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
