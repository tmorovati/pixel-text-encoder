# Simple Image Text Hiding in Python

This is a small Python project that hides text inside an image by modifying selected pixel values, then reads that hidden text back from the encoded image.

The project was built as a hands-on exercise in working with images, basic encoding logic, file handling, and simple command-line interaction in Python.

## What the project does

- Encodes a text message into an image
- Saves the encoded image as a PNG file
- Decodes the hidden text from an encoded image
- Supports either:
  - a user-provided image URL, or
  - a randomly fetched image

## How it works

The program stores each character of the input text in the red channel of selected image pixels.  
During decoding, it reads those pixel values back and reconstructs the original text.

A null character (`\0`) is added at the end of the message to mark where the hidden text stops.

## Important note

This project is a **basic steganography demonstration**, not a secure encryption tool.

It is meant for learning and experimentation, not for privacy, security, or serious data hiding use cases.

## Why PNG is used

The encoded image is saved as a PNG file because PNG preserves exact pixel values.

Formats like JPEG use lossy compression, which changes pixel values and can corrupt the hidden text.


## Requirements
Python 3.x
Pillow
requests

## Install dependencies with:

pip install -r requirements.txt
How to run

## Run the program from the terminal:

python main.py

You will then be able to choose between:

1. Encoding text into an image
2. Decoding text from an image

# Example workflow
## Encode
- Enter a text message
- Choose whether to use your own image URL or a random image
- The program saves the output as encoded_img.png

## Decode
- Provide the path to the encoded image
- The program reads the hidden message and prints it


# This project helped me practice:

- image processing with Pillow
- working with HTTP requests in Python
- encoding and decoding logic
- error handling
- organizing a small Python project into separate files

# License

This project is for learning and personal development. You can adapt it further based on your own needs.