import subprocess

# Command to copy the directory
command = "sudo cp -r /var/lib/docker/volumes/b-tool-dcompose_mongodb_data /home/acampos/"

# Execute the command
subprocess.run(command, shell=True)