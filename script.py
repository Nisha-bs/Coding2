#!/usr/bin/env python3

import os
import shutil

with open("./remove.txt", "r") as f:

     s = f.read()
     e =""
     for i in s:
         if i !="\n":
            e+=i
         else:
             print(" ".join(e.split(" ")[-2:]))
             try:
               cmd = "rm -r "+" ".join(e.split(" ")[-2:])
               os.remove(cmd)
             except:
               continue
             e=""







