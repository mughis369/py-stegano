# py-stegano
*self-contained tool that can be used for covertmessaging. This tool is able to “hide” and retrieve ASCII text inside PNG files.*

This repo contains 4 modules 
-main.py
-StegEncode.py
-StegDecode.py
-png.py

main.py contains all the driver code to encode and decode messages from png files.
StegEncode.py consits of encode function which takes 3 arguments input_png, message_to_encode, output_png
StegDecode.py has one function that returns hidden message from the file passed to it
png.py - PNG encoder/decoder in pure Python

**Usage**

    This program have two modes (reading and writing) specified through the -w switch. 
    If the switch is not provided reading mode is assumed and this program dumps any text 
    found in the png file to standard output.
    The text to be inserted in the PNG file is specified by one of three methods:

    1 - using standard input to insert data
    2 - using -f switch to read data from file
    3 - using -t switch to read from text
    
    
**Examples**
```    
    python3 main.py input_file.png
    python3 main.py -w input.png -f input.txt output.png
    python3 main.py -w input.png -t 'random text' output.png
    python3 main.py -w input.png 'random text' output.png
```
