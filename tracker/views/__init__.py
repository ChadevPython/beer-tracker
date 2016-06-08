# -*- coding: utf-8 -*-

from flask import render_template
from tracker.views.general import GeneralView
from tracker.views.user_profile import UserView

__all__ = ('init_views')


def init_views(app):
    register_error_handlers(app)
    GeneralView.register(app)
    UserView.register(app)


def register_error_handlers(app=None):
    """Register app error handlers.
    Raises error if app is not provided.
    """

    if app is None:
        raise ValueError('cannot register views on an empty app')

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(405)
    def method_not_allowed_error(error):
        return render_template('404.html'), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500
