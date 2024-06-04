import subprocess

import utils.utilities as ut

# Command to copy the directory
command = "rm -rf /var/lib/docker/volumes/b-tool-dcompose_mongodb_data && sudo cp -r ./backup-db /var/lib/docker/volumes/b-tool-dcompose_mongodb_data"

control = ''
while control.lower() != 'override-database':
    control = input(f"{ut.bcolors.WARNING}Are you sure do you want to override the database? This action will be irreversible\nType 'override-database' to continue: / 'n' to abort: {ut.bcolors.ENDC}")
    if control.lower() == 'n':
        print(f"{ut.bcolors.WARNING}Exiting the execution{ut.bcolors.ENDC}")
        exit(1)

# Execute the command
result = subprocess.run(command, shell=True)

# Check if the command executed successfully
if result.returncode == 0:
    print(f"{ut.bcolors.OKGREEN}Database exported successfully on /home/acampos/b-tool-dcompose_mongodb_data{ut.bcolors.ENDC}")
else:
    print(f"{ut.bcolors.FAIL}Something went wrong exporting the database in /home/acampos/b-tool-dcompose_mongodb_data\n{result}{ut.bcolors.ENDC}")
