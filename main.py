# This implementation of AIXItl will have access to the pixels of a computer monitor for its environment.
# The mouse and keyboard are potential actions from the action set. We want to observe the algorithm learning to learn
# from these premises.

import math
import cmath

import string
import random
import pyautogui

from pynput.keyboard import Key, Controller

def main():
    keyboard = Controller()
    print(type(string.ascii_letters))
    for i in range(0, 26):
        x = list()
        b = string.ascii_letters[i]
        print(b)
        
    #Set the lifetime of the agent to be 1000000 seconds.
    #Infinite lifetime agents are lazy!
    tinf = 1000000
    while True:
        a = set(b)
    

    #a = set(keyboard.press(string.ascii_letters)).Union(set(keyboard.release(string.ascii_letters)))
    #print(a)a

    t=0
  
if __name__ == "__main__":
  main()
