#!/usr/bin/python3
# writen by Philip

def uppercase(text):
    result = ""
    for char in text:
         if 'a' <= char <= 'z':
             result += chr(ord(char) -32)
         else:
             result += char
    print(result)

