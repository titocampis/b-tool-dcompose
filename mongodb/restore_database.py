from mongodb import utilities_mongodb as ut


class bc:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


###############################################################################
############                    Configuration                     #############
###############################################################################

# WARNING! Remember to execute this script on the server
# which the running mongodb you want to override
#
# WARNING! You need to modify the path variable

db_name = "friends_birthdays"
container_name = "mongodb"

## NEED TO BE MODIFIED
folder = f"./backups/{db_name}-06-06-2024"

# Commands
command_docker_cp = f"docker cp {folder} {container_name}:/tmp/{db_name} "
# mongorestore --db <database_name> <path/to/dump/file>
command_docker_restore = (
    f"docker exec -it {container_name} mongorestore "
    f"--db {db_name} /tmp/{db_name}"
)
command_docker_rm = f"docker exec -it {container_name} rm -rf /tmp/{db_name}"


###############################################################################
############                        Main                          #############
###############################################################################

# WARNING! Remember to execute this script on the server
# which the running mongodb you want to override
#
# WARNING! backups directory must exist

# Copy the folder to the docker container
ut.exec_command(command_docker_cp, True)

# Execute inside the container the mongorestore
ut.exec_command(command_docker_restore, True)

# Remove the file inside the docker container
ut.exec_command(command_docker_rm)
