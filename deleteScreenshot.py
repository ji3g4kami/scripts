#! /usr/bin/env python3
import os, sys

os.chdir('/Users/Dengli/Desktop')

if len(sys.argv) == 1:
	for filename in os.listdir():
	    if filename.startswith("螢幕快照"):
	        print(filename)
	        os.unlink(filename)

else:
	pic = sys.argv[1]
	for filename in os.listdir():
	    if filename.endswith(pic):
	        print(filename)
	        os.unlink(filename)