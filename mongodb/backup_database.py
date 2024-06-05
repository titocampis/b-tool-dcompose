import os
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Command to copy the directory
command = "sudo rm -rf backup-db && sudo cp -r /var/lib/docker/volumes/b-tool-dcompose_mongodb_data/ backup-db/"

# Execute the command
result = subprocess.run(command, shell=True)

# Check if the command executed successfully
if result.returncode == 0:
    print(f"{bcolors.OKGREEN}Database backed up successfully on in {os.getcwd()}/backup-db{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}Something went wrong backing up the database in {os.getcwd()}/backup-db\n{result}{bcolors.ENDC}")
