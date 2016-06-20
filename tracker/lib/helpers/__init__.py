# -*- coding: utf-8 -*-

from flask_mail import Message
from flask import render_template
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
from tracker import mail
from config import config

# logging to log.txt file
logging_on = config.LOGGING_ON
print_log = config.PRINTLOG


def logit(data):
    """Writes data to a text file for logging purposes."""
    if logging_on:
        with open('log.txt', 'a') as f:
            f.write(data)
            f.write('\n')
        if print_log:
            print(data)
    else:
        print(data)

def send_email(to, subject, template, **kwargs):
    msg = Message(config.MAIL_SUBJECT_PREFIX + ' ' + subject,
                  sender=config.MAIL_SENDER, recipients=to)
    msg.to = to
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

def item_in_fields(item, fields):
    if item in fields:
        return fields[item]
    else:
        return None