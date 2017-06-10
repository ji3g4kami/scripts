#! /usr/bin/env python3
import pyperclip

copiedStr = pyperclip.paste()
copiedStr = copiedStr.split(':')
copiedStr = "\': \'".join(copiedStr)
copiedStr = copiedStr.split('\n')
copiedStr = "\',\n\'".join(copiedStr)
copiedStr = "\'" + copiedStr + "\'"

print(copiedStr)
pyperclip.copy(copiedStr)
