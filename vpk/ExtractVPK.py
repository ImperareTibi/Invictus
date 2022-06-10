#!/usr/bin/python
import vpk, os

# Terminal Colours
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
CYAN   = '\033[36m'
BRIGHT = '\033[1m'
CLEAR  = '\033[0m'

vpk_file_name = "Invicta.vpk"

decompiled_path = os.getcwd() + "/DECOMPILED"
if os.path.exists("./Invicta.vpk"):
    VPK = vpk.open(vpk_file_name)

    if not os.path.exists(decompiled_path):
        os.mkdir(decompiled_path) # Create DECOMPILED folder if it doesn't exist.

    for path in VPK:
        file = VPK.get_file(path)
        full_path = decompiled_path + "/" + path

        if not os.path.exists(full_path):
            dir = path.split("/")[:-1]
            file_dir = ""
            for folder in dir:
                file_dir += folder + "/"
                if not os.path.exists(f"{decompiled_path}/{file_dir}"):
                    os.mkdir(f"{decompiled_path}/{file_dir}")
            print(f"{BRIGHT}Extracting: {CLEAR}{BRIGHT}{YELLOW}{vpk_file_name}/{path}{CLEAR}{BRIGHT}\nto {YELLOW}{decompiled_path}/{path}{CLEAR}")
            status = os.path.exists(decompiled_path+'/'+file_dir)
            print(f"{BRIGHT}Status: {BRIGHT}{GREEN}{status}{CLEAR}", end="\n\n")
        else:
            print(f"""
    {BRIGHT}File: {YELLOW}File.vpk/{path}
    {CYAN}Exists:{BRIGHT}{GREEN} {os.path.exists(full_path)}
    {CYAN}Path: {YELLOW}{full_path}{CLEAR}""")
        file.save(f"{decompiled_path}/{path}")
else:
    print(f"{RED}VPK file not found.\nPlease rename your vpk file to {BRIGHT}{RED}File.vpk{CLEAR} {RED}and try again.{CLEAR}")