#! /usr/bin/env python
import requests
import re
import sys
import argparse
import time
from datetime import datetime
import smtplib, ssl
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Locally sourced credentials file.
import email_details


email_host = email_details.server['host']
email_port = email_details.server['port']


def run(search_term, endpoint, check_interval_sec):
    """
    Checks the result of hitting an endpoint for a term every X seconds.

    :param str search_term:        Term to scrape from the endpoint results.
    :param str endpoint:           Endpoint URL to hit for the searchable text.
    :param int check_interval_sec: Amount of time in seconds to wait before checking again.
    """
    while True:
        r = requests.get(url = endpoint)
        content_text = r.content

        if re.search(search_term, content_text, re.IGNORECASE):
            dt_current = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            send_notification_email(search_term.decode(), dt_current, endpoint)
            sys.exit(0)
        time.sleep(check_interval_sec)


def send_notification_email(search_term, time, endpoint):
    """
    Sends an email using the email details within `email_details.py` informing of search term discovery.

    :param str search_term: Term that was searched.
    :param str time:        Time that a hit was found.
    :param str endpoint:    URL whose result was checked for the term.
    :raises SMTPAuthenticationError: If authentication fails for the details specified.
    """
    msg = MIMEMultipart()
    s = smtplib.SMTP(host = email_host, port = email_port)
    s.starttls()
    s.login(email_details.credentials['username'], email_details.credentials['password'])

    message_template = read_template('message_template.txt')
    message_body = message_template.substitute(SEARCH_TERM = search_term, TIME = time, ENDPOINT = endpoint)

    msg['From'] = email_details.credentials['username']
    msg['To'] = email_details.recipient
    msg['Subject'] = 'Search term match (Python script)'
    msg.attach(MIMEText(message_body, 'html'))

    s.send_message(msg)
    s.quit()


def read_template(filename):
    """
    Reads a template file into a usable object.

    :param str filename: Name of the file to use as a template.
    :return: A template containing the message to be emailed.
    :rtype: Template
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wait until a term is successfully retrieved from an endpoint.")
    parser.add_argument("search_term", type=str, help="Text to periodically check for.")
    parser.add_argument("endpoint", type=str, help="URL to scrape for the search term.")
    parser.add_argument("check_interval_min", type=int, help="Time in minutes to wait before checking again.")
    args = parser.parse_args()

    run(args.search_term.encode(), args.endpoint, args.check_interval_min * 60)
