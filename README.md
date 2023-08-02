# Steganography Project

![Steganography](images/Comparison.png) 
<p align="center">One of this images contain the message: Teddy bear is waiting for you at the front door of belmont hotel!</p>

## Introduction
Steganography Project is a Python-based implementation of steganography, which allows you to hide secret messages within image files using the Least Significant Bit (LSB) technique. Steganography is the art of concealing sensitive information within another seemingly innocent medium to avoid detection. This project aims to provide a simple and user-friendly tool for encoding and decoding hidden messages in images.

## Technical Significance
Steganography has various practical applications, including secure communication, watermarking, and digital forensics. Your project explores the following technical aspects:

1. **LSB Steganography**: The project demonstrates the implementation of LSB steganography, which involves hiding data in the least significant bits of an image, causing minimal visual impact to the human eye.

2. **Image Processing**: The project utilizes the OpenCV library (cv2) in Python to read and manipulate image pixels for encoding and decoding secret messages.

3. **Binary Conversion**: The functions `str2bin` and `bin2str` are used to convert text to binary and binary back to text, respectively, for encoding and decoding purposes.

4. **Data Encryption**: The project uses the `cryptography.fernet` module to provide an optional password protection during encoding, enhancing the security of the hidden message.

5. **Error Handling**: The project includes custom exceptions (`FileNotThereError`, `DataError`, and `PasswordError`) to handle various errors gracefully.

## Functionality
The Steganography Project provides the following functionalities:

1. **Encoding**: The `encode` function allows you to encode a secret message into a cover image and generate a stego-image.

2. **Decoding**: The `decode` function allows you to extract a hidden message from a stego-image.

3. **Password Protection (Optional to be updated)**: During encoding, you can choose to use a password to enhance security and prevent unauthorized access to the hidden message.

## Usage
To encode a message into an image, run the script and choose option 1:
```bash
python menu.py
```

License
This project is licensed under the MIT License - see the LICENSE file for details.

Note
Please note that this project may have limitations and should not be used for critical security purposes. It is meant for educational and demonstration purposes only.
