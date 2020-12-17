#!/usr/bin/env python3

import png


def encode(png_in, message, png_out):
    '''Hides the data in a PNG
    
    (str, str, str) -> str
    
    png_in - file path to suitable carrier PNG
    png_out - file path for the PNG with the data hidden inside
    bindata - the bytes to be encoded
    '''

    try:    
        # adding delimiter (“$$halt$$") at the end of the secret message
        message += "$$halt$$"

        # reading image properties and pixel stream from png_in  
        reader = png.Reader(filename = png_in)
        w, h, pixels, metadata = reader.read_flat()
        
        # checks to tackle the alpha channel if image has one
        pixel_byte_width = 4 if metadata['alpha'] else 3 
        alpha_channel = True if metadata['alpha'] else False

        # encoding message to binary
        b_message = ''.join([format(ord(i), "08b") for i in message])
        
        # pixel related calculations
        req_pixels = len(b_message)
        pixel_count = len(pixels)
        total_pixels = pixel_count // pixel_byte_width
        
        if total_pixels > req_pixels: # input file sanity check
            index = 0

            #iterating over the list of pixels from image
            for i in range(pixel_count):
                if i % pixel_byte_width == 0 and pixel_byte_width == 4:
                    #skip when alpha channel is found
                    continue
                else:
                    if index < req_pixels:
                        # encoding hidden message to lsb of pixel stream
                        pixels[i] = int(bin(pixels[i])[2:9] + b_message[index], 2)
                        index += 1
        else:
            return "ERROR: Need larger file size"
        
        # writing new file containing hidden message as output file
        output = open(png_out, 'wb')
        writer = png.Writer(w, h, alpha = alpha_channel, greyscale = False)
        writer.write_array(output, pixels)
        output.close()
        return "Message '{}' encoded to {}".format(message[:-8], png_out)
    except:
        return "Error processing given image and message"

    
# png_in = 'input.png'
# message = "hello"
# png_out = "output.png"

# encode(png_in, message, png_out)
