# How to create the virtual environment
1. Create the virtual environment:
```bash
python3 -m venv b-tool-venv
```

2. Activate the virtual environment:
```bash
source b-tool-venv/bin/activate
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python3 ....
```

The venv is stored in the repository, if you are not going to use the venv anymore, do: 

```bash
rm -rf b-tool-venv
```

To deactivate the venv:
```bash
deactivate
```

# How to override the database
You need to execute the script [mongodb/override_database.py](mongodb/override_database.py) and change the owner of the files to root

# Next Steps
1. Sort the project structure and folders
2. Finish the GUI
3. Use tha marlot email to send you notifications each 1 of the month of the birthdays of the month
4. Test python crons and play with them
5. Implement it as a cron job
