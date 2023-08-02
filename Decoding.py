from cv2 import imread
from Encoding import *


def bin2str(string):
    return ''.join(chr(int(string[i:i+8],2)) for i in range(len(string))[::8])

def decode(input_filepath):
    result,extracted_bits,completed,number_of_bits = '',0,False,None
    total_bits = 0
    img = imread(input_filepath) #open the image


    if img is None:
        raise FileNotThereError("The image file '{}' is inaccessible".format(input_filepath)) 
    height,width = img.shape[0],img.shape[1]


    #Run 2 nested for loops to traverse all the pixels of the whole image in left to right, top to bottom fashion
    for i in range(height):
        for j in range(width):
            for k in img[i,j]: #for values in pixel RGB tuple
                result += str(k%2) #extract the LSB of RGB values of each pixel
                extracted_bits += 1
                total_bits += 1

                if extracted_bits == 32 and number_of_bits == None: # first 32 extracted_bits are the data size.
                    number_of_bits = int(result,2)*8 #number of bits to extract from the image
                    result = ''
                    extracted_bits = 0

                elif (number_of_bits != None and total_bits == number_of_bits + 32): #if all required bits are extracted, mark the process as completed
                    completed = True
                    break
            if completed:
                break
        if completed:
            break
        
    return bin2str(result) #decoding the data to string formation from binary.