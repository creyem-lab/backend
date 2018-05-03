from marshmallow import Schema, fields


class Hotspot():
    def __init__(self, _id, case_id, pitch, yaw, hotspotType, text, created_at):
        self._id = _id
        self.case_id = case_id
        self.pitch = pitch
        self.yaw = yaw
        self.hotspotType = hotspotType
        self.text = text
        self.created_at = created_at

    def __repr__(self):
        return '<Hotspot(name={self.id!r})>'.format(self=self)


class HotspotSchema(Schema):
    _id = fields.Str()
    case_id = fields.Str()
    pitch = fields.Number()
    yaw = fields.Number()
    hotspotType = fields.Str()
    text = fields.Str()
    created_at = fields.DateTime()
