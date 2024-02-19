import subprocess

import utilities as ut

# Command to copy the directory
command = "sudo cp -r /var/lib/docker/volumes/b-tool-dcompose_mongodb_data /home/acampos/"

# Execute the command
result = subprocess.run(command, shell=True)

# Check if the command executed successfully
if result.returncode == 0:
    print(f"{ut.bcolors.OKGREEN}Databse backed up successfully on /home/acampos/b-tool-dcompose_mongodb_data{ut.bcolors.ENDC}")
else:
    print(f"{ut.bcolors.FAIL}Something went wrong backing up the database in /home/acampos/b-tool-dcompose_mongodb_data\n{result}{ut.bcolors.ENDC}")