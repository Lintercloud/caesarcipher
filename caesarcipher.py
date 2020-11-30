# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:42:29 2020

@author: Linter
"""

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encode =""
    for w in text:
        text_position = alphabet.index(w)
        new_position = text_position + shift
        while new_position > len(alphabet):
            new_position -= len(alphabet)     
        encode += alphabet[new_position]
    print(f"The encoded text is {encode}")
    
def decrypt(text, shift):
    decode =""
    for w in text:
        text_position = alphabet.index(w)
        new_position = text_position - shift
        while new_position > len(alphabet):
            new_position -= len(alphabet)     
        decode += alphabet[new_position]
    print(f"The dncoded text is {decode}")


#結合加密及解密版本
def caeser(text, shift, direction):
    end_code = ""
    if direction == "decode":
        shift *= -1
    for w in text:
        position = alphabet.index(w)
        new_position = position + shift
        while new_position > len(alphabet):
            new_position -= len(alphabet)
        end_code += alphabet[new_position]
    print(f"The {direction} text is :{end_code}")
    
        


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    if text not in alphabet:
        print("there can only put letter")
        continue
    shift = int(input("Type the shift number:\n"))

    caeser(text, shift, direction)
    play_again = input("Do you want to play again yes\ no: ").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        print("byebye")
        break
    