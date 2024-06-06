from datetime import datetime
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

############################################################################################
############                           Configuration                           #############
############################################################################################

# WARNING! Remember to execute this script on the server which the running mongodb you want
# to backup
#
# WARNING! backups directory must exist

db_name = 'friends_birthdays'
container_name = 'mongodb'
folder = f"./backups/{db_name}-{datetime.today().strftime('%m-%d-%Y')}"

# Commands
command_docker_dump = f"docker exec -it {container_name} mongodump --db {db_name} --out /tmp/"
command_docker_cp = f"docker cp {container_name}:/tmp/{db_name} {folder}"
command_docker_rm = f"docker exec -it {container_name} rm -rf /tmp/{db_name}"

############################################################################################
############                              Methods                              #############
############################################################################################

def exec_command(command:str, verbose:bool=False):
    '''Method to execute a command on shell and check the result'''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command executed successfully
    if result.returncode == 0:
        print(f"{bcolors.OKGREEN}[{command}]: Successfully executed!{bcolors.ENDC}")
        if verbose: print(result.stdout)
    
    else:
        print(f"{bcolors.FAIL}[{command}]: Something went wrong.\nError: {result}{bcolors.ENDC}")

############################################################################################
############                                Main                               #############
############################################################################################

# WARNING! Remember to execute this script on the server which the running mongodb you want
# to backup
#
# WARNING! backups directory must exist

# Execute the docker dump
exec_command(command_docker_dump, True)

# Copy the file from the container to local
exec_command(command_docker_cp)

# Remove the file inside the docker container
exec_command(command_docker_rm)
