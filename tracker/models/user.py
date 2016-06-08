# -*- coding: utf-8 -*-

from arrow import utcnow
from sqlalchemy_utils import ArrowType
from flask_user import UserMixin
from sqlalchemy import Column, Integer, Boolean
from tracker import db
from tracker.models import ModelMixin


class User(db.Model, UserMixin, ModelMixin):
    id = Column(Integer, primary_key=True)

    # User authentication information
    username = Column(db.Unicode, nullable=False, unique=True)
    password = Column(db.Unicode, nullable=False, server_default='')
    reset_password_token = Column(
        db.Unicode, nullable=False, server_default='')

    # User email information
    email = Column(db.Unicode, nullable=False, unique=True)
    confirmed_at = Column(ArrowType, default=utcnow, nullable=False)

    # User information
    active = Column('is_active', Boolean(), nullable=False, server_default='0')
    first_name = Column(db.Unicode, nullable=False, server_default='')
    last_name = Column(db.Unicode, nullable=False, server_default='')
    receive_email = Column(Boolean, nullable=True, default=False)

    def __repr__(self):
        return self.username

    @property
    def is_admin(self):
        for user_role in self.roles:
            if user_role.name == 'admin':
                return True
        return False

    @property
    def is_super_admin(self):
        for user_role in self.roles:
            if user_role.name == 'super-admin':
                return True
        return False

    # Relationships
    roles = db.relationship('Role', secondary='user_roles',
                            backref=db.backref('users', lazy='dynamic'))


class UserRoles(db.Model, ModelMixin):
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = Column(Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class Role(db.Model, ModelMixin):
    id = Column(Integer(), primary_key=True)
    name = Column(db.Unicode, unique=True)
