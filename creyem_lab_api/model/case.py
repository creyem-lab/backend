import datetime as dt

from marshmallow import Schema, fields


class Case():
    def __init__(self, _id, title):
        self._id = _id
        self.title = title

    def __repr__(self):
        return '<Case(name={self.title!r})>'.format(self=self)


class CaseSchema(Schema):
    _id = fields.Str()
    title = fields.Str()
