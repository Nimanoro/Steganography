from cv2 import imread,imwrite
from base64 import urlsafe_b64encode
from hashlib import md5
from cryptography.fernet import Fernet

    
def str2bin(string):
	return ''.join((bin(ord(i))[2:]).zfill(8) for i in string)

def encode(input_filepath,text,output_filepath):

    data = text


    data_length = bin(len(data))[2:].zfill(32) #get length of data to be encoded
    bin_data = iter(data_length + str2bin(data)) #add length of data with actual data and get the binary form of it


    img = imread(input_filepath,1) #read the cover image


    if img is None:
        raise FileNotThereError("The image file '{}' is inaccessible".format(input_filepath)) 
    

    height,width = img.shape[0],img.shape[1] 
    encoding_capacity = height*width*3 #maximum number of bits of data that the cover image can hide.


    total_bits = 32+len(data)*8 #total bits of data plus 32 bits for lentgh
    if total_bits > encoding_capacity:
        raise DataError("The data size is too big to fit in this image!") 
    
    completed = False
    modified_bits = 0
    
    #Run 2 nested for loops to traverse all the pixels of the whole image in left to right, top to bottom fashion
    for i in range(height):
        for j in range(width):
            pixel = img[i,j] 
            
            for k in range(3): #get next 3 bits from the binary data that is to be encoded in image
                try:
                    x = next(bin_data)

                except StopIteration: #if there is no data to encode, mark the encoding process as completed
                    completed = True
                    break

                if x == '0' and pixel[k]%2==1: 
                    pixel[k] = 0 #change LSB from 1 to 0
                    modified_bits += 1 #increment the modified bits count

                elif x=='1' and pixel[k]%2==0: 
                    pixel[k] = 1 #change LSB from 0 to 1
                    modified_bits += 1 #increment the modified bits count

            if completed:
                break
        if completed:
            break

    written = imwrite(output_filepath,img) #create a new image with the modified pixels
    if not written:
        raise FileNotThereError("Failed to write image '{}'".format(output_filepath))
    modified_bits_percent = (modified_bits/encoding_capacity)*100 #calculate how many bits of the original image are changed in order to encode the secret message and calculate the percentage of data loss from it
    return modified_bits_percent



class FileNotThereError(Exception):
    pass

class DataError(Exception):
    pass

class PasswordError(Exception):
    pass