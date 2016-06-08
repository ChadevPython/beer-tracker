# -*- coding: utf-8 -*-

from flask_classy import FlaskView, route
from flask import render_template


__all__ = ('GeneralView')


class GeneralView(FlaskView):
    route_base = '/'

    @route('/', methods=('GET', 'POST'))
    def index(self):
        return render_template('index.html')
