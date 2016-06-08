#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import csv
import arrow
from flask.ext.script import Server, Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask import url_for
from sqlalchemy_utils.functions import create_database, database_exists
from tracker import db
from tracker import app
from config import config
from tracker.models.user import User
import arrow


now = arrow.now()

logging.getLogger("requests").setLevel(logging.WARNING)
migrate = Migrate(app, db)
manager = Manager(app)


def _make_context():
    return dict(app=app, db=db, user=User)

manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

port = int(os.environ.get("PORT", 5000))
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=port)
)

@manager.command
def create_db():
    """Creates database if it doesn't exist."""
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_uri):
        print('Creating database ...')
        create_database(db_uri)
        db.create_all()
    else:
        print('Database already exists. Nothing to create.')


@manager.command
def routes():
    # Ran by: python manange.py routes
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote(
            "{:25s} {:25s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    manager.run()
