import os
import subprocess

import utilities as ut

# Command to copy the directory
command = "sudo rm -rf backup-db && sudo cp -r /var/lib/docker/volumes/b-tool-dcompose_mongodb_data/ backup-db/"

# Execute the command
result = subprocess.run(command, shell=True)

# Check if the command executed successfully
if result.returncode == 0:
    print(f"{ut.bcolors.OKGREEN}Database backed up successfully on in {os.getcwd()}/backup-db{ut.bcolors.ENDC}")
else:
    print(f"{ut.bcolors.FAIL}Something went wrong backing up the database in {os.getcwd()}/backup-db\n{result}{ut.bcolors.ENDC}")
