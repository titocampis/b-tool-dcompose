# Birthday Tool with Docker Compose 🎉

Imagine a world where you never miss a friend's birthday again. This project aims to be the ultimate companion, ensuring you remember every special day. One of the greatest challenges of being a good friend is keeping track of birthdays; but let’s face it, life gets busy. That's when this tool comes into play, designed to run on a Raspberry Pi (or any environment, thanks to Docker). It will faithfully remind you of your friends’ birthdays, helping you become the thoughtful friend you’ve always aspired to be! 🎉

To bring this idea to life, we will set up:

- A Docker container hosting a MongoDB database to store all your friends' birthdays.
- Another Docker container with two crucial cron jobs:
    - A daily job at midnight that checks if it's anyone's birthday and sends an email notification with their age.
    - A monthly job on the 1st, summarizing all the upcoming birthdays and sending a comprehensive email with the same details.

Get ready to impress your friends with your impeccable memory and thoughtfulness!

## Index
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [MongoDB Database Container](#mongodb-database-container)
   - [Docker Build](#docker-build)
   - [Docker Compose Config](#docker-compose-config)
   - [Running the Container](#running-the-container)
   - [Execute Actions Once the Database is Running](#execute-actions-once-the-database-is-running)
   - [How to Backup the Database](#how-to-backup-the-database)
4. [Cronjobs Container](#cronjobs-container)
   - [Send Email](#send-email)
       - [SMTP](#smtp)
       - [Enable Google Apps Authentication](#enable-google-apps-authentication)
   - [Cronjobs Image Build](#cronjobs-image-build)
   - [Docker Compose Config](#docker-compose-config-1)
   - [Secrets](#secrets)
   - [Cronjobs Container Run](#cronjobs-container-run)
   - [Local Tests](#local-tests)
   - [Release new cron-container version on Production](#release-new-cron-container-version-on-production)
5. [Web Server](#web-server)
   - [How to Run It](#how-to-run-it)
6. [Pre-commit](#pre-commit)
   - [What is Pre-commit?](#what-is-pre-commit)
   - [Steps to configure precommit](#steps-to-configure-precommit)
       - [Install the package](#install-the-package)
       - [Configure the hooks](#configure-the-hooks)
   - [Install the hooks](#install-the-hooks)
   - [Enjoy your precommit!](#enjoy-your-precommit)
7. [Next Steps](#next-steps)

## Project Structure
```bash
mongodb/ #
    ├── __init__.py # File for python to consider this folder as python package
    ├── backup_database.py # Script to extract a dump from a mongodb
    ├── examples.py # Queries examples to execute on the mongodb
    ├── filters.py # Queries to execute from outside the database and request data
    ├── init_mongo.py # Script to define the rules from a new database (if not restored)
    ├── internal_queries.py # Queries for the internal mongodb management (create indexes, configure db, etc.)
    └── restore_database.py # Script to restore a database from a mongodb dump file
static/ # Web server static content
    ├── css/ # Styles
    └── img/ # Pictures
templates/ # Web server templates to render from controller
    └── base.html # The only template to render
utils/ # Folder containing the shared utilities used in all components
    ├── send_mail.py # Standard method to send an email
    └── utilitites.py # Other methods shared between all components
.dockerignore # File including all the files and folders to no push into docker images
.gitignore # File including all the files and folders to not push into git
check_daily_birthdays.py # File to be executed every day at 00:00 to check if it's the birthday of some friend
                         # and if it is the case, send an email
check_mongo_backup.py # File to check that the mongodb backup has been done successfully
check_monthly_birthdays.py # File to be executed every month 1st sending via email all the birthdays of the month
crontab # File with the jobs configured
docker-compose.yaml # File with the configuration for all docker containers
Dockerfile # Cron image composition file
main_db.py # Python script to execute queries into db
README.md # Repository documentation
requirements.txt # File with python modules to install
webapp.pym # Webapp controller in Flask to server the web
```

## MongoDB Database Container
A mongodb database containing all friends data:
- full name
- alias
- birth
- birth.month
- phone
- sex

### Docker Build
Nothing to build, because I use the default mongodb image. Image can be pulled:
```bash
docker pull mongo:latest
```

### Docker Compose Config
It can be checked on [docker-compose.yaml](docker-compose.yaml)

### Running the container
```bash
docker compose up -d mongodb
```

### Execute actions once the database is running
To execute actions on the database, the following python script [main_db.py](main_db.py) should be executed.

> :paperclip: It is recommended to use a python virtual environment
> - Create the virtual environment if it is not created: ```python3 -m venv .venv```
> - Activate it: ```source .venv/bin/activate```
> - Install the requirements on it: ```pip install -r requirements.txt```
> - To deactivate it: ```deactivate```

Ideas of how to use it checking [mongodb/examples.py](mongodb/examples.py)

#### Make queries on the database
Friends can be inserted by different ways, updated, removed... Check all the methods available in [mongodb/internal_queries.py](mongodb/internal_queries.py)

#### Retrieve data from database
All friends can be retrieved, as well as friends by its name, by its alias, retrieve friends with birthday in specific month, etc. Check all the methods available in [mongodb/filters.py](mongodb/filters.py)

### How to backup the database?
With this process we are going to replicate exactly the mongodb, with all the documents and also the indexes.

In order to backup database we are going to use:
- [mongodb/backup_database.py](mongodb/backup_database.py): which will access the source docker container running the database and dump all data into a local folder `backups/friends_birthdays-%m-%d-%Y`
- By hand, because depending on the database and where the backup of the db is going to be made, it will be a completely different process, I hardly recommend to use `sftp` i both flavours (get/put) to the full path of the backup directory
- [mongodb/restore_database.py](mongodb/restore_database.py): which will copy the backup file into the target docker container running the database and execute a mongorestore.

**The process is:**
:one: Have the repository cloned in the machine running the source mongodb, if not:
```bash
git clone https://github.com/titocampis/b-tool-dcompose.git
```

:two: Access the repository

:three: Ensure that the mongodb container is running:
```bash
docker ps
```

:four: Ensure that the `backups/` folder is created, if not:
```bash
mkdir backups
```

:five: Activate the python venv:
```bash
source venv-name/bin/activate
```

> [!NOTE]
> If the python venv is not created:
> ```bash
> python3 -m venv <venv-name>
> ```
> ```bash
> pip3 install -r requirements.txt
> ```

:six: Execute the [mongodb/backup_database.py](mongodb/backup_database.py) script:
```bash
python3 mongodb/backup_database.py
```

:seven: The backup file will be created, so it must be send to the target host. It can be done by multiple ways, but i recommend sftp using both flavours (get / put) with the full backup directory path.

:eight: Access the host where the override is going to be made.

:nine: Repeat until step 6 on the target mongodb host.

:ten: Execute the [mongodb/restore_database.py](mongodb/restore_database.py) script:
```bash
python3 mongodb/restore_database.py
```

Now, check the mongodb has been correctly backed up running:
```bash
python3 check_mongo_backup.py
```

## Cronjobs Container
Docker container with 2 cronjobs scheduled:
- 1 job executed each day at 00:00 to check if it is the birthday of some of my friends, and in case it is, send a mail to my mailbox notifying me about it and with the years he or she is turning
- 1 job executed the 1st day of each month to check and send all the birthdays of the month to my mailbox with the same information

### Send Email
#### SMTP
To send the email we use [smtplib](https://docs.python.org/3/library/smtplib.html) python library which provides a way to send email using the Simple Mail Transfer Protocol (SMTP). It provides methods for logging in to an SMTP server using a username and password which we are going to use and allows sending emails by specifying sender and recipient addresses, subject, and body. It supports plain text and MIME (Multipurpose Internet Mail Extensions) emails.

So we use [smtplib](https://docs.python.org/3/library/smtplib.html) to authenticate in our Google account and send email through this account.

#### Enable Google Apps Authentication
:one: Go into `Google Account Management`:

![alt text](static/img/jiminy.png)

:two: Go to `Security`.

:three: Turn ON `2-Step Verification` (if it is not already enabled).

:four: On the same page as `2-Step Verification`, go to `App passwords`:

![alt text](static/img/app_pwd.png)

:five: Create a new `app password` to authenticate into Google Account using apps.

### Cronjobs Image Build
We can check the configuration of the image in [Dockerfile](Dockerfile).

```bash
docker build -t cron-container .
```

> [!NOTE]
> [.dockerignore](.dockerignore) file contains the directories / files to not to be included when copy or add in the docker image.

### Docker Compose Config
It can be checked on [docker-compose.yaml](docker-compose.yaml)


### Secrets
In order to export the `mail_username` and the `mail_password` from the `mail service` we use **docker secrets**. So before running the application, the content of the following files must be fulfilled:

- `secret_mail_username.conf`
- `secret_mail_password.conf`


### Cronjobs Container Run
```bash
docker compose up -d cron
```

### Local Tests
:one: Fulfill the following files with the sensitive data (just if you wanna test send_email):
```bash
vim secret_mail_username.conf
```
```bash
vim secret_mail_password.conf
```

> [!CAUTION]
> Use `vim` or another text editor to fulfill the content of these files, do not do it through the terminal, because it may be a security weakness to have sensitive raw data in terminal history. Alternatively, you can do for both:
> - `cat > secret_mail_username.conf`
> - type the content + `Enter`
> - `Ctrl+D`

:two: Run the following on terminal:
```bash
export SECRET_MAIL_USERNAME_FILE="./secret_mail_username.conf" && \
export SECRET_MAIL_PASSWORD_FILE="./secret_mail_password.conf"
```

:three: Run the script:
```bash
python3 check_daily_birthdays.py
```

:four: Remove the sensitive data files:
```bash
rm -rf secret*
```

> :paperclip: It is recommended to use a python virtual environment:
> - Create the virtual environment if it is not created: ```python3 -m venv .venv```
> - Activate it: ```source .venv/bin/activate```
> - Install the requirements on it: ```pip install -r requirements.txt```
> - To deactivate it: ```deactivate```

### Release new `cron-container` version on Production

:one: Access production server

:two: Pull the last version of the `main` branch / clone this repository:
```bash
git pull -v --all
```

:three: Build the new released version of the docker image:
```bash
docker build -t cron-container .
```

:four: Fulfill the following files with the sensitive data (just if you wanna test send_email):
```bash
vim secret_mail_username.conf
```
```bash
vim secret_mail_password.conf
```

> [!CAUTION]
Use `vim` or another text editor to fulfill the content of these files, do not do it through the terminal, because it may be a security weakness to have sensitive raw data in terminal history. Alternatively, you can do for both:
> - `cat > secret_mail_username.conf`
> - type the content + `Enter`
> - `Ctrl+D`

:five: Run the docker container using `docker compose`:
```bash
docker compose up -d
```

:six: Execute `check_mongo_backup.py` in the new `cron-container` just created:
- Just db connection:
```bash
docker exec cron-container export MONGO_HOST=mongodb; python3 check_mongo_backup.py
```

:seven: (Just if you wanna test the email send):

- Access the `cron-container`:
```bash
docker exec -it cron-container /bin/bash
```

- Inside the docker container, export the following variables:
```bash
export MONGO_HOST=mongodb; export SECRET_MAIL_USERNAME_FILE="/run/secrets/secret_mail_username"; export SECRET_MAIL_PASSWORD_FILE="/run/secrets/secret_mail_password"
```

- Execute inside the container `check_monthly_birthdays.py`:
```bash
python3 check_monthly_birthdays.py
```

:eight: Remove the sensitive data files:
```bash
rm -rf secret*
```

## Web Server

In this repository, we also have a lite webserver showing the birthdays of my friends:

- [webapp.py](webapp.py): file with the controller of the webapp
- [static/](static/): static content to show on the web page: images, css (styles)
- [templates/](templates/): templates to render by the controller
- :paperclip: it also uses functions from [utils/](utils/)

### How to run it

As it is a very lite webserver, we do not develop to run it using docker, it will run directly from python:

:one: Activate the python venv:
```bash
source venv-name/bin/activate
```

> [!NOTE]
> If the python venv is not created:
> ```bash
> python3 -m venv <venv-name>
> ```
> ```bash
> pip3 install -r requirements.txt
> ```

:two: Run the [webapp.py](webapp.py) script:
```bash
python3 webapp.py
```

:three: Access in your browser: [http://localhost:8080](http://localhost:8080)

> [!IMPORTANT]
> The webserver is running on debug mode, so you can make hot changes and with Ctrl+s will be applied at the moment.

## Pre-commit
### What is Pre-commit?
Pre-commit is a python framework for managing and maintaining multi-language pre-commit hooks. These hooks are scripts that run automatically before you make a commit in your version control system, such as Git. They help to ensure code quality, consistency, and adherence to coding standards by performing checks and modifications to your code before it is committed to the repository.

### Steps to configure precommit

#### Install the package
:one: Activate the python virtual environment:
```bash
source .venv/bin/activate
```

:two: Install pre-commit package:
```bash
pip install pre-commit
```

#### Configure the hooks
Pre-commit uses a configuration file, usually named .pre-commit-config.yaml, placed in the root directory of your repository. This file specifies the hooks you want to use. Each hook can be a check like linting, formatting, security checks, or custom scripts.

You can check [.pre-commit-config.yaml](.pre-commit-config.yaml)

As well, each hook has its own file configuration, check the hooks documentation to learn how to configure them:
- isort: [.isort.cfg](.isort.cfg)
- pylint: [.pylintrc](.pylintrc)
- flake8: [.flake8](.flake8)

### Install the hooks
:three: Install hooks configured inside [.pre-commit-config.yaml](.pre-commit-config.yaml):
```bash
pre-commit install
```
> [!NOTE]
> Some of the Hooks used:
> * [trailing-whitespace](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace)
> * [end-of-file-fixer](https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer)
> * [black](https://pypi.org/project/black/)
> * [isort](https://pypi.org/project/isort/)
> * [pylint](https://pypi.org/project/pylint/)
> * [flake8](https://github.com/PyCQA/flake8)

### Enjoy your precommit!
Hooks run automatically on git commit. If a hook fails, the commit will be aborted, and you’ll need to fix the issues before committing again.

You can also run all the hooks on all files (not just the files staged for commit) using:
```bash
pre-commit run --all-files
```

Or just run an specific hook: `pre-commit run <hook-id> --all-files`
```bash
pre-commit run check-yaml --all-files
```

To just check specific files / folders:
```bash
pre-commit run <hook-id> --files path/to/file1 path/to/folder1/
```

## Next Steps
| Status | Task                                         |
|--------------------|----------------------------------|
| :white_check_mark: | Change the way you backup the db |
| :white_check_mark: | Think where put webapp but dont remove pupurri (to let horoscope calc) |
