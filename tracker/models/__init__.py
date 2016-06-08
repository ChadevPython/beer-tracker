# -*- coding: utf-8 -*-

from tracker import db


class ModelMixin(object):

    """ Mixin class for database model helper methods/attributes.

    To enable these helpers on models, ensure to include this mixin with your
    class definition:
            class MyModel(db.Model, ModelMixin):
                # model definition
    """

    def __repr__(self):
        return unicode(self.__dict__)

    def save(self):
        """ Save instance to database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Delete instance.
        """
        db.session.delete(self)
        db.session.commit()

    def deactivate(self):
        """ Deactivate an instance and update db record.
        """
        self.active = False
        self.save()

    def reactivate(self):
        """ Reactivate a deactivated instance.
        """
        self.active = True
        self.save()
