#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:42:42 2022
@author: nabil
"""
import cv2
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

namaFile = input("Nama file : ")
namaFileOutput = input("Tuliskan nama file setelah di konversi : ")

def awal(namaFile, namaFileOutput):
    
    try:
        img = cv2.imread(namaFile, 1)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray)
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
        final_img = cv2.divide(img_gray, 255 - img_smoothing, scale=256)
        cv2.imwrite(namaFileOutput, final_img)
        
    except:
        print('\n\nTuliskan nama file dengan benar!!                  ')
        sys.exit()
        

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    awal(namaFile, namaFileOutput)
    with Loader("Loading gambar mohon tunggu..."):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Save gambar", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()
    
img = cv2.imread(namaFileOutput, 1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

