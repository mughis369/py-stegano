#!/usr/bin/env python3

import png


def decode(filename):
    '''Reveal the binary data packed in the pixels

    (str) -> str
    filename - path of file to read data from
    
    This function accumulates the least significant bits of every
    pixel into the returned bytes object.
    '''
    
    try:
        reader = png.Reader(filename = filename)
        w, h, pixels, metadata = reader.read_flat()
        pixel_byte_width = 4 if metadata['alpha'] else 3 
        
        pixel_count = len(pixels)
        
        hidden_bits = ""
        for i in range(pixel_count):
            if i % pixel_byte_width == 0 and pixel_byte_width == 4:
                #skip when alpha channel is found
                continue
            else:
                hidden_bits += (bin(pixels[i])[2:][-1])

        hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

        message = ""
        for i in range(len(hidden_bits)):
            if message[-8:] == "$$halt$$":
                break
            else:
                message += chr(int(hidden_bits[i], 2))
        if "$$halt$$" in message:
            return message[:-8]
        else:
            return "No Hidden Message Found"

    except:
        return "ERROR extracting Hidden Message"
    
# filename = "output.png"
# decode(filename)
