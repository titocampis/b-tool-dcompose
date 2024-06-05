# Birthday Tool with Docker Compose

The idea of this mini project is to be the best friend of the world!! One of the bigest problems of a good friend is always remember the birthdays of your friends... But being honest, it is not always possible. That's why I developed this tool, to run into a raspberry pi (or wherever because it is implemented in docker). It will always remember you the birthday of your friends in order you can be the friend you always wanted to be! :tada:

For this, we will need:
1. A docker container running a mongodb database with all the birthdays of my friends
2. Another docker container with 2 cronjobs:
    - 1 job executed each day at 00:00 to check if it is the birthday of some of my friends, and in case it is, send a mail to my mailbox notifying me about it and with the years he or she is turning
    - 1 job executed the 1st day of each month to check and send all the birthdays of the month to my mailbox with the same information

## MongoDB Database Container
A mongodb database containing all your friends data:
- full name
- alias
- birth
- birth.month
- phone
- sex

### Docker Build
Nothing to build, because I use the default mongodb image. You can pull the image: 
```bash
docker pull mongo:latest
```

### Docker Compose Config
It can be checked on [docker-compose.yml](docker-compose.yml)

### Running the container
```bash
docker compose up -d mongodb
```

### Execute actions once the database is running
To execute actions on the database, you should execute the python script [main_db.py](main_db.py).

> :paperclip: It is recommended to use a python virtual environment
> - Create the virtual environment if it is not created: ```python3 -m venv b-tool-venv```
> - Activate it: ```source b-tool-venv/bin/activate```
> - Install the requirements on it: ```pip install -r requirements_mongodb.txt```
> - To deactivate it: ```deactivate``` 

You can retrieve ideas of how to use it checking [mongodb/examples.py](mongodb/examples.py)

#### Make queries on the database
You can insert friends by different ways, update them, remove them... Check all the methods available in [mongodb/internal_queries.py](mongodb/internal_queries.py)

#### Retrieve data from database
You can get all friends, retrieve a friend by its name, retrieve a friend by its alias get friends with birthday in specific Check all the methods available in [mongodb/filters.py](mongodb/filters.py)month... 

### How to backup the database?
```bash
python3 mongodb/backup_database.py
```
You can check the content of the file: [mongodb/backup_database](mongodb/backup_database)

### How to override the database with the backup
You need to execute the script [mongodb/override_database.py](mongodb/override_database.py) and change the owner of the files to root

## Cronjobs Container
Docker container with 2 cronjobs scheduled
- 1 job executed each day at 00:00 to check if it is the birthday of some of my friends, and in case it is, send a mail to my mailbox notifying me about it and with the years he or she is turning
- 1 job executed the 1st day of each month to check and send all the birthdays of the month to my mailbox with the same information

### Cronjobs Image Build
We can check the configuration of the image in [Dockerfile](Dockerfile)

```bash
docker build -t cron-container .
```

> :paperclip: **NOTE:** [.dockerignore](.dockerignore) file contains the directories / files to not to be included when copy or add in the docker image.

### Docker Compose Config
It can be checked on [docker-compose.yml](docker-compose.yml)


### Secrets

In order to export the `mail_username` and the `mail_password` from the `mail service` we use **docker secrets**. So before running the application, you should fulfill the content of the following files:

- `secret_mail_username.conf`
- `secret_mail_password.conf`


### Cronjobs Container Run
```bash
docker compose up -d cron
```

### Local Tests
:one: Fulfill the following files with the sensitive data:
- `secret_mail_username.conf`
- `secret_mail_password.conf`

:two: Run the following on your terminal
```bash
export SECRET_MAIL_USERNAME_FILE="./secret_mail_username.conf" && \
export SECRET_MAIL_PASSWORD_FILE="./secret_mail_password.conf"
```

:three: Run the application
```bash
python3 check_daily_birthdays.py
```

> :paperclip: It is recommended to use a python virtual environment
> - Create the virtual environment if it is not created: ```python3 -m venv b-tool-venv```
> - Activate it: ```source b-tool-venv/bin/activate```
> - Install the requirements on it: ```pip install -r requirements_mongodb.txt```
> - To deactivate it: ```deactivate``` 

## Next Steps
| Status | Task |
|----------|----------|
| :white_check_mark: | Define the function check_daily_birthdays.py |
| :white_check_mark: | Define the function check_monthly_birthdays.py |
| :white_check_mark: | Check how to do with the secrets and docker compose |
| :white_check_mark: | Check if .env is needed on the docker image |
| :white_check_mark: | Test to run the scripts using docker-compose (without sending the email, just printing the value of the secrets) |
| :hourglass_flowing_sand: | Clone the webapp to this branch, test it but dont remove pupurri (to let horoscope calc) |
| :hourglass_flowing_sand: | Test the cronjobs on your laptop |
| :hourglass_flowing_sand: | Do the repository for ansible-raspberry pi |
| :hourglass_flowing_sand: | Clone the repository and test it on the raspberry |
