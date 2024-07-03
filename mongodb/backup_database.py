from datetime import datetime

from mongodb import utilities_mongodb as ut

###############################################################################
############                    Configuration                     #############
###############################################################################

# WARNING! Remember to execute this script on the server
# which the running mongodb you want to backup
#
# WARNING! backups directory must exist

db_name = "friends_birthdays"
container_name = "mongodb"
folder = f"./backups/{db_name}-{datetime.today().strftime('%m-%d-%Y')}"

# Commands
command_docker_dump = (
    f"docker exec -it {container_name} mongodump --db {db_name} --out /tmp/"
)
command_docker_cp = f"docker cp {container_name}:/tmp/{db_name} {folder}"
command_docker_rm = f"docker exec -it {container_name} rm -rf /tmp/{db_name}"


###############################################################################
############                        Main                          #############
###############################################################################

# WARNING! Remember to execute this script on the server
# which the running mongodb you want to backup
#
# WARNING! backups directory must exist

# Execute the docker dump
ut.exec_command(command_docker_dump, True)

# Copy the file from the container to local
ut.exec_command(command_docker_cp)

# Remove the file inside the docker container
ut.exec_command(command_docker_rm)
