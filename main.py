#!/usr/bin/env python3
import argparse
import os
from StegEncode import encode
from StegDecode import decode

def read_text(text):
    '''str -> str
    returns string data from file if passed string is valid filepath else
    returns the text passed as perameter'''
    if not os.path.isfile(text):
        return text
    return read_from_file(text)

def read_from_file(filename):
    '''Read and return text from file

    str -> str
    
    filename - name of the text file to extract text from
    returns string data from file if passed string is valid filepath else
    returns the text passed as perameter'''
    f = open(filename)
    s = f.read()
    f.close()
    return s

class Parser():
    def __init__(self):
        '''NoneType -> NoneType
        Initialize argparse parser, parse and store the arguments to 
        args variable'''

        example_text = """example:

        python3 main.py input_file.png
        python3 main.py -w input.png -f input.txt output.png
        python3 main.py -w input.png -t 'random text' output.png
        python3 main.py -w input.png 'random text' output.png
        """
        
        usage = """
        This program have two modes (reading and writing) specified through the -w switch. 
        If the switch is not provided reading mode is assumed and this program dumps any text 
        found in the png file to standard output.
        The text to be inserted in the PNG file is specified by one of three methods:
        
        1 - using standard input to insert data
        2 - using -f switch to read data from file
        3 - using -t switch to read from text"""

        parser = argparse.ArgumentParser(
            prog = "Stegnographer",
            allow_abbrev = True,
            description = "self-contained tool that can be used for covertmessaging. This tool is able to “hide” and retrieve ASCII text inside PNG files.",
            usage = usage,
            epilog = example_text,
            formatter_class = argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-w", help = "this switch sets the program to write mode", type = str)
        parser.add_argument("-f", help = "filename to read data", type = str)
        parser.add_argument("-t", help = "string to be inserted", type = str)
        parser.add_argument("stdin", help = "passing input from stdin", nargs = "?", type = str)
        parser.add_argument("stream", help = "input or output file", type = str)
        self.args = parser.parse_args()

def run():
    rtn_msg = ""
    parser = Parser()
    if parser.args.w:
        if parser.args.f:
            print("InputPng[{}], InputTxt[{}], Output[{}]".format(parser.args.w, read_text(parser.args.f), parser.args.stream))
            rtn_msg = encode(parser.args.w, read_text(parser.args.f), parser.args.stream)
        elif parser.args.t:
            print("InputPng[{}], InputTxt[{}], Output[{}]".format(parser.args.w, parser.args.t, parser.args.stream))
            rtn_msg = encode(parser.args.w, parser.args.t, parser.args.stream)
        elif parser.args.stdin:
            print("InputPng[{}], InputTxt[{}], Output[{}]".format(parser.args.w, parser.args.stdin, parser.args.stream))
            rtn_msg = encode(parser.args.w, parser.args.stdin, parser.args.stream)
        else:
            rtn_msg = "argument missing!"
    else:
        print("selected file[{}] to read data".format(parser.args.stream))
        rtn_msg = decode(parser.args.stream)

    print(rtn_msg.strip())

run()