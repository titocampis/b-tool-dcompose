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
# to override
#
# WARNING! You need to modify the path variable

db_name = 'friends_birthdays'
container_name = 'mongodb'

## NEED TO BE MODIFIED
folder = f"./backups/{db_name}-06-06-2024"

# Commands
command_docker_cp = f"docker cp {folder} {container_name}:/{db_name} "
# mongorestore --db <database_name> <path/to/dump/file>
command_docker_restore = f"docker exec -it {container_name} mongorestore --db {db_name} {db_name}"
command_docker_rm = f"docker exec -it {container_name} rm -rf {db_name}"

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

# Copy the folder to the docker container
exec_command(command_docker_cp, True)

# Execute inside the container the mongorestore
exec_command(command_docker_restore, True)

# Remove the file inside the docker container
exec_command(command_docker_rm)
