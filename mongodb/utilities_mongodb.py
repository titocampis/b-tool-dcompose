import subprocess

from utils.utilities import st


def exec_command(command: str, verbose: bool = False) -> None:
    """
    Method to execute a command on shell and check the result.

    Parameters:
    command (str): command to execute.
    verbose (str)

    Returns:
    None
    """
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,  # To raise exceptions if exit != 0
    )

    # Check if the command executed successfully
    if result.returncode == 0:
        print(st("green", f"[{command}]: Successfully executed!"))
        if verbose:
            print(result.stdout)

    else:
        print(st("fail", f"[{command}]\n{result}"))
