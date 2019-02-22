#Joshua Childs 02/14/2019 Valentines Day gift to myself
#Program that will append to .bash_profile and create an alias of current working directory
#Makes shortcut creating a bit quicker, although deleting unused shortcuts is still requires same old process.

import sys
import os

#must use os for hidden file, bash_profile
def write_to_bash_profile(alias,pwd):
    with open(os.path.expanduser('~/.bash_profile'),'a+') as f:
        f.write("\nalias " + alias + "='cd " + pwd + "'")


def _main_():
    #user defined alias
    alias = input("Enter Alias Name: ")
    pwd = sys.argv[1]
    write_to_bash_profile(alias,pwd)
	print("Update the bash_profile with 'confirm' command")

_main_()

