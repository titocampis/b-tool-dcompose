FROM ubuntu:22.04

# Enable shell verbosity, 
#   update the system, install cron binary and python
RUN set -x && \
    apt-get update && \
    apt-get install -y cron python3 python3-pip

# TZone Configuration
## Set environment variable for non-interactive 
##     installation (the tzdata ask you for region)
ENV DEBIAN_FRONTEND=noninteractive 

## Installations and configurations to set Madrid TimeZone
## also reduce the image size cleaning up APT
RUN apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/Europe/Madrid /etc/localtime && \
    echo "Europe/Madrid" > /etc/timezone &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV TZ=Europe/Madrid

# Set the working directory inside the container
WORKDIR /app

# Copy python requirements file and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy crontab file
COPY crontab .

# Give right permissions to crontab file
#   schedule as job for the cron daemon the especified on crontab file
#   create the file to print the logs from cron
RUN chmod 0755 crontab && \
    crontab crontab && \
    touch /var/log/cron.log

# Copy the needed files
COPY utils/ utils/
COPY mongodb/filters.py mongodb/filters.py
COPY check_daily_birthdays.py check_daily_birthdays.py
COPY check_monthly_birthdays.py check_monthly_birthdays.py

# Initiate the cron daemon and print in the output
#    the content of /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
