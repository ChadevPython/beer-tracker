# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash
from flask import request, redirect, url_for
from flask_user import current_user
from tracker import db
from tracker.forms.profile import UserProfileForm

from flask_classy import FlaskView, route

__all__ = ('UserView')

class UserView(FlaskView):
    route_base = '/userprofile/'

    def index(self):
        """Landing page."""
        return render_template('index.html')


    @route('edit/profile', methods=('GET', 'POST'))
    def edit_profile(self):

        if request.method == 'GET':
            form = UserProfileForm(obj=current_user)
            return render_template('flask_user/edit_profile.html', form=form)

        form = UserProfileForm()
        if request.method == 'POST' and form.validate_on_submit():
            current_user.username = form.username.data
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.email = form.email.data
            current_user.save()
            flash(u'Profile has been successfully updated', 'success')
            return redirect(url_for('.index'))
