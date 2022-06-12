#!/usr/bin/python
import vpk, os, sys

# Terminal Colours
RED    = '\033[31m'
GREEN  = '\033[32m'
BRIGHT = '\033[1m'
CLEAR  = '\033[0m'

vpk_name = "Invicta.vpk"

compile_path = os.getcwd() + "/MAKE_VPK"
if os.path.exists(compile_path):
    NEWVPK = vpk.new("./MAKE_VPK")
    NEWVPK.save(vpk_name)
    print(f"File saved as {BRIGHT}{GREEN}{vpk_name}{CLEAR} in {os.getcwd()}{CLEAR}")
else:
    print(f"{RED}Folder not found.\nPlease create a folder named {BRIGHT}MAKE_VPK{CLEAR}{RED} and move files to compile inside it. {CLEAR}")