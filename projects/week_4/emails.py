#!/usr/bin/env bash

# You work at a company that sends daily reports to clients via email. The goal
# of this project is to automate the process of sending these reports via email.
#
# Here are the steps you can take to automate this process:
#   Use the smtplib library to connect to the email server and send the emails.
#   Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.
#   Use the os library to access the report files that need to be sent.
#   Use a for loop to iterate through the list of recipients and send the email and attachment.
#   Use the schedule library to schedule the script to run daily at a specific time.
#   You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process.

import os
import schedule
import smtplib
import sys
import time

from argparse import ArgumentParser
from email.message import EmailMessage


# these are set on my machine because I don't want my email credentials in git
USER = os.environ['GMAIL_EMAIL_ADDRESS']
PASS = os.environ['GMAIL_APP_PASSWORD']
LOGFILE = '.email_schedule_log'


def log(func):
    def timefmt():
        '''
        Returns a human-readable timestamp.
        '''
        return f'{time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())}'

    def _decorator(*args, **kwargs):
        with open(LOGFILE, 'a') as f:
            try:
                f.write(
                    f'[{timefmt()}] running scheduled job: {func.__name__}\n'
                )
                ret = func(*args, **kwargs)
                f.write(
                    f'[{timefmt()}] job completed successfully\n'
                )
                return ret
            except Exception as ex:
                f.write(
                    f'[{timefmt()}] error ocurred while running scheduled program: {ex}\n'
                )

    return _decorator


@log
def send_email(to: list[str], subject: str, message: str, files: list[str]):
    msg = EmailMessage()

    msg['From'] = USER
    msg['To'] = ','.join(to)
    msg['Subject'] = subject
    msg.set_content(message)

    for file in files:
        msg.add_attachment(open(file, 'r').read(), filename=file)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(USER, PASS)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('-t', '--to', metavar='email', nargs='+')
    args.add_argument('-s', '--subject', nargs='?')
    args.add_argument('-m', '--message', nargs='?')
    args.add_argument(
        '-f',
        '--files',
        metavar='attachment',
        nargs='*',
        default=[],
        help='files to attach to the email',
    )
    args = vars(args.parse_args(sys.argv[1:]))

    schedule.every().day.at("10:00", "Europe/Dublin").do(lambda: send_email(
        args['to'], args['subject'], args['message'], args['files']
    ))

    while True:
        schedule.run_pending()
        time.sleep(1)
