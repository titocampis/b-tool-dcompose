FROM ubuntu:22.04

# Copy crontab file
COPY crontab .


# Enable verbose for shell,
#   update the system, install cron binary, 
#   give right permissions to crontab file
#   schedule as job for the cron daemon the especified on crontab file
#   create the file to print the logs from cron
RUN set -x \
    && apt-get update \
    && apt-get install cron \
    && chmod 0755 crontab \
    && crontab crontab \
    && touch /var/log/cron.log

# Initiate the cron daemon and print in the output the content of /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
