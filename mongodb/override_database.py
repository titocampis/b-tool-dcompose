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
command = "rm -rf /var/lib/docker/volumes/b-tool-dcompose_mongodb_data && sudo cp -r ./backup-db /var/lib/docker/volumes/b-tool-dcompose_mongodb_data"

control = ''
while control.lower() != 'override-database':
    control = input(f"{bcolors.WARNING}Are you sure do you want to override the database? This action will be irreversible\nType 'override-database' to continue: / 'n' to abort: {bcolors.ENDC}")
    if control.lower() == 'n':
        print(f"{bcolors.WARNING}Exiting the execution{bcolors.ENDC}")
        exit(1)

# Execute the command
result = subprocess.run(command, shell=True)

# Check if the command executed successfully
if result.returncode == 0:
    print(f"{bcolors.OKGREEN}Database exported successfully on /home/acampos/b-tool-dcompose_mongodb_data{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}Something went wrong exporting the database in /home/acampos/b-tool-dcompose_mongodb_data\n{result}{bcolors.ENDC}")
