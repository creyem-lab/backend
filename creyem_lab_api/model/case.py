from marshmallow import Schema, fields


class Case():
    def __init__(self, _id, title, created_at):
        self._id = _id
        self.title = title
        self.created_at = created_at

    def __repr__(self):
        return '<Case(name={self.title!r})>'.format(self=self)


class CaseSchema(Schema):
    _id = fields.Str()
    title = fields.Str()
    created_at = fields.DateTime()
