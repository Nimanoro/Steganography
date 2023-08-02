from Decoding import *
from Encoding import *


if __name__ == "__main__":

    ch = int(input('What do you want to do?\n\n1.Encrypt\n2.Decrypt\n\nInput(1/2): '))
    if ch == 1:
        ip_file = input('\nEnter cover image name(path)(with extension): ')
        text = input('Enter secret data: ')
        op_file = input('Enter output image name(path)(with extension): ')
        try:
            loss = encode(ip_file,text,op_file)
        except FileNotThereError as fe:
            print("Error: {}".format(fe))
        except DataError as de:
            print("Error: {}".format(de))
        else:
            print('Encoded Successfully!\nImage Data Loss = {:.5f}%'.format(loss))
    elif ch == 2:
        ip_file = input('Enter image path: ')
        try:
            data = decode(ip_file)
        except FileNotThereError as fe:
            print("Error: {}".format(fe))
        else:
            print('Decrypted data:',data)
    else:
        print('Wrong Choice!')