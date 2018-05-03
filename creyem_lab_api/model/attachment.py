from marshmallow import Schema, fields


class Attachment():
    def __init__(self, _id, hotspot_id, text, created_at):
        self._id = _id
        self.hotspot_id = hotspot_id
        self.text = text
        self.created_at = created_at

    def __repr__(self):
        return '<Attachment(name={self.id!r})>'.format(self=self)


class AttachmentSchema(Schema):
    _id = fields.Str()
    hotspot_id = fields.Str()
    text = fields.Str()
    created_at = fields.DateTime()
